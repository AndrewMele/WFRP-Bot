import random

z = random.randrange(1,11) #just using this to represent inputs since I do not know how to do them yet

natalia = ["Natalia", 24, 28]
luci = ["Luci", 30, 20]

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

    def function(self):
        print(self.name)
        characteristics = ("WS: {} , BS: {}")
        print(characteristics.format(self.weaponskill,self.ballisticskill))

diz = Character(natalia[0], natalia[1], natalia[2])
vent = Character(luci[0], luci[1], luci[2])


if z <= 5:
    diz.function()

else:
    vent.function()

"""
Dictionary Testing

characters = {
    "Natalia" : {
        "WeaponSkill" : ws,
        "BallisticSkill" : bs
    },
    "Luci" : {
        "WeaponSkill" : ws,
        "BallisticSkill" : bs
    }
}

if z<= 5:
    print("Natalia")
    print(characters["Natalia"])
 
else
    print("Luci")
    print(characters["Luci"])
"""
