#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2017-09-18
@author: Shell.Xu
@copyright: 2017, Shell.Xu <shell909090@gmail.com>
@license: BSD-3-clause
'''
from __future__ import absolute_import, division,\
    print_function, unicode_literals
import unittest


class HashTable(object):

    def __init__(self, init_size=8, hashfunc=None):
        self.esize = 0  # element size
        self.bsize = init_size
        self.buckets = [None, ]*self.bsize
        self.hashfunc = hashfunc if hashfunc else hash

    def empty(self):
        return self.esize == 0

    def __len__(self):
        return self.esize

    def __setitem__(self, k, v):
        if (float(self.esize) / self.bsize) > 1.5:
            self.grow()
        h = self.hashfunc(k) % self.bsize
        if self.buckets[h] is None:
            self.buckets[h] = []
        for pair in self.buckets[h]:
            if pair[0] == k:
                pair[1] = v
                return
        self.buckets[h].append([k, v])
        self.esize += 1

    def grow(self):
        bsize = 2*self.bsize
        buckets = [None, ]*bsize
        for i in range(bsize):
            buckets[i] = [p for p in self.buckets[int(i % self.bsize)]
                          if self.hashfunc(p[0]) % bsize == i]
        self.bsize, self.buckets = bsize, buckets

    def __getitem__(self, k):
        h = self.hashfunc(k) % self.bsize
        if self.buckets[h] is None:
            raise KeyError()
        for pair in self.buckets[h]:
            if pair[0] == k:
                return pair[1]
        raise KeyError()

    def __delitem__(self, k):
        if (float(self.esize) / self.bsize) < 0.25:
            self.shrink()
        h = self.hashfunc(k) % self.bsize
        if self.buckets[h] is None:
            raise KeyError()
        for i, pair in enumerate(self.buckets[h]):
            if pair[0] == k:
                del self.buckets[h][i]
                self.esize -= 1
                return
        raise KeyError()

    def shrink(self):
        bsize = int(self.bsize/2)
        buckets = [None, ]*bsize
        for i in range(self.bsize):
            if not self.buckets[i]:
                continue
            u = int(i % bsize)
            if not buckets[u]:
                buckets[u] = []
            buckets[u].extend(self.buckets[i])
        self.bsize, self.buckets = bsize, buckets

    def keys(self):
        for b in self.buckets:
            if b is None:
                continue
            for pair in b:
                yield pair[0]

    def values(self):
        for b in self.buckets:
            if b is None:
                continue
            for pair in b:
                yield pair[1]

    def items(self):
        for b in self.buckets:
            if b is None:
                continue
            for pair in b:
                yield tuple(pair)


class HashTableTest(unittest.TestCase):

    def test_htab(self):
        h = HashTable()
        self.assertEqual(h.empty(), True)
        self.assertEqual(len(h), 0)

        for i in range(24):
            h[i] = str(i)
        self.assertEqual(h.empty(), False)
        self.assertEqual(len(h), 24)
        self.assertEqual(h[0], '0')
        self.assertEqual(h[23], '23')
        with self.assertRaises(KeyError):
            h[24]

        for i in range(20):
            del h[i]
        self.assertEqual(len(h), 4)
        with self.assertRaises(KeyError):
            h[0]
