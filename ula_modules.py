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
    s = [Signal(bool(0)) for _ in range(3)]
    haList = [None for _ in range(2)]

    haList[0] = halfAdder(a, b, s[0], s[1])
    haList[1] = halfAdder(c, s[0], soma, s[2])

    @always_comb
    def comb():
        carry.next = s[1] or s[2]

    return instances()


@block
def adder2bits(x, y, soma, carry):
    s_soma = [Signal(bool(0)) for _ in range(2)]
    half_adder_1_carry = Signal(bool(0))
    full_adder_2_carry = Signal(bool(0))

    half_adder_1 = halfAdder(x[0], y[0], soma[0], half_adder_1_carry)
    full_adder_2 = fullAdder(x[1], y[1], half_adder_1_carry, soma[1], full_adder_2_carry)


    @always_comb
    def comb():
        carry.next = full_adder_2_carry

    return instances()


@block
def adder(x, y, soma, carry):
    size = len(x)
    faList = [None for _ in range(size)]
    sc = [Signal(bool(0)) for _ in range(size+1)]
    faList[0] = fullAdder(x[0],y[0],Signal(bool(0)), soma[0], sc[0])

    for i in range(len(faList)):
        faList[i] = fullAdder(x[i],y[i],sc[i], soma[i], sc[i+1])

    @always_comb
    def comb():
        carry .next = sc[-1] # Last carry

    return instances()
