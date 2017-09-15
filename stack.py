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


class Stack(object):

    def __init__(self):
        self.head = None

    def push(self, o):
        self.head = (o, self.head)

    def pop(self):
        if self.head is None:
            raise Exception('empty stack')
        o, self.head = self.head
        return o

    def empty(self):
        return self.head is None


class StackTest(unittest.TestCase):

    def test_stack(self):
        s = Stack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.pop(), 2)
        s.push(3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 1)

    def test_empty(self):
        s = Stack()
        self.assertEqual(s.empty(), True)
        with self.assertRaises(Exception):
            s.pop()
