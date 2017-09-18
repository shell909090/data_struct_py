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


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur[0]
            cur = cur[1]

    def empty(self):
        return self.head is None

    def rpush(self, o):
        n = [o, None]
        if self.tail is None:
            self.head = n
        else:
            self.tail[1] = n
        self.tail = n

    def rpop(self):
        if self.tail is None:
            raise Exception('empty list')
        if self.head is self.tail:
            o = self.head[0]
            self.head, self.tail = None, None
            return o
        o = self.tail[0]
        cur = self.head
        while cur:
            if self.tail is cur[1]:
                break
            cur = cur[1]
        self.tail = cur
        self.tail[1] = None
        return o

    def lpush(self, o):
        self.head = [o, self.head]
        if self.tail is None:
            self.tail = self.head

    def lpop(self):
        if self.head is None:
            raise Exception('empty list')
        if self.head is self.tail:
            self.tail = None
        o, self.head = self.head
        return o


class LinkedListTest(unittest.TestCase):

    def test_list(self):
        l = LinkedList()
        l.lpush(1)
        self.assertEqual(l.rpop(), 1)
        l.rpush(2)
        self.assertEqual(l.lpop(), 2)
        l.rpush(3)
        self.assertEqual(l.rpop(), 3)
        l.lpush(4)
        l.rpush(5)
        l.lpush(6)
        self.assertEqual(list(l), [6, 4, 5])
        self.assertEqual(l.lpop(), 6)
        self.assertEqual(l.lpop(), 4)
        self.assertEqual(l.lpop(), 5)

    def test_empty(self):
        l = LinkedList()
        self.assertEqual(l.empty(), True)
        with self.assertRaises(Exception):
            l.lpop()
        with self.assertRaises(Exception):
            l.rpop()
