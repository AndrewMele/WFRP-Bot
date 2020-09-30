import random

natalia = ["Natalia", 33, 33, 29, 29, 23, 32, 30, 33, 30, 44]
luci = ["Luci", 33, 30, 40, 30, 29, 34, 29, 33, 40, 37]
char = ["Default", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  #selected character array

"""
How to change values

natalia[0] = "Character Name"  
natalia[1] = weaponskill
natalia[2] = ballisticskill
"""

#Testing Classes

class Character():
    def __init__(self, name, weaponskill, ballisticskill, strength, toughness, initiative, agility, dexterity, intelligence, willpower, fellowship):
        self.name = name
        self.weaponskill = weaponskill
        self.ballisticskill = ballisticskill
        self.strength = strength
        self.toughness = toughness
        self.initiative = initiative
        self.agility = agility
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.willpower = willpower
        self.fellowship = fellowship

    def function(self): #Will display the character you have selected and then replace the selected character array with the array of your chosen character
        print(self.name)
        characteristics = ("WS: {}, BS: {}, S: {}, T: {}, I: {}, Ag: {}, Dex: {}, Int: {}, WP: {}, Fel: {}")
        print(characteristics.format(self.weaponskill,self.ballisticskill, self.strength, self.toughness, self.initiative, self.agility, self.dexterity, self.intelligence, self.willpower, self.fellowship))
        char.clear()  #Where it replaces selected character array with the array of your chosen character
        char.append(self.name)
        char.append(self.weaponskill)
        char.append(self.ballisticskill)
        char.append(self.strength)
        char.append(self.toughness)
        char.append(self.initiative)
        char.append(self.agility)
        char.append(self.dexterity)
        char.append(self.intelligence)
        char.append(self.willpower)
        char.append(self.fellowship)

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

    def change(self):  #Changes Characteristics for the Selected Character. * WILL WORK ON MAKING IT CHANGE FOR BOTH ARRAYS *
        print("""Which characteristic would you like to replace?
        [WS]: Weapon Skill
        [BS: Ballistic Skill
        [S]: Strength
        [T]: Toughness
        [I]: Initiative
        [AG]: Agility
        [DEX]: Dexterity
        [INT]: Intelligence
        [WP]: Willpower
        [FEL]: Fellowship
        [ALL]: All""")
        x = input().upper()
        if x == "WS":
            ws = ("""Current WS: {} 
            what value would you like to replace it with?""")
            print(ws.format(self.weaponskill))
            x = input()
            char[1] = int(x)
        elif x == "BS":
            bs = ("""Current BS: {} 
            what value would you like to replace it with?""")
            print(ws.format(self.ballisticskill))
            x = input()
            char[2] = int(x)
        elif x == "S":
            s = ("""Current S: {} 
            what value would you like to replace it with?""")
            print(ws.format(self.strength))
            x = input()
            char[3] = int(x)
        elif x == "T":
            t = ("""Current T: {} 
            what value would you like to replace it with?""")
            print(ws.format(self.toughness))
            x = input()
            char[4] = int(x)
        elif x == "I":
            i = ("""Current I: {} 
            what value would you like to replace it with?""")
            print(ws.format(self.initiative))
            x = input()
            char[5] = int(x)
        elif x == "AG":
            ag = ("""Current Ag: {} 
            what value would you like to replace it with?""")
            print(ws.format(self.agility))
            x = input()
            char[6] = int(x)
        elif x == "DEX":
            dex = ("""Current Dex: {} 
            what value would you like to replace it with?""")
            print(ws.format(self.dexterity))
            x = input()
            char[7] = int(x)
        elif x == "INT":
            intel = ("""Current Int: {} 
            what value would you like to replace it with?""")
            print(ws.format(self.intelligence))
            x = input()
            char[8] = int(x)
        elif x == "WP":
            wp = ("""Current WP: {} 
            what value would you like to replace it with?""")
            print(ws.format(self.willpower))
            x = input()
            char[9] = int(x)
        elif x == "FEL":
            fel = ("""Current Fel: {} 
            what value would you like to replace it with?""")
            print(ws.format(self.fellowship))
            x = input()
            char[10] = int(x)
        elif x == "ALL":
            ws = ("""Current WS: {} 
            what value would you like to replace it with?""")
            print(ws.format(self.weaponskill))
            a = input()
            char[1] = int(a)
            bs = ("""Current BS: {} 
            what value would you like to replace it with?""")
            print(ws.format(self.ballisticskill))
            b = input()
            char[2] = int(b)
            s = ("""Current S: {} 
            what value would you like to replace it with?""")
            print(ws.format(self.strength))
            q = input()
            char[3] = int(q)
            t = ("""Current T: {} 
            what value would you like to replace it with?""")
            print(ws.format(self.toughness))
            d = input()
            char[4] = int(d)
            i = ("""Current I: {} 
            what value would you like to replace it with?""")
            print(ws.format(self.initiative))
            e = input()
            char[5] = int(e)
            ag = ("""Current Ag: {} 
            what value would you like to replace it with?""")
            print(ws.format(self.agility))
            f = input()
            char[6] = int(f)
            dex = ("""Current Dex: {} 
            what value would you like to replace it with?""")
            print(ws.format(self.dexterity))
            g = input()
            char[7] = int(g)
            intel = ("""Current Int: {} 
            what value would you like to replace it with?""")
            print(ws.format(self.intelligence))
            h = input()
            char[8] = int(h)
            wp = ("""Current WP: {} 
            what value would you like to replace it with?""")
            print(ws.format(self.willpower))
            j = input()
            char[9] = int(j)
            fel = ("""Current Fel: {} 
            what value would you like to replace it with?""")
            print(ws.format(self.fellowship))
            l = input()
            char[10] = int(l)


diz = Character(natalia[0], natalia[1], natalia[2], natalia[3], natalia[4], natalia[5], natalia[6], natalia[7], natalia[8], natalia[9], natalia[10])
vent = Character(luci[0], luci[1], luci[2], luci[3], luci[4], luci[5], luci[6], luci[7], luci[8], luci[9], luci[10])


def hub():
    print("""What would you like to do today?
    [C]hoose a Character
    [R]eplace characteristics/stats
    [H]it roll
    [Q]uit""")
    
    x = input().upper()
    if x == "C":
        choose()
    elif x == "R":
        c = Character(char[0], char[1], char[2], char[3], char[4], char[5], char[6], char[7],char[8],char[9],char[10])
        c.change()
    elif x == "H":
        c = Character(char[0], char[1], char[2], char[3], char[4], char[5], char[6], char[7],char[8],char[9],char[10])
        c.wsroll()
        hub()
    elif x == "Q":
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