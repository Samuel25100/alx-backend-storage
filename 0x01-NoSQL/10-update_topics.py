#!/usr/bin/env python3
"""function: update_topics"""


def update_topics(mongo_collection, name, topics):
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
