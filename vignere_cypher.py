#!/usr/bin/env python2

import collections
import string
import itertools

msg = 'm311a50_0x_a1rn3x3_h1ah3xfmel1g3m'

key = 'flag'

def encrypt(msg, key, multiplier = -1):
    lowercase_msg = msg.lower()

    for punctuation in str(string.punctuation + ' '):
        lowercase_msg = lowercase_msg.replace(punctuation, '')

    cycler = itertools.cycle(key.lower())
    long_key = ''.join([next(cycler) for _ in range(len(lowercase_msg)) ])
    
    coded = []
    for number in range(len(long_key)):
        cipher_letter = lowercase_msg[number]
        key_letter = long_key[number]
        key_index = string.lowercase.index(key_letter)
        cipher_index = string.lowercase.index(cipher_letter)
        
        lowercase = collections.deque(string.lowercase)
        lowercase.rotate(multiplier * key_index)
        new_alphabet = ''.join(list(lowercase))
        new_character = new_alphabet[cipher_index]
        coded.append(new_character)

    return ''.join(coded)

def decrypt(msg, key):
    return encrypt(msg, key, 1) 

print(decrypt(msg, key))
