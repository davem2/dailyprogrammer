#!/usr/bin/env python

import wave # 1
import struct

ifile = wave.open("input.wav")
ofile = wave.open("output.wav", "w")
ofile.setparams(ifile.getparams())

sampwidth = ifile.getsampwidth()
fmts = (None, "=B", "=h", None, "=l")
print("sampwidth={}".format(sampwidth))
fmt = fmts[sampwidth]
print("fmt='{}'".format(fmt))
dcs  = (None, 128, 0, None, 0)
dc = dcs[sampwidth]

for i in range(ifile.getnframes()):
    iframe = ifile.readframes(1)
    iframe = struct.unpack(fmt, iframe)[0]
    iframe -= dc

    oframe = iframe / 2;

    oframe += dc
    oframe = struct.pack(fmt, oframe)
    ofile.writeframes(oframe)

ifile.close()
ofile.close()
