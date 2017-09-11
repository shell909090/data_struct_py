#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2017-09-11
@author: Shell.Xu
@copyright: 2017, Shell.Xu <shell909090@gmail.com>
@license: BSD-3-clause
'''
from __future__ import absolute_import, division,\
    print_function, unicode_literals
import unittest


class VectorCircularQueue(object):

    def __init__(self, n):
        self.size = n+1
        self.data = [0, ]*self.size
        self.head = n
        self.tail = 0

    def push(self, o):
        if self.tail == self.head:
            raise Exception('queue full')
        self.data[self.tail] = o
        self.tail = (self.tail+1) % self.size

    def pop(self):
        if self.empty():
            raise Exception('empty queue')
        self.head = (self.head+1) % self.size
        o = self.data[self.head]
        return o

    def empty(self):
        return ((self.head+1) % self.size) == self.tail


class VectorCircularQueueTest(unittest.TestCase):

    def test_vcqueue(self):
        q = VectorCircularQueue(2)
        q.push(1)
        q.push(2)
        self.assertEqual(q.pop(), 1)
        q.push(3)
        self.assertEqual(q.pop(), 2)
        self.assertEqual(q.pop(), 3)

        self.assertEqual(q.empty(), True)
        with self.assertRaises(Exception):
            q.pop()
        q.push(4)
        q.push(5)
        with self.assertRaises(Exception):
            q.push(6)
