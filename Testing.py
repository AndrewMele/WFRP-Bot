import random

natalia = ["Natalia", 24, 28]
luci = ["Luci", 30, 20]
char = ["Default", 0, 0]  #selected character array

"""
How to change values

natalia[0] = "Character Name"  
natalia[1] = weaponskill
natalia[2] = ballisticskill
"""

#Testing Classes, even though I could just simplify it down.

class Character():
    def __init__(self, name, weaponskill, ballisticskill):
        self.name = name
        self.weaponskill = weaponskill
        self.ballisticskill = ballisticskill

    def function(self): #Will display the character you have selected and then replace the selected character array with the array of your chosen character
        print(self.name)
        characteristics = ("WS: {} , BS: {}")
        print(characteristics.format(self.weaponskill,self.ballisticskill))
        char.clear()  #Where it replaces selected character array with the array of your chosen character
        char.append(self.name)
        char.append(self.weaponskill)
        char.append(self.ballisticskill)

    def wsroll(self): #Will do a basic WeaponSkill roll for the selected character
        z = random.randrange(1, 101)
        sl = (self.weaponskill - z)/10
        r = ("You rolled {}.")
        print(r.format(z))
        if z <= self.weaponskill:
            hit = ("You Hit by {} SLs!")
            print(hit.format(sl))
        else:
            hit = ("You Miss by {} SLs!")
            print(hit.format(sl))
    
        

diz = Character(natalia[0], natalia[1], natalia[2])
vent = Character(luci[0], luci[1], luci[2])



def hub():
    print("""What would you like to do today?
    [C]hoose a Character
    [R]oll
    [Q]uit""")
    
    y = input().upper()
    if y == "C":
        choose()
    elif y =="R":
        c = Character(char[0],char[1],char[2])
        c.wsroll()
        hub()
    elif y == "Q":
        print("Thank you!  Have a nice day!")
    else:
        hub()
    
    
def choose(): #Choose which character to play.  Will be replaced with checking the user on discord and automatically assigning the character.
    print("""Which character would you like to play?
    [1] Natalia
    [2] Luci""")
    x = input()
    if x == "1":
        diz.function()
    elif x =="2":
        vent.function()    
    hub()

hub()