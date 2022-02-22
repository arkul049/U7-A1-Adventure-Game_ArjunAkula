
#name= [name & desc, health, attack, chance to dodge,
#probabilities are written as single digit integers, out of which a random number generator will pick a number of choices from.

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    OKRED = '\033[31m'
    OKMAG = '\033[35m'
    OKYEL = '\033[33m'
    OKBLACK = '\033[30;1m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENEMY = OKRED + 'Enemy' + ENDC
    PLAYER = OKBLUE + 'Player' + ENDC
    BATTLE = OKMAG + 'Battle HUD' + ENDC
    TREE = OKYEL + 'Great Oak' + ENDC
    FKING = OKRED + 'Fire King' + ENDC
    WKING = OKCYAN + 'Water King' + ENDC
    SKING = OKBLACK + 'Stone King' + ENDC
    WIN = BOLD + 'You Won!!'+ENDC
    LOSS = BOLD + 'You Lost!!'+ENDC

#100%
ten = [[True],["100%"]]
#90%
nine = [[True,True,True,True,True,True,True,True,True,False],["90%"]]
#80%
eight = [[True,True,True,True,False],["80%"]]
#60%
six = [[True,True,True,False,False],["60%"]]
#50%
five = [[True,False],["50%"]]
#30%
three = [[True,True,True,False,False,False,False,False,False,False],["30%"]]
#10%
one = [[True,False,False,False,False,False,False,False,False,False],["10%"]]
#0%
zero = [[False],["0%"]]

#Ancient Oak Enemies
dummy= [["Dummy", "Old Oak's offspring. Trees can't fight."],[24],[0],nine]

#Bunny Field Enemies
bunny= [["Bunny","A regular bunny."],[8],[2],six]
bigbunny= [["BIG Bunny", "This one got a little fat."],[16],[4],six]
bossbunny= [["BIGGEST Bunny","Did it . . . just eat another bunny!?"],[25],[12],eight]
#Blue Lake Enemies
minnow = [["Minnow","A small fish in a big pond. It wanted to leave home and now it has legs."],[15],[8],eight]
shark = [["Shark","These don't belong in freshwater . . . or on the surface."],[25],[15],eight]
waterKing = [[bcolors.WKING,"He's a whale with a crown, and feet. He hasn't evolved for the surface."],[50],[20],six]
#Scattered Cliffs Enemies
butterfly = [["Butterfly","It lost its way. Its accuracy however, is another story."],[15],[12],ten]
bird = [["Bird","It's looking for worms. Why is it looking at you?"],[25],[15],eight]
windKing = [["Wind King","A large bird with a crown. It sacrificed Accuracy for Power."],[50],[20],six]
#Coal Mines Enemies
fireLizard = [["Fire Lizard","A small lizard. It looks sick, but coughs out sparks."],[15],[12],eight]
golem = [["Golem","A mishmash of molten rock and metals, taking humanoid form."],[25],[15],six]
stoneKing = [[bcolors.SKING,"To regular golems combined into one. This one has a crown."],[50],[20],eight]
#Red Mountain Enemies
dragon = [["Dragon","A small dragon breathing large spouts of fire."],[20],[20],six]
fireKing = [[bcolors.FKING,"A giant dragon with a crown."],[40],[28],eight]
oldOak = [[bcolors.TREE,"His magic's strenght has increased tenfold. He can fight."],[80],[35],nine]