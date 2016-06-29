#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import collections
import fileinput

def main():
    tileCount = { 'A':9, 'B':2, 'C':2, 'D':4, 'E':12,'F':2, 'G':3,
                  'H':2, 'I':9, 'J':1, 'K':1, 'L':4, 'M':2, 'N':6,
                  'O':8, 'P':2, 'Q':1, 'R':6, 'S':4, 'T':6, 'U':4,
                  'V':2, 'W':2, 'X':1, 'Y':2, 'Z':1, '_':2 }

    #inputString = 'LQTOONZOEFFJZT'
    #inputString = 'PQAREIOURSTHGWIOAE_'
    #inputString = 'LQTOONOEFFJZT'
    #inputString = 'AXHDRUIOR_XHJZUQEE'
    inputString = 'PQREAUTHGWU_EOTG'

    for c in inputString:
        if tileCount[c] == 0:
            raise ValueError("Invalid input. More {}'s have been taken from the bag than possible.".format(c))
        else:
            tileCount[c] -= 1

    out = collections.defaultdict(list)
    for k, v in tileCount.items():
        out[v].append(k)

    for k in sorted(out, reverse=True):
        sys.stdout.write("\n{}:".format(k))
        for c in out[k]:
            sys.stdout.write(" {}".format(c))

    print()

if __name__ == "__main__":
    main()
