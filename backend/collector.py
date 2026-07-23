from datetime import datetime
from opensearchpy import OpenSearch
from config import OPENSEARCH_HOST, OPENSEARCH_PORT, INDEX_NAME

client = OpenSearch(
    hosts=[{
        "host": OPENSEARCH_HOST,
        "port": OPENSEARCH_PORT
    }],
    use_ssl=False,
    verify_certs=False
)

if not client.indices.exists(index=INDEX_NAME):
    client.indices.create(index=INDEX_NAME)
    print(f"Index '{INDEX_NAME}' created.")
else:
    print(f"Index '{INDEX_NAME}' already exists.")

from datetime import datetime
import socket

log_file = "../logs/system.log"

with open(log_file, "r") as file:
    for line in file:
        line = line.strip()

        if not line:
            continue

        parts = line.split(" ", 1)

        severity = parts[0]
        event = parts[1] if len(parts) > 1 else ""

        log = {
            "timestamp": datetime.now().isoformat(),
            "host": socket.gethostname(),
            "severity": severity,
            "event": event
        }

        response = client.index(
            index=INDEX_NAME,
            body=log
        )

        print(f"Inserted: {event}")

print("Log inserted successfully!")
print(response)
