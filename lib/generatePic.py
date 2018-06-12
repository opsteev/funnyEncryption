#!/usr/bin/env python  
# coding=utf-8
from crypto import Caesar, Atbash
from puzzle import Puzzle
import io
import base64

def generateCaesarPicture(text, offset, clue = None, clue_pic = None):
    caesar = Caesar(text, offset, clue=clue, clue_pic=clue_pic)
    puzzle = Puzzle(caesar)
    puzzle.backgroud()
    puzzle.encryptData(to_ascii=False)
    puzzle.encryptCipherTable()
    puzzle.encryptClue()
    puzzle.encryptBrand()
    puzzle.encryptMaterial()
    output = io.BytesIO()
    puzzle.image.save(output, 'PNG')
    #puzzle.image.show()
    hex_data = output.getvalue()
    puzzle.image.close()
    return hex_data

def generateAtbashPicture(text, clue = None, clue_pic = None):
    caesar = Atbash(text, clue=clue, clue_pic=clue_pic)
    puzzle = Puzzle(caesar)
    puzzle.backgroud()
    puzzle.encryptData(to_ascii=False)
    puzzle.encryptCipherTable()
    puzzle.encryptClue()
    puzzle.encryptBrand()
    puzzle.encryptMaterial()
    output = io.BytesIO()
    puzzle.image.save(output, 'PNG')
    #puzzle.image.show()
    hex_data = base64.b64encode(output.getvalue())
    print hex_data
    puzzle.image.close()
    return hex_data
