#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def strtobin(s):
    s = s.encode('utf-8')
    out = ''
    for c in s:
        out += format(c,'08b')

    return out


def uuencode(s):
    output = "begin 644 out.txt\n"
    bstring = strtobin(s)
    #print(bstring)

    line = ''
    while bstring:
        wb = bstring[:24]
        bstring = bstring[24:]
        #print(wb)
        while len(wb) < 24:
            wb += '0'

        #print(len(wb))

        # Encode 24 bits (4 6-bit values) into 4 bytes)
        ob = ''
        for i in range(4):
            v = int(wb[:6],2)
            wb = wb[6:]
            ch = chr(ord(' ') + v)
            ob += ch

        line += ob
        #print(line)

        if len(line) >= 60:
            #print(line)
            output += 'M{}\n'.format(line)
            line = ''

    if len(s) % 45 != 0:
        linelen = chr(ord(' ') + len(s) % 45)
        output += '{}{}\n'.format(chr(ord(' ') + len(s) % 45),line)

    output += '\nend\n'

    return output


def uudecode(s):
    return

def uudecode(line):
    return

def main():

    inp = "I feel very strongly about you doing duty. Would you give me a little more documentation about your reading in French? I am glad you are happy — but I never believe much in happiness. I never believe in misery either. Those are things you see on the stage or the screen or the printed pages, they never really happen to you in life."

    out = uuencode(inp)
    print(out)

if __name__ == "__main__":
    main()
