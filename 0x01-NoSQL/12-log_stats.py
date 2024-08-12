#!/usr/bin/env python3
"""provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def log_stat():
    """provides some stats about Nginx logs stored in MongoDB Database: logs"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginxcol = client.logs.nginx
    count = nginxcol.count_documents({})
    ar = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print(count, "logs")
    print("Methods:")
    for i in ar:
        result = nginxcol.count_documents({'method': i})
        print(f"\tmethod {i}: ", result)
    stat = nginxcol.count_documents({'method': 'GET', 'path': '/status'})
    print(stat, "status check")


if __name__ == '__main__':
    log_stat()