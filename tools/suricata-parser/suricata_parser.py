#!/usr/bin/env python3
import json
import argparse
from collections import defaultdict
from datetime import datetime
from pathlib import Path
 
 
def load_alerts(eve_path: str) -> list[dict]:
    alerts = []
    skipped = 0
    with open(eve_path, "r") as f:
        for line in f:
            try:
                event = json.loads(line.strip())
                if event.get("event_type") == "alert":
                    if not event.get("src_ip") or not event.get("dest_ip"):
                        skipped += 1
                        continue
                    alerts.append(event)
            except json.JSONDecodeError:
                continue
    if skipped:
        print(f"[*] Skipped {skipped} non-IP alert(s) (e.g. Ethertype unknown)")
    return alerts
 
 
def group_by_signature(alerts: list[dict]) -> dict:
    grouped = defaultdict(list)
    for alert in alerts:
        sig = alert.get("alert", {}).get("signature", "Unknown Signature")
        grouped[sig].append(alert)
    return grouped
 
 
def format_row(alert: dict) -> str:
    ts       = alert.get("timestamp", "N/A")[:19].replace("T", " ")
    src_ip   = alert.get("src_ip", "N/A")
    src_port = alert.get("src_port", "N/A")
    dst_ip   = alert.get("dest_ip", "N/A")
    dst_port = alert.get("dest_port", "N/A")
    proto    = alert.get("proto", "N/A")
    severity = alert.get("alert", {}).get("severity", "N/A")
    return f"| {ts} | {src_ip}:{src_port} | {dst_ip}:{dst_port} | {proto} | {severity} |"
 
 
def generate_report(grouped: dict, total: int, source_file: str) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = []
 
    lines.append("# Suricata Alert Report")
    lines.append(f"\n**Generated:** {now}  ")
    lines.append(f"**Source:** `{source_file}`  ")
    lines.append(f"**Total alerts:** {total}  ")
    lines.append(f"**Unique signatures:** {len(grouped)}  ")
 
    lines.append("\n---\n")
    lines.append("## Summary\n")
    lines.append("| Signature | Count |")
    lines.append("|-----------|-------|")
    for sig, events in sorted(grouped.items(), key=lambda x: -len(x[1])):
        lines.append(f"| {sig} | {len(events)} |")
 
    lines.append("\n---\n")
    lines.append("## Alerts by Signature\n")
 
    for sig, events in sorted(grouped.items(), key=lambda x: -len(x[1])):
        severity = events[0].get("alert", {}).get("severity", "N/A")
        category = events[0].get("alert", {}).get("category", "N/A")
        sid      = events[0].get("alert", {}).get("signature_id", "N/A")
 
        lines.append(f"### {sig}")
        lines.append(f"- **SID:** {sid}")
        lines.append(f"- **Category:** {category}")
        lines.append(f"- **Severity:** {severity}")
        lines.append(f"- **Hit count:** {len(events)}\n")
        lines.append("| Timestamp | Source | Destination | Proto | Severity |")
        lines.append("|-----------|--------|-------------|-------|----------|")
        for alert in events[:20]:  # cap at 20 rows per signature
            lines.append(format_row(alert))
        if len(events) > 20:
            lines.append(f"\n> _{len(events) - 20} additional events truncated._")
        lines.append("")
 
    return "\n".join(lines)
 
 
def main():
    parser = argparse.ArgumentParser(
        description="Parse Suricata eve.json and generate a Markdown report."
    )
    parser.add_argument(
        "-i", "--input",
        default="/var/log/suricata/eve.json",
        help="Path to eve.json (default: /var/log/suricata/eve.json)"
    )
    parser.add_argument(
        "-o", "--output",
        default="suricata_report.md",
        help="Output Markdown file (default: suricata_report.md)"
    )
    args = parser.parse_args()
 
    if not Path(args.input).exists():
        print(f"[ERROR] File not found: {args.input}")
        raise SystemExit(1)
 
    print(f"[*] Loading alerts from: {args.input}")
    alerts = load_alerts(args.input)
    print(f"[*] Found {len(alerts)} alert(s)")
 
    if not alerts:
        print("[!] No alerts found. Exiting.")
        raise SystemExit(0)
 
    grouped = group_by_signature(alerts)
    report  = generate_report(grouped, len(alerts), args.input)
 
    with open(args.output, "w") as f:
        f.write(report)
 
    print(f"[+] Report saved to: {args.output}")
 
 
if __name__ == "__main__":
    main()
