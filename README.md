\# SIEM Alert Correlation Engine (MITRE ATT\&CK Based)



\## Problem

Security teams face alert fatigue due to uncorrelated security events.



\## Solution

This project correlates authentication events to detect real attacks and maps them to MITRE ATT\&CK techniques.



\## Detection Logic

\- Multiple failed logins

\- Followed by successful authentication

\- From same IP and user



\## MITRE Mapping

\- T1110: Brute Force

\- T1078: Valid Accounts



\## Tech Stack

\- Python

\- MITRE ATT\&CK

\- Log Correlation



\## Outcome

Reduced false positives and highlighted real attack patterns.



