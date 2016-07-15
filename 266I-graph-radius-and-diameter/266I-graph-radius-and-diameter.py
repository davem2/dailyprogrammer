#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fileinput
import collections

def main():

    lines = [line.rstrip() for line in fileinput.input()]
    count = int(lines[0])
    graph = collections.defaultdict(list)
    for line in lines[1:]:
        a, b = line.split()
        graph[a].append(b)
        graph[b].append(a)

    for k in sorted(graph, key=int):
        print("Node {} has a degree of {}".format(k,len(graph[k])))


if __name__ == "__main__":
    main()
