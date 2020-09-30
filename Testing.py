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

def hub():
    print("""What would you like to do today?
    [C]hoose a Character
    [Q]uit""")
    
    y = input()
    if y == "C":
        choose()
    elif y == "Q":
        print("Thank you!  Have a nice day!")
    else:
        hub()
    

def choose():
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