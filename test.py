import sys

#from jains import *

text = sys.argv[1]
with open(text) as f:
    lines = [line.rstrip() for line in f]

print(lines)

#jfi(lines)