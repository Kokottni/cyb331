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

def normBar(alpha, y, title="", imagename = None):
    """Outputs a bar graph histgram given counts as y, and symbols as alpha"""
    ticks = None
    if alpha is binalphabet:
      na = []
      ticks = []
      for number in alpha:
        na.append(hex(ord(number)).lstrip("0x"))
        if ord(number) % 8 == 0:
          ticks.append(ord(number))
      alpha = na
    n = sum(y)
    ny = norm(y)
    plt.bar(alpha, ny)
    if ticks is not None:
      plt.xticks(ticks)
    plt.title(title)
    if imagename is not None:
      plt.savefig(imagename)
    plt.show()


def norm(x):
  """Normalizes an array of counts so that it sums
  to 1.0."""
  s = sum(x)
  return [i / s for i in x]

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
    count = Counter(text)
    ordered = [0]*len(alphabet)
    for index, a in enumerate(alphabet):
        ordered[index] = count[a]
    return ordered
    
def bdist(p,q):
    """Bhattacharyya Distance between two probability distributions. Must be normed
    assumes both p and q come from the same alphabet and are ordered"""
    s = [math.sqrt(x*y) for x,y in zip(p,q)]
    return -1.0*math.log(sum(s))
    
def main():

  fn = sys.argv[2]
  if sys.argv[1] == '-az':
    alphabet = azalphabet
    text = readazfile(fn)
  if sys.argv[1] == '-b':
    alphabet = binalphabet
    text = readbinaryfile(fn)
  
  ordered = orderedCount(text, alphabet)
  normBar(alphabet, ordered, title=fn, imagename=fn+".png")


if __name__ == "__main__":
  ### sys.argv = ["", "-b", "foo.txt"]
  main()
