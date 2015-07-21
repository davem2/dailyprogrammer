import random

# Richard Durstenfeld version of Fisher-Yates shuffle
# https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#Modern_method
def shuffleList( l ):
    e = len(l)-1
    while( e >= 1 ):
        i = random.randint(0,e)
        l[e], l[i] = l[i], l[e]
        e = e - 1

    return l

def shuffleList2( l ):
    l2 = l[:]
    for i in range(len(l)-1,0,-1): j = random.randint(0,i); l2[i],l2[j]=l2[j],l2[i]
    return l2

print( shuffleList(["apple", "blackberry", "cherry", "dragonfruit", "grapefruit", "kumquat", "mango", "nectarine", "persimmon", "raspberry", "raspberry"]) )
print( shuffleList(["a", "e", "i", "o", "u"]) )

