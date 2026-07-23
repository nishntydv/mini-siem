from opensearchpy import OpenSearch
from datetime import datetime

client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    http_compress=True,
    use_ssl=False,
    verify_certs=False,
)

LOG_INDEX = "mini-siem-logs"
ALERT_INDEX = "mini-siem-alerts"

rules = [
    {"keyword": "Unauthorized", "priority": "HIGH"},
    {"keyword": "failed login", "priority": "MEDIUM"},
    {"keyword": "Firewall blocked", "priority": "MEDIUM"},
    {"keyword": "USB device", "priority": "LOW"},
    {"keyword": "Malware", "priority": "CRITICAL"},
]

response = client.search(
    index=LOG_INDEX,
    body={
        "query": {"match_all": {}},
        "size": 100
    }
)

logs = response["hits"]["hits"]

print("\n========== Mini SIEM Alert Engine ==========\n")

alert_count = 0

for log in logs:

    source = log["_source"]

    event = source["event"]
    severity = source["severity"]
    host = source["host"]

    for rule in rules:

        if rule["keyword"].lower() in event.lower():

            alert = {
                "timestamp": datetime.now().isoformat(),
                "host": host,
                "priority": rule["priority"],
                "severity": severity,
                "event": event
            }

            client.index(
                index=ALERT_INDEX,
                body=alert
            )

            alert_count += 1

            print("=" * 60)
            print(f"Priority : {rule['priority']}")
            print(f"Host     : {host}")
            print(f"Severity : {severity}")
            print(f"Event    : {event}")
            print("=" * 60)

print(f"\nTotal Alerts Stored : {alert_count}")
