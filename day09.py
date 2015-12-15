#!/usr/bin/python3
# Advent of Code 2015: Day 9
import re

DATA = ["Faerun to Tristram = 65","Faerun to Tambi = 129","Faerun to Norrath = 144","Faerun to Snowdin = 71","Faerun to Straylight = 137","Faerun to AlphaCentauri = 3","Faerun to Arbre = 149","Tristram to Tambi = 63","Tristram to Norrath = 4","Tristram to Snowdin = 105","Tristram to Straylight = 125","Tristram to AlphaCentauri = 55","Tristram to Arbre = 14","Tambi to Norrath = 68","Tambi to Snowdin = 52","Tambi to Straylight = 65","Tambi to AlphaCentauri = 22","Tambi to Arbre = 143","Norrath to Snowdin = 8","Norrath to Straylight = 23","Norrath to AlphaCentauri = 136","Norrath to Arbre = 115","Snowdin to Straylight = 101","Snowdin to AlphaCentauri = 84","Snowdin to Arbre = 96","Straylight to AlphaCentauri = 107","Straylight to Arbre = 14","AlphaCentauri to Arbre = 46"]

reg_route = re.compile(r'(\w+)\ to\ (\w+)\ =\ (\d+)')
routes = []
sav_shrt_dist = 0
sav_long_dist = 0
sav_shrt_path = []
sav_long_path = []
curr_dist = 0
curr_path = []
all_cities = []

#Organize the data
for line in DATA:
  match = re.match(reg_route, line)
  routes.append([match.group(1),match.group(2),match.group(3)])
  if (not match.group(1) in all_cities): all_cities.append(match.group(1))
  if (not match.group(2) in all_cities): all_cities.append(match.group(2))

#Return the distance between two cities
def route_dist(city1, city2):
  for route in routes:
    if (city1 in route) & (city2 in route):
      return int(route[2])
  return 0

#Recursive hole
def recur(cities_left):
  global curr_dist, curr_path, sav_shrt_dist, sav_long_dist, sav_shrt_path, sav_long_path

  for city in cities_left:
    cities_2pass = list(cities_left)
    cities_2pass.remove(city)

    dist = route_dist(city, curr_path[len(curr_path)-1])
    if dist > 0 : # there is a path to this city
      curr_path.append(city)
      curr_dist += dist

      if len(cities_2pass) > 0: # more cities to visit, keep going down
        recur(cities_2pass)
 
      else: # this is a complete path
        if (sav_shrt_dist == 0) | (curr_dist < sav_shrt_dist) :
          sav_shrt_dist = curr_dist
          sav_shrt_path = list(curr_path)

        if curr_dist > sav_long_dist :
          sav_long_dist = curr_dist
          sav_long_path = list(curr_path)
        
      curr_path.remove(city)
      curr_dist -= dist

#MAIN
for city in all_cities:
  cities_2pass = list(all_cities)
  cities_2pass.remove(city)
  curr_path = [city]
  curr_dist = 0
  recur(cities_2pass)

print ("Shortest Path: "+str(sav_shrt_dist))
print (" Longest Path: "+str(sav_long_dist))
