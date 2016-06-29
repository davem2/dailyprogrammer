#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
from array import array

def NoDither(filename):
    im = Image.open(filename)
    px = im.load()
    w, h = im.size

    for y in range(h):
        for x in range(w):
            v = px[x,y]
            if v < 128:
                px[x,y] = 0
            else:
                px[x,y] = 255

    return im


def OneDimensionalErrorDiffusionDithering(filename):
    im = Image.open(filename)
    px = im.load()
    w, h = im.size

    for y in range(h):
        error = 0
        for x in range(w):
            p = px[x,y]
            v = p + error
            if v < 128:
                px[x,y] = 0
                error = v
            else:
                px[x,y] = 255
                error = -(255 - v)

    return im




matrices = (
    ('FloydSteinberg',16,
        [(1,0,7),(-1,1,3),(0,1,5),(1,1,1)]),
    ('JarvisJudiceNinke',48,
        [(1,0,7),(2,0,5),(-2,1,3),(-1,1,5),(0,1,7),(1,1,5),(2,1,3),(-2,2,1),(-1,2,3),(0,2,5),(1,2,3),(2,2,1)]),
    ('Stucki',42,
        [(1,0,8),(2,0,4),(-2,1,2),(-1,1,4),(0,1,8),(1,1,4),(2,1,2),(-2,2,1),(-1,2,2),(0,2,4),(1,2,2),(2,2,1)]),
    ('Atkinson',8,
        [(1,0,1),(2,0,1),(-1,1,1),(0,1,1),(1,1,1),(0,2,1)]),
    ('Burkes',32,
        [(1,0,8),(2,0,4),(-2,1,2),(-1,1,4),(0,1,8),(1,1,4),(2,1,2)]),
    ('Sierra',32,
        [(1,0,5),(2,0,3),(-2,1,2),(-1,1,4),(0,1,5),(1,1,4),(2,1,2),(-1,2,2),(0,2,3),(2,2,2)]),
    ('TwoRowSierra',16,
        [(1,0,4),(2,0,3),(-2,1,1),(-1,1,2),(0,1,3),(1,1,2),(2,1,1)]),
    ('SierraLite',4,
        [(1,0,2),(-1,1,1),(0,1,1)])
)


def DitherBW(im,matrix,denom=None):
    px = im.load()
    w, h = im.size
    if not denom:
        denom = sum([m[2] for m in matrix])

    for y in range(h):
        error = 0
        for x in range(w):
            p = px[x,y]
            v = p

            if v < 128:
                px[x,y] = 0
                error = v
            else:
                px[x,y] = 255
                error = -(255 - v)

            frac = error / denom
            for m in matrix:
                try:
                    dx, dy, v = m
                    px[x+dx,y+dy] += int(frac * v)
                except IndexError:
                    pass

    return im


def DitherColor(im,matrix,denom=None):
    px = im.load()
    w, h = im.size
    if not denom:
        denom = sum([m[2] for m in matrix])

    for y in range(h):
        error = 0
        for x in range(w):
            p = px[x,y]
            r, g, b = p
            cv = [0,0,0]

            for c in range(0,3):
                if p[c] < 64:
                    cv[c] = 0
                    error = p[c]
                elif p[c] > 196:
                    cv[c] = 255
                    error = -(255 - p[c])
                else:
                    cv[c] = 128
                    error = -(128 - p[c])

                px[x,y] = tuple(cv)

                frac = error / denom
                for m in matrix:
                    try:
                        dx, dy, v = m
                        o = list(px[x+dx,y+dy])
                        o[c] += int(frac * v)
                        px[x+dx,y+dy] = (o[0],o[1],o[2])
                    except IndexError:
                        pass

    return im


def main():

    #for i in range(len(matrices)):
    #    print(matrices[i])
    #    im = DitherBW(Image.open("testbw.jpg"),matrices[i][2],denom=matrices[i][1])
    #    im.show()

    for i in range(len(matrices)):
        print(matrices[i])
        im = DitherColor(Image.open("test3.jpg"),matrices[i][2],denom=matrices[i][1])
        im.save("{}.png".format(matrices[i][0]),"png")



if __name__ == "__main__":
    main()
