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

print( shuffleList(["apple", "blackberry", "cherry", "dragonfruit", "grapefruit", "kumquat", "mango", "nectarine", "persimmon", "raspberry", "raspberry"]) )
print( shuffleList(["a", "e", "i", "o", "u"]) )

