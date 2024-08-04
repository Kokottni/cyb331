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

def readbinaryfile(filename):
  """returns the file as an array of single character strings"""
  return [chr(b) for b in open(filename, "rb").read(-1)]

def readazfile(filename):
  """Reads a text file and returns an array of only letters A-Z upcased"""
  f = open(filename, "r", encoding="utf-8")
  text = f.read()
  s = set(azalphabet)
  return [c.upper() for c in text if c.upper() in s]

def orderedCount(text, alphabet):
    ordered = [0 for i in range(len(alphabet))]
    j = 0
    totalChars = 0
    for i in alphabet:
       ordered[j] = text.count(i)
       totalChars += ordered[j]
       j += 1
    for i in range(0, len(alphabet)):
       ordered[i] = ordered[i] / totalChars
    return ordered

def normalizedIOC(ordered, alphabet):
    IOC = 0
    for i in range(0, len(alphabet)):
      IOC += math.pow(ordered[i], 2)
    IOC *= len(alphabet)
    return IOC

def entropyCalc(ordered, alphabet):
    entropy = 0
    for i in range(0, len(alphabet)):
      entropy += ordered[i] * math.log2(ordered[i])
    entropy *= -1
    return entropy

def main():

  fn = sys.argv[2]
  if sys.argv[1] == '-az':
    alphabet = azalphabet
    text = readazfile(fn)
  if sys.argv[1] == '-b':
    alphabet = binalphabet
    text = readbinaryfile(fn)
  
  ordered = orderedCount(text, alphabet)
  IOC = normalizedIOC(ordered, alphabet)
  entropy = entropyCalc(ordered, alphabet)
  print('The IOC for this file is: ' + str(IOC))
  print('The entropy for this file is: ' + str(entropy))


if __name__ == "__main__":
  ### sys.argv = ["", "-b", "foo.txt"]
  main()