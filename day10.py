#!/usr/bin/python3
# Advent of Code 2015: Day 10

DATA = "1113222113"

data2 = DATA
part1 = 0

for i in range(50):

  data1 = data2
  data2 = ""
  hold = []
  temp = ""

  for place in range(len(data1)):
    
    temp += data1[place]

    if place == len(data1)-1: 
      hold.append(temp)

    else:
      if data1[place] != data1[place+1]:
        hold.append(temp)
        temp = ""

  for temp in hold:
    data2 += str(len(temp))+temp[0:1]

  if i == 39: part1 = len(data2) 

print ("Length of 40th iteration: "+str(part1))      
print ("Length of 50th iteration: "+str(len(data2))) 
