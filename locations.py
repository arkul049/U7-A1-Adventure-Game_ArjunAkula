from battleLogic import *
import time

def title():
  print("Rainbow Falls")
  time.sleep(1)
  ent()
def tutorial():
  screen_clear()
  time.sleep(0.5)
  print("You wake to find yourself lying in front of a giant tree.")
  time.sleep(0.25)
  ent()
  print("<::"+bcolors.TREE+"::>")
  time.sleep(0.25)
  print("Welcome,")
  time.sleep(0.25)
  print("I am the Great Oak, who keeps order across the "+bcolors.BOLD+"Magic Forest"+bcolors.ENDC+".")
  time.sleep(0.25)
  ent()
  print("<::"+bcolors.PLAYER+"::>")
  time.sleep(0.5)
  print(" . . . ")
  time.sleep(0.25)
  ent()
  print("<::"+bcolors.TREE+"::>")
  time.sleep(0.25)
  print("Unfortunatley, the "+bcolors.FKING+" stole the Rainbow Key.")
  time.sleep(0.25)
  print("He, along with the "+bcolors.WKING+", "+bcolors.SKING+", and the Wind King plan to use it to overthrow me.")
  time.sleep(0.25)
  print("This will destroy the "+bcolors.BOLD+"Magic Forest"+bcolors.ENDC+",")
  time.sleep(0.25)
  print("So I made you with my magic to defeat the kings, as my kind cannot fight.")
  time.sleep(0.25)
  ent()
  print("<::"+bcolors.PLAYER+"::>")
  time.sleep(0.5)
  print(" . . . ")
  time.sleep(0.25)
  ent()
  print("<::"+bcolors.TREE+"::>")
  time.sleep(0.25)
  print("Before you go, please try "+bcolors.OKMAG + 'Battling' + bcolors.ENDC+" that pile of sticks and leaves.")
  time.sleep(0.25)
  print("It will act as a dummy.")
  time.sleep(0.25)
  ent()
  battle(dummy)
  print("<::"+bcolors.TREE+"::>")
  time.sleep(0.25)
  print("Congratulations! You are now ready, however,")
  time.sleep(0.25)
  print("Keep in mind:")
  time.sleep(0.25)
  print(" - each location has its own raid, concluding with a battle with the location's King.")
  time.sleep(0.25)
  print(" - Upgrades are permanently gained from fragments of the rainbow key.") 
  time.sleep(0.25)
  print(" - Weapons are gifts of gratitiude from merchants in the area once a raid is completed.") 
  time.sleep(0.25)
  print("   - If you already have a weapon stronger than the one in that area, you wont recieve a new weapon") 
  time.sleep(0.25)
  print(" - Previous weapons cannot be re-equipped once replaced with a more powerful version.")
  time.sleep(0.25)
  print(" - If you lose, you will return to Bunny Fields(All upgrades and areas previously unlocked remain unlocked).")
  time.sleep(0.25)
  print(" - Each location's King has a different fragment of the key, defeat them all to assemble it.")
  time.sleep(0.25)
  print(" - Once you retrieve the key, return it to Rainbow Falls.")
  time.sleep(0.25)
  print("Good Luck! First, head to Bunny Fields.")
  ent()
  
def oldOak():
  print("<::Road to Old Oak::>")
def bunField():
  print("<::Road to Bunny Fields::>")