#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


@block
def halfAdder(a, b, soma, carry):
    @always_comb
    def comb():
        soma.next = (a or b) and not (a and b)
        carry.next = a and b

    return instances()


@block
def fullAdder(a, b, c, soma, carry):
    # adder_1_soma = Signal(bool(0))
    # adder_1_carry = Signal(bool(0))
    # adder_2_soma = Signal(bool(0))
    # adder_2_carry = Signal(bool(0))

    # adder_1 = halfAdder(a, b, adder_1_soma, adder_1_carry)
    # adder_2 = halfAdder(c, adder_1_soma, adder_2_soma, adder_2_carry)

    s = [Signal(bool(0)) for _ in range(3)]

    adder_1 = halfAdder(a, b, s[0], s[1])
    adder_2 = halfAdder(c, s[0], soma, s[2])

    @always_comb
    def comb():
        # soma.next = adder_2_soma
        # carry.next = adder_1_carry or adder_2_carry
        carry.next = s[1] or s[2]

    return instances()


@block
def adder2bits(x, y, soma, carry):
    return instances()


@block
def adder(x, y, soma, carry):
    @always_comb
    def comb():
        pass

    return instances()
