#!/usr/bin/env python3
"""Class: Cache"""
import redis
import uuid
from functools import wraps
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """method to count number Cache class methods call"""
    k: str = method.__qualname__

    @wraps(method)
    def warpper(self, *args, **kwargs):
        """wrapper for decorator"""
        self._redis.incr(k)
        result = method(self, *args, **kwargs)
        return result
    return warpper


class Cache:
    """class that use redis to store variable"""

    def __init__(self):
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """create key and store data in database by key"""
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[str], str]] = None) -> str:
        """getter for key and decode data using fn"""
        val = self._redis.get(key)
        if (fn):
            return fn(val)
        return val

    def get_str(self, key: str) -> Union[str, None]:
        """getter for data in str type"""
        if (key):
            val = self._redis.get(key, str)
            return val
        return None

    def get_int(self, key: str) -> Union[str, None]:
        """getter for data in int type"""
        if (key):
            val = self._redis.get(key, int)
            return val
        return None
