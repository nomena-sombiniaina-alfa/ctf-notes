**Splunk – Log Exploration (Condensed Notes)**

**Index Loading**

* `index=main` (All time).
* Two sourcetypes: **web_traffic**, **firewall_logs** (server IP: 10.10.1.15).

**Initial Triage**

* `index=main sourcetype=web_traffic`
* Check timeline → spike = attack window.
* Key fields: **user_agent**, **client_ip**, **path**, **status**.

**Daily Volume Check**

* `index=main sourcetype=web_traffic | timechart span=1d count`
* `... | sort by count | reverse`
  → Identify abnormal high‑volume day.

**Anomaly Detection**

* Inspect **user_agent**, **client_ip**, **path**.
  → Suspicious UAs, one dominant attacker IP.

**Filter Out Legit Traffic**

```
index=main sourcetype=web_traffic \
user_agent!=*Mozilla* user_agent!=*Chrome* \
user_agent!=*Safari* user_agent!=*Firefox*
```

→ All suspicious traffic from one IP (<REDACTED>).

**Top Malicious IPs**

```
sourcetype=web_traffic user_agent!=*Mozilla* ... \
| stats count by client_ip | sort -count | head 5
```

---

### Attack Chain

**1. Recon**

```
sourcetype=web_traffic client_ip="<REDACTED>" \
AND path IN ("/.env","/*phpinfo*","/.git*") \
| table _time path user_agent status
```

→ Curl/wget probing.

**2. Enumeration (Path Traversal / Redirect)**

```
sourcetype=web_traffic client_ip="<REDACTED>" \
AND path="*..\/..\/*" OR path="*redirect*" \
| stats count by path
```

→ Attempts to read system files.

**3. SQL Injection**

```
sourcetype=web_traffic client_ip="<REDACTED>" \
AND user_agent IN ("*sqlmap*","*Havij*") \
| table _time path status
```

→ SQLmap, time‑based payloads (SLEEP).

**4. Exfiltration Attempts**

```
sourcetype=web_traffic client_ip="<REDACTED>" \
AND path IN ("*backup.zip*","*logs.tar.gz*") \
| table _time path user_agent
```

→ Backup/log downloads.

**5. Ransomware + Webshell (RCE)**

```
sourcetype=web_traffic client_ip="<REDACTED>" \
AND path IN ("*bunnylock.bin*","*shell.php?cmd=*") \
| table _time path user_agent status
```

→ Shell execution + ransomware loader.

---

### C2 Correlation (Firewall Logs)

```
sourcetype=firewall_logs \
src_ip="10.10.1.5" dest_ip="<REDACTED>" action="ALLOWED" \
| table _time action protocol src_ip dest_ip dest_port reason
```

→ Outbound C2 confirmed.

**Exfiltration Volume**

```
sourcetype=firewall_logs \
src_ip="10.10.1.5" dest_ip="<REDACTED>" action="ALLOWED" \
| stats sum(bytes_transferred) by src_ip
```

---

### Summary

* **Attacker Identity**: IP with highest malicious events.
* **Attack Flow**: Recon → traversal → SQLi → webshell → ransomware → C2.
* **RCE Evidence**: `shell.php?cmd=./bunnylock.bin`.
* **C2 Verified**: Firewall logs show allowed outbound traffic to attacker.





2025-10-12	2267

Havij/1.17 (Automated SQL Injection)	993	5,783 %

client IP : 198.51.100.55


/download?file=../../etc/passwd	658	3,832 %

sourcetype=web_traffic client_ip="198.51.100.55" AND path IN ("/.env", "/*phpinfo*", "/.git*") | table _time, path, user_agent, 

sourcetype=firewall_logs src_ip="10.10.1.5" AND dest_ip="198.51.100.55" AND action="ALLOWED" | stats sum(bytes_transferred) by src_ip