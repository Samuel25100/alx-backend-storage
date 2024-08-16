#!/usr/bin/env python3
"""function: get_page"""
import requests
from redis import Redis


def get_page(url: str) -> str:
    """Request HTML content of a particular URL and returns it"""
    count: int = 0
    re: str = requests.get(url)
    r = Redis()
    if (r.exists(f"count:{url}")):
        count = int(r.get(f"count:{url}")) + 1
    r.setex(f"result:{url}", 10, re)
    r.set(f"count:{url}", count)
    return re
