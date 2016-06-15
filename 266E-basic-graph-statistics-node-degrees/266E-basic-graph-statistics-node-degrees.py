#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fileinput
import collections


def main():

    lines = [line.rstrip() for line in fileinput.input()]
    count = int(lines[0])
    degree = collections.defaultdict(int)
    for line in lines[1:]:
        for node in line.split():
            degree[node] += 1

    for k in sorted(degree, key=int):
        print("Node {} has a degree of {}".format(k,degree[k]))


if __name__ == "__main__":
    main()
