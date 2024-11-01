#!/usr/bin/python3
""" Lifocache class that inherits from BaseCaching
"""
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        if key or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.order.pop()
            del self.cache_data[last_key]
            print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        return self.cache_data.get(key, None)
