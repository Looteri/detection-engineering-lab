# IR-001 — Full Attack Chain: Recon → Exploit → Post-Exploitation

**Author:** Looteri  
**Date:** 2026-03-27 / 2026-03-30  
**Classification:** Lab Exercise — Detection Engineering Portfolio  
**Environment:** Kali Linux + T-Pot (Cowrie, Suricata, Dionaea) + Metasploitable2  
**Status:** Completed

---

## Executive Summary

A simulated threat actor conducted a multi-phase attack spanning three days
against lab infrastructure. Starting with network reconnaissance, the attacker
progressed through SMB exploit probing, SSH brute force credential access,
and full system compromise via a backdoored FTP service — achieving root
shell access and credential exfiltration on the target host.

Detection coverage was partial: Suricata identified recon and exploit probe
activity, while post-exploitation phases generated no alerts under the
default ruleset.

---

## Timeline of Events

| Timestamp 	   | 		Phase 		| Technique 		| Source   | 	Detection 		|
|------------------|----------------------------|-----------------------|----------|----------------------------|
| 2026-03-26 12:39 | 	Recon 			| T1046 Nmap -sV 	| Suricata | ET SCAN Nmap User-Agent	|
| 2026-03-27 11:09 | 	Exploit Probe 		| T1190 EternalBlue 	| Suricata | ET EXPLOIT MS17-010 	|
| 2026-03-27 11:12 | 	Exploit Probe 		| T1190 DoublePulsar 	| Suricata | ET EXPLOIT DoublePulsar	|
| 2026-03-27 14:44 | 	Exploitation 		| CVE-2011-2523 vsftpd  | Suricata | No alert			|
| 2026-03-27 14:44 | 	Credential Access 	| T1003.008 /etc/shadow | Local    | No alert			|
| 2026-03-27 14:44 | 	Exfiltration 		| T1005 /etc/passwd 	| Local    | No alert			|
| 2026-03-30 09:18 | 	Brute Force 		| T1110.001 SSH 	| Cowrie   | cowrie.login.failed	|
| 2026-03-30 09:18 | 	Access Gained 		| T1110.001 SSH 	| Cowrie   | cowrie.login.success	|

![timeline](screenshots/IR-001-full-attack-chain-timeline.png)

---

## Attack Phases

### Phase 1 — Reconnaissance

**Technique:** T1046 — Network Service Discovery  
**Tool:** Nmap `-sV`  
**Target:** 10.20.124.124 / 192.168.232.129

Attacker performed service version scan revealing vsftpd 2.3.4,
SMB on port 445, and multiple web services.

**Detection:** Suricata fired `ET SCAN Possible Nmap User-Agent Observed`
immediately — confirming that aggressive scans with version detection
are reliably detected by default ET ruleset.

**Reference:** [T1046 writeup](../../attack-simulations/T1046-nmap-network-scan/writeup.md)

---

### Phase 2 — Exploit Probing

**Technique:** T1190 — Exploit Public-Facing Application  
**Tool:** Metasploit `auxiliary/scanner/smb/smb_ms17_010`  
**Target:** 10.20.124.124 (Dionaea)

Scanner confirmed MS17-010 vulnerability and DoublePulsar backdoor
presence (simulated by Dionaea). Full exploitation failed — Dionaea
does not implement complete SMB protocol.

**Detection:** Suricata fired three signatures:
- `ET EXPLOIT Possible ETERNALBLUE Probe MS17-010 (MSF style)`
- `ET EXPLOIT Possible ETERNALBLUE Probe MS17-010 (Generic Flags)`
- `ET EXPLOIT [PTsecurity] DoublePulsar Backdoor installation communication`

**Reference:** [T1190 writeup](../../attack-simulations/T1190-eternalblue-ms17-010/writeup.md)

---

### Phase 3 — Credential Access via Brute Force

**Technique:** T1110.001 — Brute Force: Password Guessing  
**Tool:** Hydra with Default Credentials wordlist  
**Target:** 10.20.124.124 (Cowrie SSH honeypot)

Attacker performed SSH brute force — Cowrie logged 1,151 failed attempts
and 1 successful login (`<N/A>:admin`). Session `b704583dd59f` lasted
132ms with no post-login commands — consistent with automated
credential harvesting, not interactive access.

**Detection:** Cowrie logged full session including
`cowrie.login.failed` and `cowrie.login.success` events.

**Reference:** [T1110.001 writeup](../../attack-simulations/T1110.001-ssh-brute-force/writeup.md)

---

### Phase 4 — Exploitation & Post-Exploitation

**Technique:** T1190 CVE-2011-2523, T1003.008, T1005  
**Tool:** Metasploit `exploit/unix/ftp/vsftpd_234_backdoor`  
**Target:** 192.168.232.129 (Metasploitable2)

vsftpd 2.3.4 backdoor triggered via FTP username containing `:)`.
Root shell obtained immediately. Post-exploitation activities:

- System discovery: `sysinfo`, `getuid`, `ipconfig`
- Credential access: `/etc/shadow` dumped (all password hashes exposed)
- Exfiltration: `/etc/passwd` downloaded to attacker machine

**Detection:** Zero Suricata alerts across all post-exploitation phases.
Wireshark pcap (`atak_01.pcap`) provides forensic evidence of
backdoor trigger sequence.

**Reference:** [CVE-2011-2523 writeup](../../attack-simulations/CVE-2011-2523-vsftpd-backdoor/writeup.md)

---

## Detection Gap Summary

| 	Phase 		  | Detected?   | 			Detail 					|
|-------------------------|-------------|---------------------------------------------------------------|
| Recon (Nmap -sV) 	  |    YES 	| ET SCAN Nmap User-Agent 				 	|
| EternalBlue probe 	  |    YES 	| ET EXPLOIT MS17-010 (x2) 					|
| vsftpd backdoor trigger |    NO 	| FTP `:)` pattern not in ET ruleset 				|
| vsftpd backdoor shell   |   PARTIAL 	| GPL ATTACK_RESPONSE port 6200 — detected AFTER shell spawned 	|
| /etc/shadow access 	  |    NO 	| No file integrity monitoring 					|
| Exfiltration 		  |    NO 	| No data loss detection 					|

**4 of 6 phases detected** — however vsftpd detection is reactive,
not preventive. Shell was already running when alert fired.
Custom rule targeting FTP trigger pattern would shift detection
left by approximately 30 seconds.

---

## Correlation Query (ES|QL)
```esql
FROM logstash-*
| WHERE type IN ("Suricata", "Cowrie", "Dionaea")
  AND src_ip == 10.20.8.85"
| EVAL phase = CASE(
    type == "Suricata" AND alert.signature LIKE "*Nmap*", "Phase 1 - Recon",
    type == "Suricata" AND alert.signature LIKE "*ETERNALBLUE*", "Phase 2 - Exploit Probe",
    type == "Suricata" AND alert.signature LIKE "*DoublePulsar*", "Phase 2 - Exploit Probe",
    type == "Dionaea", "Phase 2 - Honeypot Interaction",
    type == "Cowrie" AND eventid == "cowrie.login.failed", "Phase 3 - Brute Force",
    type == "Cowrie" AND eventid == "cowrie.login.success", "Phase 3 - Access Gained",
    "Other"
  )
| WHERE phase != "Other"
| KEEP @timestamp, type, src_ip, phase, alert.signature, eventid
| SORT @timestamp ASC
```

---

## Recommendations

1. **Add custom Suricata rule** for vsftpd backdoor FTP trigger —
   alert on `USER :)` pattern on port 21 to detect exploitation
   before shell spawns. Current GPL rule (SID:2100498) fires only
   after successful shell execution — too late for prevention.
2. **Deploy file integrity monitoring** — `/etc/shadow` access
   should generate immediate critical alert
3. **Implement network behavioral detection** — unexpected outbound
   connections on port 6200 indicate vsftpd backdoor success
4. **Correlate low-confidence alerts** — Nmap scan followed by
   EternalBlue probe from same IP within 30 minutes indicates
   active threat actor, not coincidence
5. **SSH honeypot alerting** — `cowrie.login.success` should
   trigger immediate investigation regardless of credentials used
