#!/usr/bin/env python3
'''0. Writing strings to Redis'''
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps

def count_calls(method: Callable) -> Callable:
    '''count_calls decorator'''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''wrapper method'''
        self._redis.incr(method.__qualname__, 1)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    '''Cache class'''
    def __init__(self):
        '''Constructor method'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, int, float, bytes]) -> str:
        '''store data in redis and return the key'''
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    
    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, int, float, bytes, None]:
        '''get data from redis and return it'''
        data = self._redis.get(key)
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, data: bytes) -> str:
        '''convert bytes to str'''
        return data.decode('utf-8')
    
    def get_int(self, data: bytes) -> int:
        '''convert bytes to int'''
        return int(data)
