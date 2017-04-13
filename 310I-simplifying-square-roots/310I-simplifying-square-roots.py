#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def product(values=None):
    p = 1
    for x in values:
        p = p*x
    return p


a, b, c, d = map(int, sys.argv[1:])

c = c * d
b = b * d

afactors = prime_factors(a)
bfactors = prime_factors(b)
cfactors = prime_factors(c)

# Simplify b by searching for pairs of common factors (perfect squares)
duplicates = []
seen = []
for f in bfactors[:]:
    if f in seen:
        duplicates.append(f)
    else:
        seen.append(f)

for f in duplicates:
    afactors.append(f)
    bfactors.remove(f)
    bfactors.remove(f)

# Simplify a and c by removing factors
for f in afactors[:]:
    if f in cfactors:
        afactors.remove(f)
        cfactors.remove(f)

# Reduce fraction
i = set(afactors).intersection(set(cfactors))
afactors = list(set(afactors).difference(i))
cfactors = list(set(cfactors).difference(i))

a = product(afactors)
b = product(bfactors)
c = product(cfactors)

print("{} sqr({}) / {}".format(a,b,c))

