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


class CircularQueue(object):

    def __init__(self, n):
        self.size = n+1
        self.data = [0, ]*self.size
        self.head = 0
        self.tail = 0

    def empty(self):
        return self.head == self.tail

    def full(self):
        return ((self.tail+1) % self.size) == self.head

    def __len__(self):
        return (self.tail-self.head) % self.size

    def push(self, o):
        if self.full():
            raise Exception('queue full')
        self.data[self.tail] = o
        self.tail = (self.tail+1) % self.size

    def pop(self):
        if self.empty():
            raise Exception('empty queue')
        o = self.data[self.head]
        self.head = (self.head+1) % self.size
        return o

    def __iter__(self):
        i = self.head
        while i != self.tail:
            yield self.data[i]
            i = (i+1) % self.size


class CircularQueueTest(unittest.TestCase):

    def test_vcqueue(self):
        q = CircularQueue(2)
        q.push(1)
        q.push(2)
        self.assertEqual(len(q), 2)
        self.assertEqual(q.pop(), 1)
        self.assertEqual(len(q), 1)
        q.push(3)
        self.assertEqual(len(q), 2)
        self.assertEqual(list(q), [2, 3])
        self.assertEqual(q.pop(), 2)
        self.assertEqual(q.pop(), 3)

        self.assertEqual(len(q), 0)
        self.assertEqual(q.empty(), True)
        self.assertEqual(q.full(), False)
        with self.assertRaises(Exception):
            q.pop()
        q.push(4)
        q.push(5)
        self.assertEqual(q.empty(), False)
        self.assertEqual(q.full(), True)
        with self.assertRaises(Exception):
            q.push(6)
