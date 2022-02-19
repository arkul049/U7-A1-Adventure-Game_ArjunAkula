import random
import time
import math
import os
from player import *
from enemyIndex import *
import copy


def updatePlayer():
  variStats = copy.deepcopy(origStats)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    OKRED = '\033[31m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENEMY = '\033[31m'+'Enemy'+'\033[0m'
    PLAYER = '\033[94m'+'Player'+'\033[0m'
    BATTLE = '\u001b[35m'+'Battle Hud'+ENDC

def ent():
  input("<Continue(enter)>")

def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

def screen_clear():
   # for mac and linux(here, os.name is 'posix')
  """
  Clears screen.
  """
  if os.name == 'posix':
    os.unsetenv('LD_PRELOAD')
    _ = os.system('clear')
  else:
    # for windows platfrom
    _ = os.system('cls')
#Battle
def land(x):
  """
  Decided whether attack lands or not.\n
  Args:\n
  x: list (for original enemy Acc, from cloned list)\n
  Returns:\n
  True/False: if attack lands or not
  
  """
  temp = random.choices(x[3][0])[0]
  return temp

def pLand():
  """
  Decided whether Player's attack lands or not.\n
  Args:\n
  x: list (for original enemy Acc, from cloned list)\n
  Returns:\n
  True/False: if attack lands or not
  
  """
  temp = random.choices(variStats[2][0])[0]
  return temp

def dispbat(y,x):
  """
  Function displays battle screen, enemies health, and your health.\n
  Args:\n
  x: list (for current enemy health, from cloned list)
  y: list (for original enemy health from original list)\n
  Returns:\n
  0: returning after every turn
  """
  disH(y,x)
  print("\n<::"+bcolors.BATTLE+"::>")
  return atkHub(y,x)


def atkHub(y,x):
  """
  Handles player options in battle.\n
  Args:\n
  t: input(any one of player's battle options)\n
  Returns:\n
  True/False: if next enemy attack will be blocked or not
  """
    #handles all combat options
  time.sleep(0.25)
  print("<Use(u)>")
  time.sleep(0.125)
  print("<Block(b)>")
  time.sleep(0.125)
  print("<Stats "+bcolors.PLAYER+"/"+bcolors.ENEMY+"(p/e)>")
  time.sleep(0.125)
  t = input("<::"+bcolors.PLAYER+"::>")
  if t== "p":
    stats1()
    dispbat(y,x)
  elif t == "e":
    stats(y)
    dispbat(y,x)
  elif (t == "u"):
    if(pLand()):
      use(y)
    else:
      print("Attack Missed!")
    return False
  elif(t == "b"):
    t = block()
    print("You attempted to Block!")
    return t
    
      
def stats(y):
  screen_clear()
  print("<"+bcolors.ENEMY+" Stats:>")
  time.sleep(0.25)
  print("HP["+str(y[1][0])+"]")
  time.sleep(0.25)
  print("ATTK["+str(y[2][0])+"]")
  time.sleep(0.25)
  print("ACC["+str(y[3][1][0])+"]")
  time.sleep(0.25)
  ent()
  return
  
def stats1():
  screen_clear()
  print("<Stats:>")
  time.sleep(0.25)
  print("HP["+str(variStats[0])+"]")
  time.sleep(0.25)
  print("ATTK["+str(variStats[1])+"]")
  time.sleep(0.25)
  print("ACC["+str(variStats[2][1][0])+"]")
  time.sleep(0.25)
  ent()
  return
  

def use(y):
    #attacks, base does 5% player hp dmg to enemy, goes up with tools
  if(variStats[1][0] != "h"):
    y[1][0]-=int(variStats[1])
    time.sleep(0.25)
    print("Attack Landed!")
    time.sleep(0.25)
    print("Your", namestr(variStats[1],globals())[0],"did", variStats[1],"points of DMG!")
  else:
    time.sleep(0.25)
    variStats[0]+= int(variStats[1][4:6])
    print("Healed by",str(variStats[1][4:6])+"HP!")

def block():
  """
  3/4 chance to block 3/4 attack
  """
  return random.choices([True,True, True, True, False])[0]
    
def encounter(x):
  screen_clear()
  print("<::You encountered a",str(x[0][0])+"::>")
  time.sleep(0.75)
  print(x[0][1])
  time.sleep(0.75)
  print("<Stats:>")
  time.sleep(0.25)
  print("HP["+str(x[1][0])+"]")
  time.sleep(0.25)
  print("ATTK["+str(x[2][0])+"]")
  time.sleep(0.25)
  print("ACC["+str(x[3][1][0])+"]")
  time.sleep(0.25)
  print("...\n")
  time.sleep(0.75)
  print("Good Luck!!")
  time.sleep(0.25)
  ent()
  return x

def disH(y,x):
  screen_clear()
  print("<::"+bcolors.OKRED+str(y[0][0])+bcolors.ENDC+"::>")
  temp = round(10*(y[1][0]/x[1][0]))
  temp1 = round(10*(variStats[0]/origStats[0]))
  print("HP["+bcolors.OKGREEN+"="*temp+bcolors.ENDC+" "*(10-temp)+"]")
  print("\n")
  print("<::"+bcolors.PLAYER+"::>")
  print("HP["+bcolors.OKGREEN+"="*temp1+bcolors.ENDC+" "*(10-temp1)+"]")

def enemyAttack(x,y):
  #20% chance of deciding to wait
  if(x != 0):
    if(random.choices([True,True,True,True,True,True,True,False,False,False])[0]): 
      time.sleep(0.25)
      print(bcolors.ENEMY+" Attacked . . .")
      time.sleep(0.25)
      print(bcolors.ENEMY+" was Blocked!")
      return
  elif(random.choices([True,True, True, True, False])[0]):
    time.sleep(0.25)
    print(bcolors.ENEMY+" Attacked . . .")
    if(land(y)):
      time.sleep(0.25)
      t = int(y[2][0])
      print(bcolors.ENEMY+" did", str(t),"points of DMG!")
      variStats[0] -= t
    else:
      time.sleep(0.25)
      print(bcolors.ENEMY+" Missed!")
      return
  else:
    time.sleep(0.25)
    print(bcolors.ENEMY+" is Waiting . . . (It didn't attack)")
  return

def battle(x):
  """
  Updates variPlayer with current stats depending on inventory. Clones enemy list for variable changes. Handles calling functions until player varihealth 0 or cloned enemy health = 0.\n
  Args:\n
  x: list(original enemy list)\n
  y: list (cloned enemy list)\n

  Returns:\n
  True or False: Win or Loss
  """
  screen_clear()
  #creates instance of enemy to compare to original enemy list
  y= copy.deepcopy(encounter(x))
  while(True):
    t = dispbat(y,x)
    if(t and y[1][0] > 0):
      time.sleep(0.5)
      print("<::"+bcolors.ENEMY+"::>")
      enemyAttack(1,y)
    else:
      time.sleep(0.5)
      print("<::"+bcolors.ENEMY+"::>")
      enemyAttack(0,y)
    time.sleep(0.25)
    ent()
    if(y[1][0] <= 0 or variStats[0] <= 0):
      break
  disH(y,x)
  if(variStats[0] <= 0):
    print("\n<::"+bcolors.BATTLE+"::>")
    print("You Lost!")
  elif(y[1][0] <= 0):
    print("\n<::"+bcolors.BATTLE+"::>")
    print("You Won!")
    ent()
    updatePlayer()
    screen_clear()
    return
      
        

  
