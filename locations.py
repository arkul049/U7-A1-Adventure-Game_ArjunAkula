from battleLogic import *
from enemyIndex import *
import time

v=0
#old oak is 0, bun fields is 1, 2 is blue lake, 3 is caves, 4 is cliffs, and five is red mountain

def title():
  """
  Prints game title.
  """
  print("Rainbow Falls")
  time.sleep(1)
  ent()
def tutorial():
  """
  Prints introduction to game at time intervals.
  """
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
  print("Traveling to any location will let you battle that location's unique enemies, but at the end, you will return to Bunny Fields. Bunny Fields, however, is complete.")
  time.sleep(0.25)
  print("Since in its current state, this game is just a battle sim, (and a lacking one at that), go into player.py and edit origStats[1] to increase attack (80 is most you'll need) for testing other functionality")
  time.sleep(0.25)
  print("There are a number of bosses in the game, but only the boss for Bunny Fields can be accessed at the end of the Raid. ")
  # print(" - Each location's King has a different fragment of the key, defeat them all to assemble it.")
  # time.sleep(0.25)
  # print(" - Once you retrieve the key, return it to Rainbow Falls.")
  time.sleep(0.25)
  print("Good Luck! First, head to Bunny Fields.")
  ent()
  return
  
def oldOak():
  """
  Prints relevent location Information.\n
  Returns:\n
  Assorted integers relative to chosen next location.
  (currently only 1)
  """
  print("<::Road to "+bcolors.TREE+"::>")
  time.sleep(0.25)
  print(". . .")
  time.sleep(0.25)
  print("You've already arrived! It wasn't that far.")
  ent()
  print("Unfortunatley, this area's under construction.")
  time.sleep(0.25)
  print("<Returning to Bunny Fields>")
  ent()
  return 1
  
# def oldOakLoc():
#   screen_clear()
#   print("<Old Oak>\n")
#   print("<Bunny Fields(b)>")
#   print("<Rainbow Falls(r)>")
#   t = input("<::"+bcolors.PLAYER+"::>")
#   if(t == 'b'):
#     return 2
#   elif(t == 'r'):
#     print("Not Implemented . . . ")
#     ent()
#     OldOakLoc()
#   else:
#     OldOakLoc()
  
def bunLoc(x):
    """
  Prints relevent location Information.\n
  Arguments:\n
  x: whether or not raid has been completed at least once
  Returns:\n
  Assorted integers relative to chosen next location.
    """
    global v
    screen_clear()
    if v == 0:
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
        v=1
        bunLoc(v)
      elif t == 'o':
        return 0
      else:
        bunLoc(v)
    else:
      print("<Bunny Fields>\n")
      print("<Old Oak(o)>")
      print("<Blue Lake(b)>")
      print("<Crystal Caves(c)>")
      print("<Howling Cliffs(h)>")
      print("<Quit(q)>")
      t = input("<::"+bcolors.PLAYER+"::>")
      if(t == 'o'):
        return 0
      elif(t == 'b'):
        return 2
      elif(t == 'c'):
        return 3
      elif(t == 'q'):
        return 6
      else:
        bunLoc(v)
        
def bunField():
  """
  Prints relevent location Information.\n
  Returns:\n
  Assorted integers relative to chosen next location.
    """
  randEnc = ["You stop and smell the roses.","The sun is shining.", "There isn't a cloud in the sky.","Lush green fields stretch into the distance, you can't see them end."]
  for i in range(2):
    screen_clear()
    print("<::Road to Bunny Fields::>")
    time.sleep(0.25)
    print(random.choice(randEnc))
    time.sleep(0.25)
    ent()
    time.sleep(0.25)
    if(random.randint(0, 1) == 1):
      battle(bunny)
    else:
      battle(bigbunny)
  print("You've arrived.")
  ent()
  return bunLoc(v)

  
def blueLake():
  """
  Prints relevent location Information.\n
  Returns:\n
  Assorted integers relative to chosen next location.
    """
  print("<::Road to Blue Lake::>")
  time.sleep(0.25)
  print(". . .")
  time.sleep(0.25)
  randEnc = ["You see a lake in the distance.","There are shadows underneath the lake's surface.", "Its raining.","Is that a fish . . . with legs!?"]
  for i in range(2):
    screen_clear()
    print("<::Road to Blue Lake::>")
    time.sleep(0.25)
    print(random.choice(randEnc))
    time.sleep(0.25)
    ent()
    time.sleep(0.25)
    if(random.randint(0, 1) == 1):
      battle(minnow)
    else:
      battle(shark)
  print("You've arrived to Blue Lake.")
  time.sleep(0.25)
  print("<Bunny Fields(any input)>")
  time.sleep(0.25)
  print("<Crystal Caves(c)>")
  time.sleep(0.25)
  print("<Howling Cliffs(h)>")
  time.sleep(0.25)
  print("<Quit(q)>")
  time.sleep(0.25)
  t = input("<::"+bcolors.PLAYER+"::>")
  if(t == 'c'):
    return 3
  elif(t == 'h'):
    return 4
  elif(t == 'q'):
    return 6
  else:
    bunLoc(v)  
  
def crysCav():
  """
  Prints relevent location Information.\n
  Returns:\n
  Assorted integers relative to chosen next location.
    """
  print("<::Road to Crystal Caverns::>")
  time.sleep(0.25)
  print(". . .")
  time.sleep(0.25)
  randEnc = ["The ground is shaking.","The rocks are alive.", "This mineshaft seems abandoned . . .","You see small pools of lava."]
  for i in range(2):
    screen_clear()
    print("<::Road to Crystal Caverns::>")
    time.sleep(0.25)
    print(random.choice(randEnc))
    time.sleep(0.25)
    ent()
    time.sleep(0.25)
    if(random.randint(0, 1) == 1):
      battle(fireLizard)
    else:
      battle(golem)
  print("You've arrived to Crystal Caverns.")
  time.sleep(0.25)
  print("<Bunny Fields(any input)>")
  time.sleep(0.25)
  print("<Blue Lake(b)>")
  time.sleep(0.25)
  print("<Howling Cliffs(h)>")
  time.sleep(0.25)
  print("<Quit(q)>")
  time.sleep(0.25)
  t = input("<::"+bcolors.PLAYER+"::>")
  if(t == 'b'):
    return 2
  elif(t == 'h'):
    return 4
  elif(t == 'q'):
    return 6
  else:
    bunLoc(v)
      
def howCliff():
  """
  Prints relevent location Information.\n
  Returns:\n
  Assorted integers relative to chosen next location.
    """
  print("<::Road to Howling Cliffs::>")
  time.sleep(0.25)
  print(". . .")
  time.sleep(0.25)
  randEnc = ["The wind is blowing.","You hear bird calls overhead.", "There are flickering shapes in the sky.","The ground around you is dissappearing."]
  for i in range(2):
    screen_clear()
    print("<::Road to Howling Cliffs::>")
    time.sleep(0.25)
    print(random.choice(randEnc))
    time.sleep(0.25)
    ent()
    time.sleep(0.25)
    if(random.randint(0, 1) == 1):
      battle(butterfly)
    else:
      battle(bird)
  print("You've arrived to Howling Cliffs.")
  time.sleep(0.25)
  print("<Crystal Caverns(c)>")
  time.sleep(0.25)
  print("<Blue Lake(b)>")
  time.sleep(0.25)
  print("<Red Mountain(Any Input)>")
  time.sleep(0.25)
  print("<Quit(q)>")
  time.sleep(0.25)
  t = input("<::"+bcolors.PLAYER+"::>")
  if(t == 'b'):
    return 2
  elif(t == 'c'):
    return 3
  elif(t == 'q'):
    return 6
  else:
    return 5
      
def redMoun():
  """
  Prints relevent location Information.\n
  Returns:\n
  Assorted integers relative to chosen next location.
    """
  print("<::Road to Red Mountain::>")
  time.sleep(0.25)
  print(". . .")
  time.sleep(0.25)
  randEnc = ["Molten rock pours down the slopes.","The air is toxic", "Sparks and fire illuminate the obsidian.","You hear a loud roar"]
  for i in range(2):
    screen_clear()
    print("<::Road to Red Mountains::>")
    time.sleep(0.25)
    print(random.choice(randEnc))
    time.sleep(0.25)
    ent()
    time.sleep(0.25)
    if(random.randint(0, 1) == 1):
      battle(fireLizard)
    else:
      battle(dragon)
  print("You've arrived to Red Mountain.")
  time.sleep(0.25)
  print("<Howling Peak(Any Input)>")
  time.sleep(0.25)
  print("<Quit(q)>")
  time.sleep(0.25)
  t = input("<::"+bcolors.PLAYER+"::>")
  if(t == 'q'):
    return 6
  else:
    return 4
      
# def rainFall():
#   print("<::Road to Rainbow Falls::>")
#   time.sleep(0.25)
#   print(". . .")
#   time.sleep(0.25)
#   print("You've already arrived to Rainbow Falls! It wasn't that far.")
#   ent()
#   print("unfortunatley, this area is underconstruction, please come back another time . . .")
#   time.sleep(0.25)
#   print("<Returning to Bunny Fields>")
#   ent()
#   return 1

def Loc(x):
  """
  Picks location func call depending on parameter "x"\n
  Arguments:\n
  x: number chosing location to travel (returned from location funcs)
  Returns:\n
  Assorted integers relative to chosen next location.
    """
  if x == 0:
    return oldOak()
  elif x == 1:
    return bunLoc(v)
  elif x == 2:
    return blueLake()
  elif x == 3:
    return crysCav()
  elif x == 4:
    return howCliff()
  elif x == 5:
    return redMoun()
  elif x == 6:
    return 6
  else:
    return bunLoc(v)
    
def locMan(x):
  """
  Calls Loc func to update "x"\n
  Arguments:\n
  x: number chosing location to travel (returned from location funcs)
    """
  while(True):
    x = Loc(x)
    if x == 6:
      break
  print("Thanks for playing. The game is obviously still in development, but I will hopefully complete it for my final project . . . (To be continued?)")
  return