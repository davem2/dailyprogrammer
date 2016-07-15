#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def decrypt(messagefile,cypherfile):

    numbers = [int(x) for x in open(messagefile).read().split(',')]
    cypher = [s[0] for s in open(cypherfile).read().split(' ')]

    return ''.join([cypher[m-1] for m in numbers])


def main():
    print(decrypt("numbers.txt","declaration_of_independence.txt"))


if __name__ == "__main__":
    main()
