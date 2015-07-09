#!/usr/bin/env python3

def lcg( seed ):
    m = 2 ** 32
    a = 1664525
    c = 1013904223

    while True:
        seed = ((a * seed) + c) % m
        yield seed

def encrypt( msg, key ):
    rng = lcg(key)
    return ''.join([chr((ord(ch) ^ next(rng)) & 0xFF) for ch in msg])

def decrypt( msg, key ):
    rng = lcg(key)
    return ''.join([chr((ord(ch) ^ next(rng)) & 0xFF) for ch in msg])

def main():
    key = 31337
    msg = "Attack at dawn"
    ciphertext = encrypt(msg, key)
    plaintext = decrypt(ciphertext, key)
    print(ciphertext)
    print(plaintext)

    rng = lcg(key)
    for i in range(0,1000):
        print(next(rng))

if __name__ == "__main__":
	main()
