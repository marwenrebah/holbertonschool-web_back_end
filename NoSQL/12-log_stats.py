#!/usr/bin/env python3
""" Python function that provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


def get_nginx_stats(db):
    """Function that provides some stats about Nginx logs stored in MongoDB"""
    collection = db["nginx"]
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    """ Print methods stats """
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    """ Print specific query """
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")


if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/")
    db = client["logs"]
