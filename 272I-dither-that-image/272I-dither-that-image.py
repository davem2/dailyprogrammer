#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
from array import array

def NoDither(filename):
    im = Image.open("testbw.jpg")
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
    im = Image.open("testbw.jpg")
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


def FloydSteinbergDithering(filename):
    im = Image.open("testbw.jpg")
    px = im.load()
    w, h = im.size

    forwardArray = [0*w]

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

            # Spread error to surrounding pixels
            sixteenth = error / 16.0
            try:
                px[x+1,y] += int(sixteenth * 7)
                px[x-1,y+1] += int(sixteenth * 3)
                px[x,y+1] += int(sixteenth * 5)
                px[x+1,y+1] += int(sixteenth * 1)
            except IndexError:
                pass

    return im


def JarvisJudiceNinkeDithering(filename):
    im = Image.open("testbw.jpg")
    px = im.load()
    w, h = im.size

    forwardArray = [0*w]

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

            # Spread error to surrounding pixels
            fourtyeigth = error / 48.0
            try:
                px[x+1,y] += int(fourtyeigth * 7)
                px[x+2,y] += int(fourtyeigth * 5)
                px[x-2,y+1] += int(fourtyeigth * 3)
                px[x-1,y+1] += int(fourtyeigth * 5)
                px[x,y+1] += int(fourtyeigth * 7)
                px[x+1,y+1] += int(fourtyeigth * 5)
                px[x+2,y+1] += int(fourtyeigth * 3)
                px[x-2,y+2] += int(fourtyeigth * 1)
                px[x-1,y+2] += int(fourtyeigth * 3)
                px[x,y+2] += int(fourtyeigth * 5)
                px[x+1,y+2] += int(fourtyeigth * 3)
                px[x+2,y+2] += int(fourtyeigth * 1)
            except IndexError:
                pass

    return im


def StuckiDithering(filename):
    im = Image.open("testbw.jpg")
    px = im.load()
    w, h = im.size

    forwardArray = [0*w]

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

            # Spread error to surrounding pixels
            fourtysecond = error / 42.0
            try:
                px[x+1,y] += int(fourtysecond * 8)
                px[x+2,y] += int(fourtysecond * 4)
                px[x-2,y+1] += int(fourtysecond * 2)
                px[x-1,y+1] += int(fourtysecond * 4)
                px[x,y+1] += int(fourtysecond * 8)
                px[x+1,y+1] += int(fourtysecond * 4)
                px[x+2,y+1] += int(fourtysecond * 2)
                px[x-2,y+2] += int(fourtysecond * 1)
                px[x-1,y+2] += int(fourtysecond * 2)
                px[x,y+2] += int(fourtysecond * 4)
                px[x+1,y+2] += int(fourtysecond * 2)
                px[x+2,y+2] += int(fourtysecond * 1)
            except IndexError:
                pass

    return im


def AtkinsonDithering(filename):
    im = Image.open("testbw.jpg")
    px = im.load()
    w, h = im.size

    forwardArray = [0*w]

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

            # Spread error to surrounding pixels
            eigth = error / 8.0
            try:
                px[x+1,y] += int(eigth * 1)
                px[x+2,y] += int(eigth * 1)
                px[x-1,y+1] += int(eigth * 1)
                px[x,y+1] += int(eigth * 1)
                px[x+1,y+1] += int(eigth * 1)
                px[x,y+2] += int(eigth * 1)
            except IndexError:
                pass

    return im


def BurkesDithering(filename):
    im = Image.open("testbw.jpg")
    px = im.load()
    w, h = im.size

    forwardArray = [0*w]

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

            # Spread error to surrounding pixels
            thirtysecond = error / 32.0
            try:
                px[x+1,y] += int(thirtysecond * 8)
                px[x+2,y] += int(thirtysecond * 4)
                px[x-2,y+1] += int(thirtysecond * 2)
                px[x-1,y+1] += int(thirtysecond * 4)
                px[x,y+1] += int(thirtysecond * 8)
                px[x+1,y+1] += int(thirtysecond * 4)
                px[x+2,y+1] += int(thirtysecond * 2)
            except IndexError:
                pass

    return im


def SierraDithering(filename):
    im = Image.open("testbw.jpg")
    px = im.load()
    w, h = im.size

    forwardArray = [0*w]

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

            # Spread error to surrounding pixels
            thirtysecond = error / 32.0
            try:
                px[x+1,y] += int(thirtysecond * 5)
                px[x+2,y] += int(thirtysecond * 3)
                px[x-2,y+1] += int(thirtysecond * 2)
                px[x-1,y+1] += int(thirtysecond * 4)
                px[x,y+1] += int(thirtysecond * 5)
                px[x+1,y+1] += int(thirtysecond * 4)
                px[x+2,y+1] += int(thirtysecond * 2)
                px[x-1,y+2] += int(thirtysecond * 2)
                px[x,y+2] += int(thirtysecond * 3)
                px[x+2,y+2] += int(thirtysecond * 2)
            except IndexError:
                pass

    return im


def TwoRowSierraDithering(filename):
    im = Image.open("testbw.jpg")
    px = im.load()
    w, h = im.size

    forwardArray = [0*w]

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

            # Spread error to surrounding pixels
            sixteenth = error / 16.0
            try:
                px[x+1,y] += int(sixteenth * 4)
                px[x+2,y] += int(sixteenth * 3)
                px[x-2,y+1] += int(sixteenth * 1)
                px[x-1,y+1] += int(sixteenth * 2)
                px[x,y+1] += int(sixteenth * 3)
                px[x+1,y+1] += int(sixteenth * 2)
                px[x+2,y+1] += int(sixteenth * 1)
            except IndexError:
                pass

    return im


def SierraLiteDithering(filename):
    im = Image.open("testbw.jpg")
    px = im.load()
    w, h = im.size

    forwardArray = [0*w]

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

            # Spread error to surrounding pixels
            fourth = error / 4.0
            try:
                px[x+1,y] += int(fourth * 2)
                px[x-1,y+1] += int(fourth * 1)
                px[x,y+1] += int(fourth * 1)
            except IndexError:
                pass

    return im


def DitherBW(im,matrix):
    px = im.load()
    w, h = im.size
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


def DitherColor(im,matrix):
    px = im.load()
    w, h = im.size
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
                elif p[c] < 192:
                    cv[c] = 128
                    error = -(128 - p[c])
                else:
                    cv[c] = 255
                    error = -(255 - p[c])

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


    im = Image.open("testbw.jpg")
    #im.show()
    im = DitherBW(im,[(1,0,2),(-1,1,1),(0,1,1)])
    im.show()
    #im2 = Image.open("test3.jpg")
    #px = array.frombytes(im2.getdata())
    #im3 = Image.fromarray(px)
    #im3.show()

    im = Image.open("test.jpg")
    im = DitherColor(im,[(1,0,4),(-1,1,1),(0,1,2),(1,1,1)])
    im.show()


    im = NoDither("testbw.jpg")
    im.show()

    im = OneDimensionalErrorDiffusionDithering("testbw.jpg")
    im.show()

    im = FloydSteinbergDithering("testbw.jpg")
    im.show()

    im = JarvisJudiceNinkeDithering("testbw.jpg")
    im.show()

    im = StuckiDithering("testbw.jpg")
    im.show()

    im = AtkinsonDithering("testbw.jpg")
    im.show()

    im = BurkesDithering("testbw.jpg")
    im.show()

    im = SierraDithering("testbw.jpg")
    im.show()

    im = TwoRowSierraDithering("testbw.jpg")
    im.show()

    im = SierraLiteDithering("testbw.jpg")
    im.show()


if __name__ == "__main__":
    main()
