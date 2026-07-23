from opensearchpy import OpenSearch

client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    http_compress=True,
    use_ssl=False,
    verify_certs=False,
)

INDEX = "mini-siem-alerts"

print("\n===== Mini SIEM Log Search =====")

print("\nSearch Options:")
print("1. Search by Severity")
print("2. Search by Host")
print("3. Search by Event")

choice = input("\nEnter your choice (1-3): ")

if choice == "1":
    value = input("Enter Severity (INFO/WARNING/ERROR): ")

    query = {
        "query": {
            "match": {
                "severity": value
            }
        }
    }

elif choice == "2":
    value = input("Enter Host: ")

    query = {
        "query": {
            "match": {
                "host": value
            }
        }
    }

elif choice == "3":
    value = input("Enter Event Keyword: ")

    query = {
        "query": {
            "match": {
                "event": value
            }
        }
    }

else:
    print("Invalid Choice")
    exit()

response = client.search(
    index=INDEX,
    body=query
)

hits = response["hits"]["hits"]

print("\n========== SEARCH RESULTS ==========\n")

if len(hits) == 0:
    print("No matching logs found.")

for log in hits:

    source = log["_source"]

    print(f"Time      : {source['timestamp']}")
    print(f"Host      : {source['host']}")
    print(f"Severity  : {source['severity']}")
    print(f"Event     : {source['event']}")
    print("-" * 50)
