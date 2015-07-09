#!/usr/bin/env python3

def main():
    words = [ "AAA","A","AA","CONSUBSTANTIATION", "WRONGHEADED", "UNINTELLIGIBILITY", "SUPERGLUE" ]

    for word in words:
        balanceWord( word )

def balanceWord( s ):
    for i in range(1,len(s)-1):
        leftWord = s[0:i]
        rightWord = s[i+1:]
        if calcWeight(leftWord[::-1]) == calcWeight(rightWord):
            print("{} {} {} - {}".format(leftWord,s[i],rightWord,calcWeight(rightWord)))
            return calcWeight(rightWord)
    else:
        print("{} DOES NOT BALANCE".format(s))
        return None

def calcWeight( s ):
    weight = 0
    for i,l in enumerate(s.upper()):
        weight += (ord(l)-ord('A')+1) * (i+1)

    return weight

if __name__ == "__main__":
	main()
