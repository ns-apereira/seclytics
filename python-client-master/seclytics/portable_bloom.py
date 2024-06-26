import sys
import os
from bloom_filter import BloomFilter


class PortableBloom(object):
    """Wraps bloom filter module"""
    bloom = None

    def __init__(self, path):
        if not os.path.exists(path):
            raise RuntimeError("Missing Bloom: %s" % path)
        self.bloom = BloomFilter.open(path)

    def contains(self, value):
        if sys.version_info < (3, 0) and not isinstance(value, str):
            value = value.encode('ascii')
        return value in self.bloom
