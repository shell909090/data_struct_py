#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2017-09-15
@author: Shell.Xu
@copyright: 2017, Shell.Xu <shell909090@gmail.com>
@license: BSD-3-clause
'''
from __future__ import absolute_import, division,\
    print_function, unicode_literals
import random
import unittest


class BinaryHeap(object):

    def __init__(self, n, key=None, cmpr=None):
        self.size = n
        self.data = [None, ]*self.size
        self.top = 0
        # max in the root
        self.cmpr = cmpr if cmpr else lambda x, y: x >= y

    def empty(self):
        return self.top == 0

    def full(self):
        return self.top == self.size

    def push(self, o):
        if self.top == self.size:
            raise Exception('heap full')
        i, u = self.top, int((self.top-1)/2)
        while i and not self.cmpr(self.data[u], o):
            self.data[i] = self.data[u]
            i, u = u, int((u-1)/2)
        self.data[i] = o
        self.top += 1

    def pop(self):
        if self.top == 0:
            raise Exception('heap empty')
        o, f, i, d = self.data[0], self.data[self.top-1], 0, 1
        while d < self.top:
            if (d+1) < self.top\
               and not self.cmpr(self.data[d], self.data[d+1]):
                d = d+1
            if not self.cmpr(self.data[d], f):
                break
            self.data[i] = self.data[d]
            i, d = d, 2*i+1
        self.data[i] = f
        self.top -= 1
        return o


class BinaryHeapTest(unittest.TestCase):

    def test_heap(self):
        h = BinaryHeap(10)
        self.assertEqual(h.empty(), True)
        self.assertEqual(h.full(), False)
        with self.assertRaises(Exception):
            h.pop()

        s = range(10)
        random.shuffle(s)
        for i in s:
            h.push(i)

        self.assertEqual(h.empty(), False)
        self.assertEqual(h.full(), True)
        with self.assertRaises(Exception):
            h.push(11)

        it = iter(sorted(s, reverse=True))
        while not h.empty():
            self.assertEqual(h.pop(), next(it))
