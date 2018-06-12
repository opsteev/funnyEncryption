#!/usr/bin/env python  
# coding=utf-8
import string
from string import ascii_letters

class Caesar(object):
    def __init__(self, text, offset, clue = None, clue_pic = None):
        self.text = text
        self.offset = offset
        self.clue = clue
        self.clue_pic = clue_pic
        self.cipher = None
        self.backgroud = (0, 0, 0, 255)
        self.cipherTable = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def encrypt(self):
        self.cipher = string.maketrans(ascii_letters, \
                        ascii_letters[self.offset:] + ascii_letters[:self.offset])
        return self.text.translate(self.cipher)

class Atbash(object):
    def __init__(self, text, clue = None, clue_pic = None):
        self.text = text
        self.clue = clue
        self.clue_pic = clue_pic
        self.cipher = None
        self.backgroud = (0, 0, 0, 255)
        self.cipherTable = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[::-1]
    def encrypt(self):
        a_z = map(chr, range(ord('a'), ord('z')+1))
        z_a = sorted(a_z, reverse=True)
        A_Z = map(chr, range(ord('A'), ord('Z')+1))
        Z_A = sorted(A_Z, reverse=True)
        conv_table = dict(zip(a_z, z_a))
        conv_table.update(dict(zip(A_Z, Z_A)))
        result_as_chars = (conv_table[char] if char in conv_table else char for char in self.text )
        self.cipher = ''.join(result_as_chars)
        return self.cipher
