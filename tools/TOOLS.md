# Tools & Frameworks Reference

Quick reference — click a technique to see how each tool was used in context.

---

## Nmap
**Purpose:** Network reconnaissance, service version detection  
**Used in:**
- [T1046 — Nmap Detection Gap Analysis](../attack-simulations/T1046-nmap-network-scan/writeup.md)
- [CVE-2011-2523 — Phase 1 Recon](../attack-simulations/CVE-2011-2523-vsftpd-backdoor/writeup.md)
- [IR-001 — Full Attack Chain](../playbooks/incident-reports/IR-001-full-attack-chain.md)

---

## Hydra
**Purpose:** SSH brute force, credential testing  
**Used in:**
- [T1110.001 — SSH Brute Force](../attack-simulations/T1110.001-ssh-brute-force/writeup.md)
- [IR-001 — Full Attack Chain](../playbooks/incident-reports/IR-001-full-attack-chain.md)

---

## Metasploit Framework
**Purpose:** Exploit execution, post-exploitation, Meterpreter sessions  
**Used in:**
- [T1190 — EternalBlue MS17-010](../attack-simulations/T1190-eternalblue-ms17-010/writeup.md)
- [CVE-2011-2523 — vsftpd Backdoor](../attack-simulations/CVE-2011-2523-vsftpd-backdoor/writeup.md)
- [IR-001 — Full Attack Chain](../playbooks/incident-reports/IR-001-full-attack-chain.md)

---

## John the Ripper
**Purpose:** Password hash cracking (MD5crypt), rule-based attacks  
**Used in:**
- [T1110.002 — Password Cracking](../attack-simulations/T1110.002-password-cracking/writeup.md)
- [IR-001 — Full Attack Chain](../playbooks/incident-reports/IR-001-full-attack-chain.md)

---

## Wireshark / tcpdump
**Purpose:** Packet capture, network forensics, protocol analysis  
**Used in:**
- [CVE-2011-2523 — FTP Backdoor Trigger (pcap evidence)](../attack-simulations/CVE-2011-2523-vsftpd-backdoor/writeup.md)

---

## Suricata IDS
**Purpose:** Signature-based network detection, custom rule development  
**Used in:**
- [T1046 — Nmap Detection Gap](../attack-simulations/T1046-nmap-network-scan/writeup.md)
- [T1190 — EternalBlue Detection](../attack-simulations/T1190-eternalblue-ms17-010/writeup.md)
- [CVE-2011-2523 — Detection Gap Analysis](../attack-simulations/CVE-2011-2523-vsftpd-backdoor/writeup.md)

---

## Elastic Stack + Kibana (ES|QL)
**Purpose:** Log ingestion, SIEM analysis, multi-source correlation  
**Used in:**
- [T1110.001 — SSH Brute Force](../attack-simulations/T1110.001-ssh-brute-force/writeup.md)
- [T1046 — Nmap Detection Gap](../attack-simulations/T1046-nmap-network-scan/writeup.md)
- [T1190 — EternalBlue](../attack-simulations/T1190-eternalblue-ms17-010/writeup.md)
- [IR-001 — Multi-source Timeline Correlation](../playbooks/incident-reports/IR-001-full-attack-chain.md)

---

## T-Pot Honeypot Platform
**Components:** Cowrie, Suricata, Dionaea, Honeytrap, Wordpot  
**Purpose:** Passive threat intelligence, attack simulation target  
**Used in:**
- All attack simulations involving T-Pot infrastructure

---

## SecLists
**Purpose:** Wordlist source for credential attacks  
**Used in:**
- [T1110.001 — Default Credentials wordlist](../attack-simulations/T1110.001-ssh-brute-force/writeup.md)
- [T1110.002 — Combolist construction](../attack-simulations/T1110.002-password-cracking/writeup.md)
