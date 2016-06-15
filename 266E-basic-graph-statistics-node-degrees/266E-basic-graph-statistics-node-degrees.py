#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fileinput

def main():

    lines = [line.rstrip() for line in fileinput.input()]
    count = int(lines[0])
    degree = [0 for n in range(count)]
    for line in lines[1:]:
        for node in line.split():
            degree[int(node)-1] += 1

    for i, d in enumerate(degree):
        print("Node {} has a degree of {}".format(i+1,d))


if __name__ == "__main__":
    main()
