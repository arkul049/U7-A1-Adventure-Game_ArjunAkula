from battleLogic import *
from enemyIndex import *
import time

#old oak is 0, bun fields is 1, 2 is blue lake, 3 is caves, 4 is cliffs, and five is red mountain

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
  print("Before you go, please try "+bcolors.OKMAG + 'Battling' + bcolors.ENDC+" that pile of sticks and leaves. It will act as a dummy.")
  time.sleep(0.25)
  print("When you are prompted with '<::Player::>', enter your input and then click enter to make a move.")
  time.sleep(0.25)
  ent()
  battle(dummy)
  print("<::"+bcolors.TREE+"::>")
  time.sleep(0.25)
  print("Congratulations! You are now ready, however,")
  time.sleep(0.25)
  print("Keep in mind:")
  time.sleep(0.25)
  # print(" - each location has its own raid, concluding with a battle with the location's King.")
  # time.sleep(0.25)
  # print(" - Upgrades are permanently gained from regular battles and fragments of the rainbow key.") 
  # time.sleep(0.25)
  # print(" - Rainbow Key shards are gifts of gratitiude from merchants in the area once a raid is completed.")
  # time.sleep(0.25)
  # print(" - If you lose, you will return to Bunny Fields(All upgrades and areas previously unlocked remain unlocked).")
  print("Game is incomplete, so locations other than bunny fields arent complete, but playable. For examples of functions with paramenters, check out the battleLogic file!")
  time.sleep(0.25)
  print(" - Each location's King has a different fragment of the key, defeat them all to assemble it.")
  time.sleep(0.25)
  print(" - Once you retrieve the key, return it to Rainbow Falls.")
  time.sleep(0.25)
  print("Good Luck! First, head to Bunny Fields.")
  ent()
  return
  
def oldOak():
  print("<::Road to "+bcolors.TREE+"::>")
  time.sleep(0.25)
  print(". . .")
  time.sleep(0.25)
  print("You've already arrived! It wasn't that far.")
  ent()
  return OldOakLoc()
  
def oldOakLoc():
  screen_clear()
  print("<Old Oak>\n")
  print("<Bunny Fields(b)>")
  print("<Rainbow Falls(r)>")
  t = input("<::"+bcolors.PLAYER+"::>")
  if(t == 'b'):
    return 2
  elif(t == 'r'):
    print("Not Implemented . . . ")
    ent()
    OldOakLoc()
  else:
    OldOakLoc()
  
def bunLoc(x):
    screen_clear()
    if x == 0:
      print("<Bunny Fields>")
      print("<Raid(r)>")
      print("<Old Oak(o)>")
      t = input("<::"+bcolors.PLAYER+"::>")
      if t == 'r':
        print("Help! An invasive species of rabbit has taken over our fields!")
        ent()
        for i in range(2):
          screen_clear()
          print("<Raid Floor 1>")
          battle(bunny)
        screen_clear()
        print("<Raid Floor 2>")
        battle(bigbunny)
        screen_clear()
        print("<Final Boss>")
        battle(bossbunny)
        print("Thank you for defeating the bunnies! You can now access other locations.")
        ent()
        bunLoc(1)
      elif t == 'o':
        return 0
      else:
        bunLoc(0)
    else:
      print("<Bunny Fields>\n")
      print("<Old Oak(o)>")
      print("<Blue Lake(b)>")
      print("<Crystal Caves(c)>")
      print("<Howling Cliffs(h)>")
      t = input("<::"+bcolors.PLAYER+"::>")
      if(t in ['o','b','c','h']):
        if(t == 'o'):
          return 0
        elif(t == 'b'):
          return 2
        elif(t == 'c'):
          return 3
        elif(t == 'h'):
          return 5
      else:
        bunLoc(1)
        
def bunField():
  randEnc = ["You stop and smell the roses.","The sun is shining.", "There isn't a cloud in the sky.","Lush green fields stretch into the distance, you can't see them end."]
  for i in range(3):
    screen_clear()
    print("<::Road to Bunny Fields::>")
    time.sleep(0.25)
    print(random.choice(randEnc))
    time.sleep(0.25)
    ent()
    time.sleep(0.25)
    if(random.choice(six)[0]):
      battle(bunny)
    else:
      battle(bigbunny)
  print("You've arrived.")
  ent()
  return bunLoc(0)

  
def blueLake():
  randEnc = []
  print("<::Road to Blue Lake::>")
  time.sleep(0.25)
  print(". . .")
  time.sleep(0.25)
  randEnc = ["You see a lake in the distance.","There are shadows underneath the lake's surface.", "Its raining.","Is that a fish . . . with legs!?"]
  for i in range(3):
    screen_clear()
    print("<::Road to Blue Lake::>")
    time.sleep(0.25)
    print(random.choice(randEnc))
    time.sleep(0.25)
    ent()
    time.sleep(0.25)
    if(random.choice(six)[0]):
      battle(minnow)
    else:
      battle(shark)
  print("You've arrived.")
  ent()
  print("unfortunatley, this area is underconstruction, please come back another time . . .")
  ent()
  return 1
  
def crysCav():
  randEnc = []
  print("<::Road to Crystal Caverns::>")
  time.sleep(0.25)
  print(". . .")
  time.sleep(0.25)
  randEnc = ["The ground is shaking.","The rocks are alive.", "This mineshaft seems abandoned . . .","You see small pools of lava."]
  for i in range(3):
    screen_clear()
    print("<::Road to Crystal Caverns::>")
    time.sleep(0.25)
    print(random.choice(randEnc))
    time.sleep(0.25)
    ent()
    time.sleep(0.25)
    if(random.choice(six)[0]):
      battle(fireLizard)
    else:
      battle(golem)
  print("You've arrived.")
  ent()
  print("unfortunatley, this area is underconstruction, please come back another time . . .")
  ent()
  return 1
      
def howCliff():
  randEnc = []
  print("<::Road to Howling Cliffs::>")
  time.sleep(0.25)
  print(". . .")
  time.sleep(0.25)
  randEnc = ["The wind is blowing.","You hear bird calls overhead.", "There are flickering shapes in the sky.","The ground around you is dissappearing."]
  for i in range(3):
    screen_clear()
    print("<::Road to Howling Cliffs::>")
    time.sleep(0.25)
    print(random.choice(randEnc))
    time.sleep(0.25)
    ent()
    time.sleep(0.25)
    if(random.choice(six)[0]):
      battle(butterfly)
    else:
      battle(bird)
  print("You've arrived.")
  ent()
  print("unfortunatley, this area is underconstruction, please come back another time . . .")
  ent()
  return 1
      
def redMoun():
  randEnc = []
  print("<::Road to Red Mountain::>")
  time.sleep(0.25)
  print(". . .")
  time.sleep(0.25)
  randEnc = ["Molten rock pours down the slopes.","The air is toxic", "Sparks and fire illuminate the obsidian.","You hear a loud roar"]
  for i in range(3):
    screen_clear()
    print("<::Road to Red Mountains::>")
    time.sleep(0.25)
    print(random.choice(randEnc))
    time.sleep(0.25)
    ent()
    time.sleep(0.25)
    if(random.choice(six)[0]):
      battle(fireLizard)
    else:
      battle(dragon)
  print("You've arrived.")
  ent()
  print("unfortunatley, this area is underconstruction, please come back another time . . .")
  ent()
  return 1
      
def rainFall():
  print("<::Road to Rainbow Falls::>")
  time.sleep(0.25)
  print(". . .")
  time.sleep(0.25)
  print("You've already arrived! It wasn't that far.")
  ent()
  print("unfortunatley, this area is underconstruction, please come back another time . . .")
  ent()
  return 1

def Loc(x):
  if x == 0:
    return oldOak()
  elif x == 1:
    return bunField()
  elif x == 2:
    return blueLake()
  elif x == 3:
    return crysCav()
  elif x == 4:
    return howCliff()
  elif x == 5:
    return howCliff()
  else:
    return bunLoc(1)
    
def locMan(x):
  print("use Loc func")