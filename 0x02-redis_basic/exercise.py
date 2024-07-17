#!/usr/bin/env python3
'''0. Writing strings to Redis'''
import redis
import uuid
from typing import Union


class Cache:
    '''Cache class'''
    def __init__(self):
        '''Constructor method'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, float, bytes]) -> str:
        '''store data in redis and return the key'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
