#!/usr/bin/env python  
# coding=utf-8
import sys, getopt
from os import path
from crypto import Caesar, Atbash
from puzzle import Puzzle

def help():
    print "Help: %s OPTION text" % (path.basename(sys.argv[0]))
    print "OPTION:" 
    print "\t-h: help message." 
    print "\t--help: help message." 

def generateCaesarPicture(text, offset, clue = None, clue_pic = None):
    caesar = Caesar(text, offset, clue=clue, clue_pic=clue_pic)
    puzzle = Puzzle(caesar)
    puzzle.backgroud()
    puzzle.encryptData(to_ascii=False)
    puzzle.encryptCipherTable()
    puzzle.encryptClue()
    puzzle.encryptBrand()
    puzzle.encryptMaterial()
    puzzle.image.save('puzzle.png', 'PNG')
    #puzzle.image.show()
    puzzle.image.close()

def generateAtbashPicture(text, clue = None, clue_pic = None):
    caesar = Atbash(text, clue=clue, clue_pic=clue_pic)
    puzzle = Puzzle(caesar)
    puzzle.backgroud()
    puzzle.encryptData(to_ascii=False)
    puzzle.encryptCipherTable()
    puzzle.encryptClue()
    puzzle.encryptBrand()
    puzzle.encryptMaterial()
    puzzle.image.save('puzzle2.png', 'PNG')
    #puzzle.image.show()
    puzzle.image.close()

def main():
    try:
        opts, arguments = getopt.getopt(sys.argv[1:], 'h', ['help'])
    except getopt.GetoptError, err:
        print str(err)
        help()
        sys.exit(1)

    if (len(arguments) != 1): 
        help()

    puzzle_text = arguments[0]
    generateCaesarPicture(puzzle_text, 6-21, "6-21")
    generateAtbashPicture(puzzle_text, "The Da Vinci Code")

if __name__ == '__main__':
    main()
