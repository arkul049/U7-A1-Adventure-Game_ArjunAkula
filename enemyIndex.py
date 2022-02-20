#name= [name & desc, health, attack, chance to dodge,
#probabilities are written as single digit integers, out of which a random number generator will pick a number of choices from.

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
finBoss = [["Dummy", "Old Oak's offspring. Trees can't fight."],[24],[0],ten]

#Bunny Field Enemies
bunny= [["Bunny","A regular bunny."],[8],[2],six]

bigbunny= [["BIG Bunny", "This one got a little fat"],[16],[4],six]

bossbunny= [["BIGGEST Bunny","Did it . . . just eat another bunny!?"],[24],[8],eight]

#Blue Lake Enemies
minnow = [["Minnow","A small fish in a big pond. It wanted to leave home and now it has legs."],[15],[10],eight]

bigfish = [["Big Fish","A big fish in a small pond. It followed the minnows out of the water."],[25],[20],six]

shark = [["Shark","These don't belong in freshwater . . . or on the surface."],[30],[35],eight]

whale = [["Whale","It's a whale with feet. It's size hasn't evolved for the surface."],[80],[40],six]

#Scattered Cliffs Enemies
butterfly = [["Butterfly","It lost its way. Its accuracy however, is another story."],[10],[15],ten]

#Coal Mines Enemies
