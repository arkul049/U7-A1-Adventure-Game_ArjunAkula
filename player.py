from enemyIndex import *
import copy

#this is what permanent upgrades are applied to
origStats = [80, 8, nine]
#instance of origStats
#this will be changes following battles, to origStats
variStats = copy.deepcopy(origStats)

#list will have 0s if places are still unfinished, and 1s if they have been completed
#Bunny Fields, Blue Lake, Crystal Caverns, Howling Cliffs, Red Mountain
#Rainbow Falls opens when all locations = 1
locat = [0,0,0,0,0]

def updatePlayer():
  """
  Updates instance of origStats in variStats.
  """
  for i in range(3):
    variStats[i] = origStats[i]


