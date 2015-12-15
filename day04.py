#!/usr/bin/python3
# Advent of Code 2015: Day 4
import hashlib

DATA = "bgvyzdsv"

number = 0
fiveanswer = ""

while True:
  test = str.encode(DATA+str(number))
  md5hash = str(hashlib.md5(test).hexdigest())

  if (md5hash[:5] == "00000") & (not fiveanswer): fiveanswer = str(number)
  if md5hash[:6] == "000000": break
  else: number += 1

print ("5 zero answer: "+fiveanswer)
print ("6 zero answer: "+str(number))
