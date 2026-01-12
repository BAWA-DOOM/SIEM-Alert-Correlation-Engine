import json
from engine.correlator import correlate_events

with open("logs/sample_logs.json") as f:
    events = json.load(f)

alerts = correlate_events(events)

print("\n[+] Correlated Alerts:\n")
for alert in alerts:
    print(alert)
