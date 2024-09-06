#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

import signal
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
    full_adder_2 = fullAdder(
        x[1], y[1], half_adder_1_carry, soma[1], full_adder_2_carry
    )

    @always_comb
    def comb():
        carry.next = full_adder_2_carry

    return instances()


@block
def adder(x, y, soma, carry):
    # size = len(x)
    # faList = [None for _ in range(size)]
    # sc = [Signal(bool(0)) for _ in range(size + 1)]
    # faList[0] = fullAdder(x[0], y[0], Signal(bool(0)), soma[0], sc[0])

    # for i in range(len(faList)):
    #     faList[i] = fullAdder(x[i], y[i], sc[i], soma[i], sc[i + 1])

    size = len(x)
    faList = [None for _ in range(size)]
    s_c = [Signal(bool(0)) for _ in range(size + 1)]
    faList[0] = fullAdder(x[0], y[0], Signal(bool(0)), soma[0], s_c[0])

    for i in range(1, len(faList)):
        faList[i] = fullAdder(x[i], y[i], s_c[i - 1], soma[i], s_c[i])

    @always_comb
    def comb():
        carry.next = s_c[size - 1]  # Last carry

    return instances()


@block
def sw2hex(hex_pins, sw):
    """
    Faz a conversão de binário para display de 7 segmentos
    """

    @always_comb
    def comb():
        if sw[4:0] == 0:
            hex_pins.next = "1000000"
        elif sw[4:0] == 1:
            hex_pins.next = "1111001"
        elif sw[4:0] == 2:
            hex_pins.next = "0100100"
        elif sw[4:0] == 3:
            hex_pins.next = "0110000"
        elif sw[4:0] == 4:
            hex_pins.next = "0011001"
        elif sw[4:0] == 5:
            hex_pins.next = "0010010"
        elif sw[4:0] == 6:
            hex_pins.next = "0000010"
        elif sw[4:0] == 7:
            hex_pins.next = "1011000"
        elif sw[4:0] == 8:
            hex_pins.next = "0000000"
        elif sw[4:0] == 9:
            hex_pins.next = "0010000"
        elif sw[4:0] == 10:
            hex_pins.next = "0001000"
        elif sw[4:0] == 11:
            hex_pins.next = "0000011"
        elif sw[4:0] == 12:
            hex_pins.next = "0100111"
        elif sw[4:0] == 13:
            hex_pins.next = "0100001"
        elif sw[4:0] == 14:
            hex_pins.next = "0000110"
        else:
            hex_pins.next = "0001110"

    return instances()
