# Detection Engineering Lab

Personal home lab focused on simulating adversary techniques,
building SIGMA detection rules, and validating detection coverage
in Elastic Stack and Suricata IDS.

## Stack
- T-Pot (Cowrie, Suricata, Dionaea)
- Kali Linux + Metasploit Framework
- Elastic Stack + Kibana (ES|QL)
- John the Ripper
- Wireshark / tcpdump

## Structure
- `attack-simulations/` — MITRE ATT&CK technique walkthroughs
- `detections/sigma/` — SIGMA detection rules
- `playbooks/` — Incident Response playbooks
- `lab-setup/` — Lab architecture and configuration
- `tools/` — Tools, frameworks and scripts reference

## Techniques Covered

| ID | Name | Status |
|---|---|---|
| T1046 | Network Service Discovery (Nmap Detection Gap) | Completed |
| T1110.001 | SSH Brute Force | Completed |
| T1110.002 | Password Cracking + Credential Validation | Completed |
| T1190 | EternalBlue MS17-010 (Dionaea) | Completed |
| CVE-2011-2523 | vsftpd 2.3.4 Backdoor — Full Kill Chain | Completed |

## Incident Reports
| ID | Title | Techniques |
|---|---|---|
| IR-001 | Full Attack Chain: Recon → Exploit → Post-Exploitation | T1046, T1190, T1110.001, T1110.002, CVE-2011-2523 |
