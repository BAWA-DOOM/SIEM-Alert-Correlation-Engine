# SIEM Alert Correlation Engine (MITRE ATT&CK Based)

## Overview
This project simulates how modern SOC teams **correlate security events** to detect real attacks instead of generating noisy alerts.

It focuses on behavioral detection rather than single-event alerting.

---

## Problem Statement
Security teams often suffer from alert fatigue due to:
- Isolated alerts
- Lack of context
- No correlation across events

Attackers exploit this gap to remain undetected.

---

## What This Project Does
- Ingests authentication-related security logs
- Correlates failed and successful login attempts
- Detects brute-force attacks followed by account compromise
- Maps detections to MITRE ATT&CK techniques

---

## Detection Logic
- Multiple failed logins from same source
- Followed by a successful login
- Indicates credential compromise

---

## MITRE ATT&CK Mapping
- **T1110** – Brute Force
- **T1078** – Valid Accounts

---

## Tech Stack
- Python
- Log correlation logic
- MITRE ATT&CK framework

---

## Why This Matters
Real SOC environments focus on:
- Signal over noise
- Behavior over events
- Contextual detection

This project mirrors real detection engineering workflows.

---

## Disclaimer
This project is for educational and defensive security research only.
