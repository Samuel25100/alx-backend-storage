#!/usr/bin/env python3
"""Class: Cache"""
import redis
import uuid
from typing import Union


class Cache:
    """class that use redis to store variable"""

    def __init__(self):
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self.__redis.set(key, data)
        return key

    def get(self, key, fn):
        if (key):
            val = self.__redis.get(key)
            if (fn == None):
                return val
            elif (fn == int):
                return int(val)
            else:
                return fn(val)
        return None
