#!/usr/bin/python3
""" Basecaching module
"""

class BaseCaching():
    """ Basecaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """ 
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize
        """
        self.cache_data = {}

    def print_cache(self):
        """ print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.key()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item key
        """
        raise NotImplementedError("get must be implemeted in your cache class")
