#!/usr/bin/env python  
# coding=utf-8
from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

class Puzzle(object):
    def __init__(self, crypto, size=(800, 600)):
        self.image = None
        self.crypto = crypto
        self.size = size
    
    def backgroud(self):
        self.image = Image.new(mode='RGBA', size=self.size, color=self.crypto.backgroud)

    def encryptData(self, to_ascii = True):
        cipher = self.crypto.encrypt()
        W, H = self.size
        #font=ImageFont.truetype(os.path.expandvars("%SystemRoot%/Fonts/segoeui.ttf"), 16)
        font = ImageFont.truetype("./resouce/fonts/blooods_.ttf", 50)
        print cipher
        if to_ascii:
            cipher = cipher.encode("hex")
        print cipher
        image = Image.new(mode='RGBA', size=(W, H/3), color=(0, 0, 0, 0))
        draw_table = ImageDraw.Draw(im=image)
        #w, h = draw_table.textsize(cipher)
        #draw_table.text(((W-w)/2,(H/3-h)/2), text=cipher, fill='#FFFFFF', font=ImageFont.truetype(os.path.expandvars("%SystemRoot%/Fonts/segoeui.ttf"), 16))
        current_h, pad = 50, 10
        for line in textwrap.wrap(cipher, width=20):
            w, h = draw_table.textsize(line, font=font)
            draw_table.text(((W - w) / 2, current_h), line, font=font, fill='#FF1722')
            current_h += h + pad
        self.image.paste(image, (0, H/3), mask=image)
        image.close()

    
    def encryptCipherTable(self):
        if self.crypto.cipherTable:
            W, H = self.size
            font = ImageFont.truetype("./resouce/fonts/Insight Issue.ttf", 30)
            image = Image.new(mode='RGBA', size=(W, H/3), color=(0, 0, 0, 0))
            draw_table = ImageDraw.Draw(im=image)
            current_h, pad = 50, 10
            for line in textwrap.wrap(self.crypto.cipherTable, width=20):
                w, h = draw_table.textsize(line, font=font)
                draw_table.text(((W - w) / 2, current_h), line, font=font, fill='#FFFFFF')
                current_h += h + pad
            self.image.paste(image, (0, H*2/3), mask=image)
            image.close()
        
    def encryptClue(self):
        if self.crypto.clue:
            W, H = self.size
            font = ImageFont.truetype("./resouce/fonts/MING____.ttf", 36)
            image = Image.new(mode='RGBA', size=(W, H/3), color=(0, 0, 0, 0))
            draw_table = ImageDraw.Draw(im=image)
            current_h, pad = 50, 10
            for line in textwrap.wrap(self.crypto.clue, width=20):
                w, h = draw_table.textsize(line, font=font)
                draw_table.text(((W - w) / 2, current_h), line, font=font)
                current_h += h + pad
            self.image.paste(image, (0, 0), mask=image)
            image.close()
        
    def encryptBrand(self):
        img = Image.open('./resouce/images/v.png')
        img = img.resize((800,600), Image.ANTIALIAS)
        img.putalpha(125)
        self.image.paste(img, (0, 0), mask=img)
        img.close()
        
    def encryptMaterial(self):
        pass
