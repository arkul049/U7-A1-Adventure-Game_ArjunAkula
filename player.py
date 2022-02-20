from enemyIndex import *
import copy

fist = "8"
branch = "10"
shellSword = "20"
feather = "40"
hammer = "30"
ironSword = "50"
rainbSword = "90"

origStats = [80, fist, eight]
variStats = [80, fist, eight]

#list will have 0s if places are still unfinished, and 1s if they have been completed
#Bunny Fields, Blue Lake, Crystal Caverns, Howling Cliffs, Red Mountain
#Rainbow Falls 
locat = [0,0,0,0,0]

def updatePlayer():
  for i in range(3):
    variStats[i] = origStats[i]


