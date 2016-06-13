#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fileinput

def main():
    lines = [line.rstrip() for line in fileinput.input()]
    maxLineLen = max((len(line) for line in lines))

    transposedLines = []
    for x in range(maxLineLen):
        tl = ''
        for l in lines:
            if x < len(l):
                tl = tl + l[x]
            else:
                tl = tl + ' '

        transposedLines.append(tl)

    for l in transposedLines:
        print(l)


if __name__ == "__main__":
    main()
