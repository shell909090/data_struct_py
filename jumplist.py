#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2018-09-20
@author: Shell.Xu
@copyright: 2018, Shell.Xu <shell909090@gmail.com>
@license: BSD-3-clause
'''
from __future__ import absolute_import, division,\
    print_function, unicode_literals
import random
import unittest

class JumpList(object):

    class Node(object):
        
        def __init__(self, o, N):
            self.o = o
            self.n = [None,] * N
    
    def __init__(self, iter=None, N=4):
        self.N = N
        self.head = JumpList.Node(None, N)
        if iter:
            for i in iter:
                self.add(i)

    @staticmethod
    def _lookup_prev(c, o, N):
        # c for current node, o for object, N for N-levels
        n = c.n[N]
        while True:
            if n is None or n.o >= o:
                if N == 0:
                    return [c,]
                l = JumpList._lookup_prev(c, o, N-1)
                l.append(c)
                return l
            c = n
            n = c.n[N]

    def add(self, o):
        # o for object, nn for new node.
        nn = JumpList.Node(o, self.N)
        l = JumpList._lookup_prev(self.head, o, self.N-1)
        for i, c in enumerate(l):
            if i != 0 and random.randint(0, 1) != 1:
                break
            nn.n[i] = c.n[i]
            c.n[i] = nn

    def remove(self, o):
        # l for level and c for current level
        l = JumpList._lookup_prev(self.head, o, self.N-1)
        n = l[0].n[0]
        if n is None or n.o != o:
            raise KeyError(o, n.o)
        for i, c in enumerate(l):
            n = c.n[i]
            if n is None or n.o != o:
                break
            c.n[i] = n.n[i]

    def _search(self, o):
        c = self.head
        N = self.N-1
        while c:
            if c.n[N] is None or c.n[N].o > o:
                if N == 0:
                    return
                else:
                    N -= 1
            if c.n[N] is not None:
                if c.n[N].o == o:
                    return c
                elif c.n[N].o < o:
                    c = c.n[N]

    def __contains__(self, o):
        return self._search(o) is not None

    def _iter_N_list(self, N):
        c = self.head.n[N]
        while c:
            yield c
            c = c.n[N]

    def print_level(self, N):
        print([i.o for i in self._iter_N_list(N)])

    def print_all(self):
        for i in reversed(range(self.N)):
            self.print_level(i)


def main():
    li = JumpList(range(10))

    li.print_all()
    print(3 in li)

    li.remove(3)
    li.remove(5)
    li.remove(8)

    li.print_all()
    print(3 in li)


if __name__ == '__main__':
    main()
