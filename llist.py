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

    def lpush(self, o):
        if self.tail is None:
            self.tail = [None, o]
            self.head = self.tail
        else:
            self.tail[0] = [None, o]
            self.tail = self.tail[0]

    def lpop(self):
        if self.tail is None:
            raise Exception('empty list')
        if self.head is self.tail:
            o = self.head[1]
            self.head, self.tail = None, None
            return o
        prev = self.head
        while prev:
            if self.tail is prev[0]:
                break
            prev, _ = prev
        if prev is None:
            raise Exception('wtf')
        o = self.tail[1]
        prev[0] = None
        self.tail = prev
        return o

    def rpush(self, o):
        self.head = [self.head, o]
        if self.tail is None:
            self.tail = self.head

    def rpop(self):
        if self.head is None:
            raise Exception('empty list')
        if self.head is self.tail:
            self.tail = None
        self.head, o = self.head
        return o

    def empty(self):
        return self.head is None


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
        self.assertEqual(l.lpop(), 4)
        self.assertEqual(l.lpop(), 5)

    def test_empty(self):
        l = LinkedList()
        self.assertEqual(l.empty(), True)
        with self.assertRaises(Exception):
            l.lpop()
        with self.assertRaises(Exception):
            l.rpop()
