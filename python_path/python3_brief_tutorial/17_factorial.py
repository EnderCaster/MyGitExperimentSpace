# !/usr/bin/env python3
# -*- utf-8 -*-
import sys


def fact(n):
    """calc factorial use recursion"""
    if n == 0:
        return 1
    return n * fact(n-1)


def div(n):
    if n == 0:
        return 0
    return 10/n


def main(n):
    res = fact(n)
    print(res)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
