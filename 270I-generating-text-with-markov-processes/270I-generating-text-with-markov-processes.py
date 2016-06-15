#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import fileinput
import collections
import random


def gen_text(text,prefixSize):
    suffixMap = gen_suffix_map(text,prefixSize)

    newWords = []
    words = text.split()
    x = random.choice(range(len(words)-prefixSize))
    p = words[x:x+prefixSize]
    for i in range(5000):
        s = random.choice(suffixMap[''.join(p)] or words)

        newWords.append(s)

        p.append(s)
        p = p[1:]

    return ' '.join(newWords)


def gen_suffix_map(text,prefixSize):
    words = text.split()
    suffixMap = collections.defaultdict(list)
    for i in range(len(words)-prefixSize):
        p = words[i:i+prefixSize]
        s = words[i+prefixSize]
        suffixMap[''.join(p)].append(s)

    return suffixMap


def main():
    text = '\n'.join([line.rstrip() for line in fileinput.input()])
    print(gen_text(text,2))


if __name__ == "__main__":
    main()
