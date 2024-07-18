#!/usr/bin/env python3
'''5. Implementing an expiring web cache and tracker'''
import redis
import requests
from typing import Callable
from functools import wraps


def web_cache(fn: Callable) -> Callable:
    '''web_cache decorator'''
    @wraps(fn)
    def wrapper(self, url: str) -> str:
        '''wrapper method'''
        key = "cached:{}".format(url)
        result = self._redis.get(key)
        if result is None:
            result = fn(self, url)
            self._redis.setex(key, 10, result)
        return result
    return wrapper


def count_calls(fn: Callable) -> Callable:
    '''count_calls decorator'''
    @wraps(fn)
    def wrapper(self, url: str) -> str:
        '''wrapper method'''
        key = "count:{}".format(url)
        self._redis.incr(key, 1)
        return fn(self, url)
    return wrapper


@web_cache
@count_calls
def get_page(url: str) -> str:
    '''return HTML webpage'''
    r = requests.get(url)
    return r.content.decode('utf-8')
