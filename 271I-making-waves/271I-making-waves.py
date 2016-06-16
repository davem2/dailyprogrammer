#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wave
import struct
import math

def main():

    sampleRate = 8000
    noteDuration = 300 # ms
    notes = "ABCDEFG_GFEDCBA"
    samplesPerNote = round(sampleRate/1000.0 * noteDuration)
    dcOffset = 2**7-1

    frequency = { '_':1, 'C':261.63, 'D':293.66, 'E':329.63, 'F':349.23, 'G':392.00, 'A':440.00, 'B':493.88 }

    with wave.open("output.wav","w") as w:
        w.setparams((1, 1, sampleRate, 0, 'NONE', 'no compression'))

        data = []
        for note in notes:

            wavelength = sampleRate / frequency[note]
            for s in range(0,samplesPerNote):
                if note == '_':
                    v = dcOffset
                else:
                    amp = 1 - abs((samplesPerNote / 2) - s) / (samplesPerNote / 2)
                    v = int(round(dcOffset + (amp*math.sin(2.0*math.pi*s/wavelength) * dcOffset)))
                frame = struct.pack("=B", v)
                data.append(frame)

        w.writeframes(b''.join(data))


if __name__ == "__main__":
    main()
