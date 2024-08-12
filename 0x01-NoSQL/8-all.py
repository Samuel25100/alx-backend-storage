#!/usr/bin/env python3
"""function: list_all"""
from pymongo import MongoClient
import json


def list_all(mongo_collection):
    """lists all documents in a collection"""
    result = mongo_collection.find({})
    return list(result)
