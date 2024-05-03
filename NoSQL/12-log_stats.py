#!/usr/bin/env python3
""" Python script that provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client["logs"]

    logs = db["nginx"]
    total_logs = logs.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = logs.count_documents({"method": method})
        print(f"\t{count} {method.upper()}")

    get_status_count = logs.count_documents({"method": "GET", "path": "/status"})
    print(f"{get_status_count} GET /status")
