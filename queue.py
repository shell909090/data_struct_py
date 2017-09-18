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


class Queue(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head is None

    def __len__(self):
        if self.head is None:
            return 0
        cur, count = self.head, 1
        while cur != self.tail:
            count += 1
            cur = cur[1]
        return count

    def push(self, o):
        n = [o, None]
        if self.head is None:
            self.head = n
        else:
            self.tail[1] = n
        self.tail = n

    def pop(self):
        if self.head is None:
            raise Exception('empty queue')
        if self.tail is self.head:
            self.tail = None
        o, self.head = self.head
        return o


class QueueTest(unittest.TestCase):

    def test_queue(self):
        q = Queue()
        q.push(1)
        q.push(2)
        self.assertEqual(len(q), 2)
        self.assertEqual(q.pop(), 1)
        self.assertEqual(len(q), 1)
        q.push(3)
        self.assertEqual(q.pop(), 2)
        self.assertEqual(q.pop(), 3)

    def test_empty(self):
        q = Queue()
        self.assertEqual(q.empty(), True)
        with self.assertRaises(Exception):
            q.pop()
