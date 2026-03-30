# Suricata Alert Report

**Generated:** 2026-03-30 10:34:41  
**Source:** `/var/log/suricata/eve.json`  
**Total alerts:** 69  
**Unique signatures:** 14  

---

## Summary

| Signature | Count |
|-----------|-------|
| ET SCAN Possible Nmap User-Agent Observed | 24 |
| ET INFO Possible Kali Linux hostname in DHCP Request Packet | 22 |
| SURICATA Applayer Detect protocol only one direction | 4 |
| SURICATA STREAM ESTABLISHED invalid ack | 3 |
| SURICATA STREAM Packet with invalid ack | 3 |
| SURICATA STREAM ESTABLISHED packet out of window | 3 |
| GPL ATTACK_RESPONSE id check returned root | 2 |
| ET INFO GNU/Linux APT User-Agent Outbound likely related to package management | 2 |
| ET EXPLOIT Possible ETERNALBLUE Probe MS17-010 (MSF style) | 1 |
| ET EXPLOIT Possible ETERNALBLUE Probe MS17-010 (Generic Flags) | 1 |
| SURICATA STREAM FIN out of window | 1 |
| SURICATA STREAM FIN invalid ack | 1 |
| ET INFO [eSentire] Possible Kali Linux Updates | 1 |
| SURICATA HTTP Response excessive header repetition | 1 |

---

## Alerts by Signature

### ET SCAN Possible Nmap User-Agent Observed
- **SID:** 2024364
- **Category:** Web Application Attack
- **Severity:** 1
- **Hit count:** 24

| Timestamp | Source | Destination | Proto | Severity |
|-----------|--------|-------------|-------|----------|
| 2026-03-27 14:42:22 | 192.168.232.128:43796 | 192.168.232.129:80 | TCP | 1 |
| 2026-03-27 14:42:22 | 192.168.232.128:43804 | 192.168.232.129:80 | TCP | 1 |
| 2026-03-27 14:42:22 | 192.168.232.128:58578 | 192.168.232.129:8180 | TCP | 1 |
| 2026-03-27 14:42:22 | 192.168.232.128:58558 | 192.168.232.129:8180 | TCP | 1 |
| 2026-03-27 14:42:22 | 192.168.232.128:43812 | 192.168.232.129:80 | TCP | 1 |
| 2026-03-27 14:42:22 | 192.168.232.128:58592 | 192.168.232.129:8180 | TCP | 1 |
| 2026-03-27 14:42:22 | 192.168.232.128:43826 | 192.168.232.129:80 | TCP | 1 |
| 2026-03-27 14:42:22 | 192.168.232.128:58604 | 192.168.232.129:8180 | TCP | 1 |
| 2026-03-27 15:25:48 | 192.168.232.128:37284 | 192.168.232.129:80 | TCP | 1 |
| 2026-03-27 15:25:48 | 192.168.232.128:36210 | 192.168.232.129:8180 | TCP | 1 |
| 2026-03-27 15:25:48 | 192.168.232.128:36224 | 192.168.232.129:8180 | TCP | 1 |
| 2026-03-27 15:25:48 | 192.168.232.128:37278 | 192.168.232.129:80 | TCP | 1 |
| 2026-03-27 15:25:48 | 192.168.232.128:36246 | 192.168.232.129:8180 | TCP | 1 |
| 2026-03-27 15:25:48 | 192.168.232.128:37292 | 192.168.232.129:80 | TCP | 1 |
| 2026-03-27 15:25:48 | 192.168.232.128:36248 | 192.168.232.129:8180 | TCP | 1 |
| 2026-03-27 15:25:48 | 192.168.232.128:37298 | 192.168.232.129:80 | TCP | 1 |
| 2026-03-27 15:41:30 | 192.168.232.128:53704 | 192.168.232.129:80 | TCP | 1 |
| 2026-03-27 15:41:30 | 192.168.232.128:53030 | 192.168.232.129:8180 | TCP | 1 |
| 2026-03-27 15:41:30 | 192.168.232.128:53712 | 192.168.232.129:80 | TCP | 1 |
| 2026-03-27 15:41:30 | 192.168.232.128:53038 | 192.168.232.129:8180 | TCP | 1 |

> _4 additional events truncated._

### ET INFO Possible Kali Linux hostname in DHCP Request Packet
- **SID:** 2022973
- **Category:** Potential Corporate Privacy Violation
- **Severity:** 1
- **Hit count:** 22

| Timestamp | Source | Destination | Proto | Severity |
|-----------|--------|-------------|-------|----------|
| 2026-03-27 14:47:25 | 192.168.232.128:68 | 192.168.232.254:67 | UDP | 1 |
| 2026-03-27 15:02:25 | 192.168.232.128:68 | 192.168.232.254:67 | UDP | 1 |
| 2026-03-27 15:17:25 | 192.168.232.128:68 | 192.168.232.254:67 | UDP | 1 |
| 2026-03-27 15:32:25 | 192.168.232.128:68 | 192.168.232.254:67 | UDP | 1 |
| 2026-03-27 15:47:25 | 192.168.232.128:68 | 192.168.232.254:67 | UDP | 1 |
| 2026-03-28 13:10:17 | 0.0.0.0:68 | 255.255.255.255:67 | UDP | 1 |
| 2026-03-28 13:10:27 | 0.0.0.0:68 | 255.255.255.255:67 | UDP | 1 |
| 2026-03-28 13:10:37 | 0.0.0.0:68 | 255.255.255.255:67 | UDP | 1 |
| 2026-03-28 13:11:11 | 0.0.0.0:68 | 255.255.255.255:67 | UDP | 1 |
| 2026-03-28 13:26:11 | 192.168.232.128:68 | 192.168.232.254:67 | UDP | 1 |
| 2026-03-28 13:41:11 | 192.168.232.128:68 | 192.168.232.254:67 | UDP | 1 |
| 2026-03-29 08:14:27 | 192.168.232.128:68 | 192.168.232.254:67 | UDP | 1 |
| 2026-03-29 18:14:33 | 0.0.0.0:68 | 255.255.255.255:67 | UDP | 1 |
| 2026-03-30 08:20:30 | 192.168.232.128:68 | 192.168.232.254:67 | UDP | 1 |
| 2026-03-30 08:35:30 | 192.168.232.128:68 | 192.168.232.254:67 | UDP | 1 |
| 2026-03-30 08:50:30 | 192.168.232.128:68 | 192.168.232.254:67 | UDP | 1 |
| 2026-03-30 09:05:30 | 192.168.232.128:68 | 192.168.232.254:67 | UDP | 1 |
| 2026-03-30 09:20:30 | 192.168.232.128:68 | 192.168.232.254:67 | UDP | 1 |
| 2026-03-30 09:35:30 | 192.168.232.128:68 | 192.168.232.254:67 | UDP | 1 |
| 2026-03-30 09:50:30 | 192.168.232.128:68 | 192.168.232.254:67 | UDP | 1 |

> _2 additional events truncated._

### SURICATA Applayer Detect protocol only one direction
- **SID:** 2260002
- **Category:** Generic Protocol Command Decode
- **Severity:** 3
- **Hit count:** 4

| Timestamp | Source | Destination | Proto | Severity |
|-----------|--------|-------------|-------|----------|
| 2026-03-27 14:42:17 | 192.168.232.128:60056 | 192.168.232.129:5432 | TCP | 3 |
| 2026-03-27 14:42:17 | 192.168.232.129:513 | 192.168.232.128:37372 | TCP | 3 |
| 2026-03-27 15:25:43 | 192.168.232.128:49242 | 192.168.232.129:5432 | TCP | 3 |
| 2026-03-27 15:41:25 | 192.168.232.128:51520 | 192.168.232.129:5432 | TCP | 3 |

### SURICATA STREAM ESTABLISHED invalid ack
- **SID:** 2210029
- **Category:** Generic Protocol Command Decode
- **Severity:** 3
- **Hit count:** 3

| Timestamp | Source | Destination | Proto | Severity |
|-----------|--------|-------------|-------|----------|
| 2026-03-27 14:44:51 | 192.168.232.129:43549 | 192.168.232.128:8080 | TCP | 3 |
| 2026-03-27 14:44:51 | 192.168.232.129:43549 | 192.168.232.128:8080 | TCP | 3 |
| 2026-03-27 14:44:51 | 192.168.232.129:43549 | 192.168.232.128:8080 | TCP | 3 |

### SURICATA STREAM Packet with invalid ack
- **SID:** 2210045
- **Category:** Generic Protocol Command Decode
- **Severity:** 3
- **Hit count:** 3

| Timestamp | Source | Destination | Proto | Severity |
|-----------|--------|-------------|-------|----------|
| 2026-03-27 14:44:51 | 192.168.232.129:43549 | 192.168.232.128:8080 | TCP | 3 |
| 2026-03-27 14:44:51 | 192.168.232.129:43549 | 192.168.232.128:8080 | TCP | 3 |
| 2026-03-27 14:44:51 | 192.168.232.129:43549 | 192.168.232.128:8080 | TCP | 3 |

### SURICATA STREAM ESTABLISHED packet out of window
- **SID:** 2210020
- **Category:** Generic Protocol Command Decode
- **Severity:** 3
- **Hit count:** 3

| Timestamp | Source | Destination | Proto | Severity |
|-----------|--------|-------------|-------|----------|
| 2026-03-27 14:44:51 | 192.168.232.128:8080 | 192.168.232.129:43549 | TCP | 3 |
| 2026-03-27 14:44:51 | 192.168.232.128:8080 | 192.168.232.129:43549 | TCP | 3 |
| 2026-03-27 14:44:51 | 192.168.232.128:8080 | 192.168.232.129:43549 | TCP | 3 |

### GPL ATTACK_RESPONSE id check returned root
- **SID:** 2100498
- **Category:** Potentially Bad Traffic
- **Severity:** 2
- **Hit count:** 2

| Timestamp | Source | Destination | Proto | Severity |
|-----------|--------|-------------|-------|----------|
| 2026-03-27 14:44:51 | 192.168.232.129:6200 | 192.168.232.128:34951 | TCP | 2 |
| 2026-03-27 15:40:35 | 192.168.232.129:6200 | 192.168.232.128:34281 | TCP | 2 |

### ET INFO GNU/Linux APT User-Agent Outbound likely related to package management
- **SID:** 2013504
- **Category:** Not Suspicious Traffic
- **Severity:** 3
- **Hit count:** 2

| Timestamp | Source | Destination | Proto | Severity |
|-----------|--------|-------------|-------|----------|
| 2026-03-30 09:47:53 | 192.168.232.128:39654 | 54.39.128.230:80 | TCP | 3 |
| 2026-03-30 09:47:53 | 192.168.232.128:44670 | 104.17.253.239:80 | TCP | 3 |

### ET EXPLOIT Possible ETERNALBLUE Probe MS17-010 (MSF style)
- **SID:** 2025649
- **Category:** A Network Trojan was detected
- **Severity:** 1
- **Hit count:** 1

| Timestamp | Source | Destination | Proto | Severity |
|-----------|--------|-------------|-------|----------|
| 2026-03-27 14:43:42 | 192.168.232.128:37809 | 192.168.232.129:445 | TCP | 1 |

### ET EXPLOIT Possible ETERNALBLUE Probe MS17-010 (Generic Flags)
- **SID:** 2025992
- **Category:** A Network Trojan was detected
- **Severity:** 1
- **Hit count:** 1

| Timestamp | Source | Destination | Proto | Severity |
|-----------|--------|-------------|-------|----------|
| 2026-03-27 14:43:42 | 192.168.232.128:37809 | 192.168.232.129:445 | TCP | 1 |

### SURICATA STREAM FIN out of window
- **SID:** 2210038
- **Category:** Generic Protocol Command Decode
- **Severity:** 3
- **Hit count:** 1

| Timestamp | Source | Destination | Proto | Severity |
|-----------|--------|-------------|-------|----------|
| 2026-03-27 14:44:51 | 192.168.232.128:8080 | 192.168.232.129:43549 | TCP | 3 |

### SURICATA STREAM FIN invalid ack
- **SID:** 2210030
- **Category:** Generic Protocol Command Decode
- **Severity:** 3
- **Hit count:** 1

| Timestamp | Source | Destination | Proto | Severity |
|-----------|--------|-------------|-------|----------|
| 2026-03-27 14:44:51 | 192.168.232.129:43549 | 192.168.232.128:8080 | TCP | 3 |

### ET INFO [eSentire] Possible Kali Linux Updates
- **SID:** 2025627
- **Category:** Misc activity
- **Severity:** 3
- **Hit count:** 1

| Timestamp | Source | Destination | Proto | Severity |
|-----------|--------|-------------|-------|----------|
| 2026-03-30 09:47:53 | 192.168.232.128:39654 | 54.39.128.230:80 | TCP | 3 |

### SURICATA HTTP Response excessive header repetition
- **SID:** 2221036
- **Category:** Generic Protocol Command Decode
- **Severity:** 3
- **Hit count:** 1

| Timestamp | Source | Destination | Proto | Severity |
|-----------|--------|-------------|-------|----------|
| 2026-03-30 09:47:53 | 54.39.128.230:80 | 192.168.232.128:39654 | TCP | 3 |
