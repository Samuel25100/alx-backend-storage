#!/usr/bin/env python3
"""Class: Cache"""
import redis
import uuid
from functools import wraps
from typing import Union, Callable, Optional


def call_history(method: Callable) -> Callable:
    """store the history of inputs and outputs for a particular function"""
    inky: str = method.__qualname__ + ":inputs"
    outky: str = method.__qualname__ + ":outputs"

    @wraps(method)
    def warpper(self, *args, **kwargs):
        """wrapper for decorator"""
        self._redis.rpush(inky, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outky, str(result))
        return result
    return warpper


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

    @call_history
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

    def replay(self, method: Callable) -> None:
        """display the history of calls of a particular function"""
        inky: str = method.__qualname__ + ":inputs"
        outky: str = method.__qualname__ + ":outputs"
        inputs = self._redis.lrange(inky, 0, -1)
        outputs = self._redis.lrange(outky, 0, -1)
        count: int = int(self._redis.llen(inky))
        print(f"Cache.store was called {count} times:")
        for inp, out in zip(inputs, outputs):
            print(f"Cache.store(*{inp.decode()}) -> {out.decode()}")
