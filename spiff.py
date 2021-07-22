#!/usr/bin/env python3
__project__ = 'Spiffatron'
__version__ = '1.0'
__description__ = 'The spiffy text generator worth less than $10'
__author__ = 'Blue_595#2315'
__date__ = '2021-07-22'

import pyperclip
import re
from sys import argv

def gettable(path):
  table = { ' ': '        ' }
  file = open(path, 'r').read()
  for line in file.splitlines():
    if len(line) > 0 and line[0] != '#':
      table.update({line[:40].strip(): line[40:]})
  return table

def compile(table):
  d = {re.escape(k): v for k, v in table.items()}
  p = re.compile('|'.join(d.keys()))
  return lambda t : p.sub(lambda m : d[re.escape(m.group(0))], t)

def main():
  spiff = compile(gettable(argv[1]))
  text = spiff(pyperclip.paste().lower())
  pyperclip.copy(text)

if __name__ == '__main__':
  main()
