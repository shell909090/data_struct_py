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


class DoubleLinkedList(object):

    def __init__(self):
        pass


class LinkedListTest(unittest.TestCase):

    def test_list(self):
        l = DoubleLinkedList()
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
        l = DoubleLinkedList()
        self.assertEqual(l.empty(), True)
        with self.assertRaises(Exception):
            l.lpop()
        with self.assertRaises(Exception):
            l.rpop()
