#Nicholas Kokott (kokottni)

import os
import sys
import matplotlib.pyplot as plt
from collections import Counter
import math

def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)):
        yield chr(c)
    yield chr(ord(c2))

azalphabet = [ a for a in char_range('A', 'Z') ]

binalphabet = [a for a in char_range('\0', '\xff')]

def readazfile(filename):
  """Reads a text file and returns an array of only letters A-Z upcased"""
  f = open(filename, "r", encoding="utf-8")
  text = f.read()
  s = set(azalphabet)
  return [c.upper() for c in text if c.upper() in s]

def readkeyfileAlpha(filename, length):
    f = open(filename, "r", encoding="utf-8")
    if length == -1:
        text = f.read()
    else:
        text = f.read(length)
    return text

def readkeyfileBin(filename, length):
    return [chr(b) for b in open(filename, "rb").read(length)]

def readbinaryfile(filename):
  """returns the file as an array of single character strings"""
  return [chr(b) for b in open(filename, "rb").read(-1)]

def encryptAlpha(text, key):
    #for every character in text, shift by current spot in key
    #Adjust for the alphabet going past z and then add one to key index
    length = len(key)
    keyPos = 0
    output = ''
    for ch in text:
        shift = azalphabet.index(key[keyPos])
        charLocation = azalphabet.index(ch)
        if shift + charLocation > 25:
            updatedCharLocation = (shift + charLocation) % 26
            updatedChar = azalphabet[updatedCharLocation]
        else:
            updatedChar = azalphabet[shift + charLocation]
        output += updatedChar
        if keyPos + 1 >= length:
            keyPos = 0
        else:
            keyPos += 1
    return output

def encryptBin(text, key):
    length = len(key)
    keyPos = 0
    output = bytearray()
    for b in text:
        shift = ord(key[keyPos])
        byteLocation = ord(b)
        if shift + byteLocation > 255:
            updatedByteLocation = (shift + byteLocation) % 256
            updatedByte = ord(binalphabet[updatedByteLocation])
        else:
            updatedByte = ord(binalphabet[shift + byteLocation])
        output.append(updatedByte)
        if keyPos + 1 >= length:
            keyPos = 0
        else:
            keyPos += 1
    return output

def decryptAlpha(text, key):
    length = len(key)
    keyPos = 0
    output = ''
    for ch in text:
        shift = azalphabet.index(key[keyPos])
        charLocation = azalphabet.index(ch)
        if charLocation - shift < 0:
            updatedCharLocation = (charLocation - shift) + 26
            updatedChar = azalphabet[updatedCharLocation]
        else:
            updatedChar = azalphabet[charLocation - shift]
        output += updatedChar
        if keyPos + 1 >= length:
            keyPos = 0
        else:
            keyPos += 1
    return output

def decryptBin(text, key):
    length = len(key)
    keyPos = 0
    output = bytearray()
    for b in text:
        shift = ord(key[keyPos])
        byteLocation = ord(b)
        if byteLocation - shift < 0:
            updatedByteLocation = (byteLocation - shift) + 256
            updatedByte = ord(binalphabet[updatedByteLocation])
        else:
            updatedByte = ord(binalphabet[byteLocation - shift])
        output.append(updatedByte)
        if keyPos + 1 >= length:
            keyPos = 0
        else:
            keyPos += 1
    return output

def main():

    length = int(sys.argv[2])
    fn = sys.argv[5]
    if sys.argv[3] == '-az':
        alphabet = azalphabet
        changedkeyfile = readkeyfileAlpha(sys.argv[4], length)
        text = readazfile(fn)
    if sys.argv[3] == '-b':
        alphabet = binalphabet
        changedkeyfile = readkeyfileBin(sys.argv[4], length)
        text = readbinaryfile(fn)
    if sys.argv[1] == 'enc' and sys.argv[3] == '-az':
        output = encryptAlpha(text, changedkeyfile)
    if sys.argv[1] == 'dec'and sys.argv[3] == '-az':
        output = decryptAlpha(text, changedkeyfile)
    if sys.argv[1] == 'enc' and sys.argv[3] == '-b':
        output = encryptBin(text, changedkeyfile)
    if sys.argv[1] == 'dec' and sys.argv[3] == '-b':
        output = decryptBin(text, changedkeyfile)

    if sys.argv[3] == '-az':
        endfile = open(sys.argv[6], "w", encoding="utf-8")
        endfile.write(output)
        endfile.close()
    else:
        endfile = open(sys.argv[6], "wb")
        #byteoutput = bytes(output, 'utf-8')
        endfile.write(output)
        endfile.close()
        
    
    


if __name__ == "__main__":
  ### sys.argv = ["", "-b", "foo.txt"]
  main()