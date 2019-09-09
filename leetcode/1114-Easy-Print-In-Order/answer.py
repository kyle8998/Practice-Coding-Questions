#!/usr/bin/env python3

#-------------------------------------------------------------------------------
from threading import Barrier

class Foo:
    def __init__(self):
        self.first_barrier = Barrier(2)
        self.second_barrier = Barrier(2)
        pass


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_barrier.wait()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.first_barrier.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.second_barrier.wait()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.second_barrier.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
#-------------------------------------------------------------------------------
