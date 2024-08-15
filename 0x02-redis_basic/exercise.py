#!/usr/bin/env python3
"""Class: Cache"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """class that use redis to store variable"""

    def __init__(self):
        """Constructor"""
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """create key and store data in database by key"""
        key: str = str(uuid.uuid4())
        self.__redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[str], str]]) -> str:
        """getter for key and decode data using fn"""
        val = self.__redis.get(key)
        if (fn):
            return fn(val)
        return val

    def get_str(self, key: str) -> Union[str, None]:
        """getter for data in str type"""
        if (key):
            val = self.__redis.get(key, str)
            return val
        return None

    def get_int(self, key: str) -> Union[str, None]:
        """getter for data in int type"""
        if (key):
            val = self.__redis.get(key, int)
            return val
        return None
