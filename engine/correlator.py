from collections import defaultdict
from rules.mitre_mapping import MITRE_TECHNIQUES

def correlate_events(events):
    failed_logins = defaultdict(int)
    alerts = []

    for event in events:
        if event["event_type"] == "login_failure":
            key = (event["username"], event["source_ip"])
            failed_logins[key] += 1

        if event["event_type"] == "login_success":
            key = (event["username"], event["source_ip"])

            if failed_logins[key] >= 3:
                alerts.append({
                    "alert": "Brute Force Followed By Success",
                    "user": event["username"],
                    "ip": event["source_ip"],
                    "mitre": [
                        MITRE_TECHNIQUES["brute_force"],
                        MITRE_TECHNIQUES["valid_accounts"]
                    ],
                    "severity": "HIGH"
                })

    return alerts
