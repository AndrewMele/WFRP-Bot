import random

natalia = ["Natalia", 33, 33, 29, 29, 23, 32, 30, 33, 30, 44]
basic_nat_skill = [0, 0, 5, 6, 0, 0, 3, 5, 0, 0, 0, 0, 5, 10, 10, 10, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0]
luci = ["Luci", 33, 30, 40, 30, 29, 34, 29, 33, 40, 37]
basic_luc_skill = [0, 0, 0, 5, 0, 0, 10, 0, 0, 0, 10, 0, 0, 2, 5, 10, 0, 3, 5, 0, 0, 0, 0, 0, 0, 0]
char = ["Default", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  #Current Character Characteristics Array
basic_char_skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #Current Character Basic Skill Array


#Testing Classes

class CharacterStats():
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
        print(f"WS: {self.weaponskill}, BS: {self.ballisticskill}, S: {self.strength}, T: {self.toughness}, I: {self.initiative}, Ag: {self.agility}, Dex: {self.dexterity}, Int: {self.intelligence}, WP: {self.willpower}, Fel: {self.fellowship}")
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

    def changestat(self):  #Changes Characteristics for the Selected Character. * WILL WORK ON MAKING IT CHANGE FOR BOTH ARRAYS *
        print("""
        Which characteristic would you like to replace?

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
        [ALL]: All
        [Q]: Quit
        """)
        x = input().upper()
        if x == "WS":
            print(f"Current WS: {self.weaponskill}\nWhat value would you like to replace it with?\n")
            x = input()
            char[1] = int(x)
        elif x == "BS":
            print(f"Current BS: {self.ballisticskill}\nWhat value would you like to replace it with?\n")
            x = input()
            char[2] = int(x)
        elif x == "S":
            print(f"Current S: {self.strength}\nWhat value would you like to replace it with?\n")
            x = input()
            char[3] = int(x)
        elif x == "T":
            print(f"Current T: {self.toughness}\nWhat value would you like to replace it with?\n")
            x = input()
            char[4] = int(x)
        elif x == "I":
            print(f"Current I: {self.initiative}\nWhat value would you like to replace it with?\n")
            x = input()
            char[5] = int(x)
        elif x == "AG":
            print(f"Current Ag: {self.agility}\nWhat value would you like to replace it with?\n")
            x = input()
            char[6] = int(x)
        elif x == "DEX":
            print(f"Current Dex: {self.dexterity}\nWhat value would you like to replace it with?\n")
            x = input()
            char[7] = int(x)
        elif x == "INT":
            print(f"Current Int: {self.intelligence}\nWhat value would you like to replace it with?\n")
            x = input()
            char[8] = int(x)
        elif x == "WP":
            print(f"Current WP: {self.willpower}\nWhat value would you like to replace it with?\n")
            x = input()
            char[9] = int(x)
        elif x == "FEL":
            print(f"Current Fel: {self.fellowship}\nWhat value would you like to replace it with?\n")
            x = input()
            char[10] = int(x)
        elif x == "ALL":
            print("WS")
            x = input()
            char[1] = int(x)
            print("BS")
            x = input()
            char[2] = int(x)
            print("S")
            x = input()
            char[3] = int(x)
            print("T")
            x = input()
            char[4] = int(x)
            print("I")
            x = input()
            char[5] = int(x)
            print("Ag")
            x = input()
            char[6] = int(x)
            print("Dex")
            x = input()
            char[7] = int(x)
            print("Int")
            x = input()
            char[8] = int(x)
            print("WP")
            x = input()
            char[9] = int(x)
            print("Fel")
            x = input()
            char[10] = int(x)
        print("""Is there another value you would like to replace?
        [Y]: Yes
        [N]: No
        """)
        x=input().upper()
        if x == "Y":
            changestat()


class CharacterBasicSkills():
    def __init__(self, art, athletics, bribery, charm, charm_animal, climb, cool, consume_alcohol, dodge, drive, endurance, entertain, gamble, gossip, haggle, intimidate, intuition, leadership, melee_basic, melee_other, navigation, outdoor_survival, perception, ride, row, stealth):
        self.art = art
        self.athletics = athletics
        self.bribery = bribery
        self.charm = charm
        self.charm_animal = charm_animal
        self.climb = climb
        self.cool = cool
        self.consume_alcohol = consume_alcohol
        self.dodge = dodge
        self.drive = drive
        self.endurance = endurance
        self.entertain = entertain
        self.gamble = gamble
        self.gossip = gossip
        self.haggle = haggle
        self.intimidate = intimidate
        self.intuition = intuition
        self.leadership = leadership
        self.melee_basic = melee_basic
        self.melee_other = melee_other
        self.navigation = navigation
        self.outdoor_survival = outdoor_survival
        self.perception = perception
        self.ride = ride
        self.row = row
        self.stealth = stealth

    def function(self): #Will display the character you have selected and then replace the selected character array with the array of your chosen character
        print(f"""
        Art: {self.art}                    Athletics: {self.athletics}
        Bribery: {self.bribery}                Charm: {self.charm}
        Charm Animal: {self.charm_animal}           Climb: {self.climb}
        Cool: {self.cool}                   Consume Alcohol: {self.consume_alcohol}
        Dodge: {self.dodge}                  Drive: {self.drive}
        Endurance: {self.endurance}              Entertain: {self.entertain}
        Gamble: {self.gamble}                 Gossip: {self.gossip}
        Haggle: {self.haggle}                Intimidate: {self.intimidate}
        Intuition: {self.intuition}              Leadership: {self.leadership}
        Melee(Basic): {self.melee_basic}           Melee(Other): {self.melee_other}
        Navigate: {self.navigation}               Outdoor Survival: {self.outdoor_survival}
        Perception: {self.perception}             Ride: {self.ride}
        Row: {self.row}                    Stealth: {self.stealth}
        """)
        basic_char_skill.clear()
        basic_char_skill.append(self.art)
        basic_char_skill.append(self.athletics)
        basic_char_skill.append(self.bribery)
        basic_char_skill.append(self.charm)
        basic_char_skill.append(self.charm_animal)
        basic_char_skill.append(self.climb)
        basic_char_skill.append(self.cool)
        basic_char_skill.append(self.consume_alcohol)
        basic_char_skill.append(self.dodge)
        basic_char_skill.append(self.drive)
        basic_char_skill.append(self.endurance)
        basic_char_skill.append(self.entertain)
        basic_char_skill.append(self.gamble)
        basic_char_skill.append(self.gossip)
        basic_char_skill.append(self.haggle)
        basic_char_skill.append(self.intimidate)
        basic_char_skill.append(self.intuition)
        basic_char_skill.append(self.leadership)
        basic_char_skill.append(self.melee_basic)
        basic_char_skill.append(self.melee_other)
        basic_char_skill.append(self.navigation)
        basic_char_skill.append(self.outdoor_survival)
        basic_char_skill.append(self.perception)
        basic_char_skill.append(self.ride)
        basic_char_skill.append(self.row)
        basic_char_skill.append(self.stealth)
    
    def changebskill(self):
        print("""
        Which Basic Skill Advancements would you like to change?

        [ART]: Art
        [ATH]: Athletics
        [BRI]: Bribery
        [CHA]: Charm
        [ANI]: Charm Animal
        [CLI]: Climb
        [COO]: Cool
        [CON]: Consume Alcohol
        [DOD]: Dodge
        [DRI]: Drive
        [END]: Endurance
        [ENT]: Entertain
        [GAM]: Gamble
        [GOS]: Gossip
        [HAG]: Haggle
        [TIM]: Intimidate
        [TUI]: Intuition
        [LEA]: Leadership
        [MEB]: Melee(Basic)
        [MEO]: Melee(Other)
        [NAV]: Navigation
        [ODS]: Outdoor Survival
        [PER]: Perception
        [RID]: Ride
        [ROW]: Row
        [STE]: Stealth
        [ALL]: Change all Basic Skill Advancements
        [Q]: Quit
        """)
        x=input().upper()
        if x == "ART":
            print(f"""Current Art Advancements: {self.art}
            What value would you like to replace it with?""")
            x = input()
            basic_char_skill[0] = int(x)
        elif x == "ATH":
            print(f"""Current Athletics Advancements: {self.athletics}
            What value would you like to replace it with?""")
            x = input()
            basic_char_skill[1] = int(x)
        elif x == "BRI":
            print(f"""Current Bribery Advancements: {self.bribery}
            What value would you like to replace it with?""")
            x = input()
            basic_char_skill[2] = int(x)
        elif x == "CHA":
            print(f"""Current Charm Advancements: {self.charm}
            What value would you like to replace it with?""")
            x = input()
            basic_char_skill[3] = int(x)
        elif x == "ANI":
            print(f"""Current Charm Animal Advancements: {self.charm_animal}
            What value would you like to replace it with?""")
            x = input()
            basic_char_skill[4] = int(x)
        elif x == "CLI":
            print(f"""Current Climb Advancements: {self.climb}
            What value would you like to replace it with?""")
            x = input()
            basic_char_skill[5] = int(x)
        elif x == "COO":
            print(f"""Current Cool Advancements: {self.cool}
            What value would you like to replace it with?""")
            x = input()
            basic_char_skill[6] = int(x)
        elif x == "CON":
            print(f"""Current Consume Alcohol Advancements: {self.consume_alcohol}
            What value would you like to replace it with?""")
            x = input()
            basic_char_skill[7] = int(x)
        elif x == "DOD":
            print(f"""Current Dodge Advancements: {self.dodge}
            What value would you like to replace it with?""")
            x = input()
            basic_char_skill[8] = int(x)
        elif x == "DRI":
            print(f"""Current Drive Advancements: {self.drive}
            What value would you like to replace it with?""")
            x = input()
            basic_char_skill[9] = int(x)
        elif x == "END":
            print(f"""Current Endurance Advancements: {self.endurance}
            What value would you like to replace it with?""")
            x = input()
            basic_char_skill[10] = int(x)
        elif x == "ENT":
            print(f"""Current Entertain Advancements: {self.entertain}
            What value would you like to replace it with?""")
            x = input()
            basic_char_skill[11] = int(x)
        elif x == "GAM":
            print(f"""Current Gamble Advancements: {self.gamble}
            What value would you like to replace it with?""")
            x = input()
            basic_char_skill[12] = int(x)
        elif x == "GOS":
            print(f"""Current Gossip Advancements: {self.gossip}
            What value would you like to replace it with?""")
            x = input()
            basic_char_skill[13] = int(x)
        elif x == "HAG":
            print(f"""Current Haggle Advancements: {self.haggle}
            What value would you like to replace it with?""")
            x = input()
            basic_char_skill[14] = int(x)
        elif x == "TIM":
            print(f"""Current Intimidate Advancements: {self.intimidate}
            What value would you like to replace it with?""")
            x = input()
            basic_char_skill[15] = int(x)
        elif x == "TUI":
            print(f"""Current Intuition Advancements: {self.intuition}
            What value would you like to replace it with?""")
            x = input()
            basic_char_skill[16] = int(x)
        elif x == "LEA":
            print(f"""Current Leadership Advancements: {self.leadership}
            What value would you like to replace it with?""")
            x = input()
            basic_char_skill[17] = int(x)
        elif x == "MEB":
            print(f"""Current Melee(Basic) Advancements: {self.melee_basic}
            What value would you like to replace it with?""")
            x = input()
            basic_char_skill[18] = int(x)
        elif x == "MEO":
            print(f"""Current Melee(Other) Advancements: {self.melee_other}
            What value would you like to replace it with?""")
            x = input()
            basic_char_skill[19] = int(x)
        elif x == "NAV":
            print(f"""Current Navigation Advancements: {self.navigation}
            What value would you like to replace it with?""")
            x = input()
            basic_char_skill[20] = int(x)
        elif x == "ODS":
            print(f"""Current Outdoor Survival Advancements: {self.outdoor_survival}
            What value would you like to replace it with?""")
            x = input()
            basic_char_skill[21] = int(x)
        elif x == "PER":
            print(f"""Current Perception Advancements: {self.perception}
            What value would you like to replace it with?""")
            x = input()
            basic_char_skill[22] = int(x)
        elif x == "RID":
            print(f"""Current Ride Advancements: {self.ride}
            What value would you like to replace it with?""")
            x = input()
            basic_char_skill[23] = int(x)
        elif x == "ROW":
            print(f"""Current Row Advancements: {self.row}
            What value would you like to replace it with?""")
            x = input()
            basic_char_skill[24] = int(x)
        elif x == "STE":
            print(f"""Current Stealth Advancements: {self.stealth}
            What value would you like to replace it with?""")
            x = input()
            basic_char_skill[25] = int(x)
        elif x == "ALL":
            print("Art")
            x = input()
            basic_char_skill[0] = int(x)
            print("Athletics")
            x = input()
            basic_char_skill[1] = int(x)
            print("Bribery")
            x = input()
            basic_char_skill[2] = int(x)
            print("Charm")
            x = input()
            basic_char_skill[3] = int(x)
            print("Charm Animal")
            x = input()
            basic_char_skill[4] = int(x)
            print("Climb")
            x = input()
            basic_char_skill[5] = int(x)
            print("Cool")
            x = input()
            basic_char_skill[6] = int(x)
            print("Consume Alcohol")
            x = input()
            basic_char_skill[7] = int(x)
            print("Dodge")
            x = input()
            basic_char_skill[8] = int(x)
            print("Drive")
            x = input()
            basic_char_skill[9] = int(x)
            print("Endurance")
            x = input()
            basic_char_skill[10] = int(x)
            print("Entertain")
            x = input()
            basic_char_skill[11] = int(x)
            print("Gamble")
            x = input()
            basic_char_skill[12] = int(x)
            print("Gossip")
            x = input()
            basic_char_skill[13] = int(x)
            print("Haggle")
            x = input()
            basic_char_skill[14] = int(x)
            print("Intimidate")
            x = input()
            basic_char_skill[15] = int(x)
            print("Intuition")
            x = input()
            basic_char_skill[16] = int(x)
            print("Leadership")
            x = input()
            basic_char_skill[17] = int(x)
            print("Melee(Basic)")
            x = input()
            basic_char_skill[18] = int(x)
            print("Melee(Other)")
            x = input()
            basic_char_skill[19] = int(x)
            print("Navigation")
            x = input()
            basic_char_skill[20] = int(x)
            print("Outdoor Survival")
            x = input()
            basic_char_skill[21] = int(x)
            print("Perception")
            x = input()
            basic_char_skill[22] = int(x)
            print("Ride")
            x = input()
            basic_char_skill[23] = int(x)
            print("Row")
            x = input()
            basic_char_skill[24] = int(x)
            print("Stealth")
            x = input()
            basic_char_skill[25] = int(x)
        print("""Is there another value you would like to replace?
        [Y]: Yes
        [N]: No
        """)
        x=input().upper()
        if x == "Y":
            changebskill()
            

def showcurrent():

    print("Name: " + char[0])
    characteristics = (f"WS: {char[1]}, BS: {char[2]}, S: {char[3]}, T: {char[4]}, I: {char[5]}, Ag: {char[6]}, Dex: {char[7]}, Int: {char[8]}, WP: {char[9]}, Fel: {char[10]}")
    basic_skills = (f"""
    Art: {basic_char_skill[0]}                    Athletics: {basic_char_skill[1]}
    Bribery: {basic_char_skill[2]}                Charm: {basic_char_skill[3]}
    Charm Animal: {basic_char_skill[4]}           Climb: {basic_char_skill[5]}
    Cool: {basic_char_skill[6]}                   Consume Alcohol: {basic_char_skill[7]}
    Dodge: {basic_char_skill[8]}                  Drive: {basic_char_skill[9]}
    Endurance: {basic_char_skill[10]}              Entertain: {basic_char_skill[11]}
    Gamble: {basic_char_skill[12]}                 Gossip: {basic_char_skill[13]}
    Haggle: {basic_char_skill[14]}                Intimidate: {basic_char_skill[15]}
    Intuition: {basic_char_skill[16]}              Leadership: {basic_char_skill[17]}
    Melee(Basic): {basic_char_skill[18]}           Melee(Other): {basic_char_skill[19]}
    Navigate: {basic_char_skill[20]}               Outdoor Survival: {basic_char_skill[21]}
    Perception: {basic_char_skill[22]}             Ride: {basic_char_skill[23]}
    Row: {basic_char_skill[24]}                    Stealth: {basic_char_skill[25]}
    """)
    
def meleeroll(): #Will do a basic WeaponSkill roll for the selected character
    z = random.randrange(1, 101)
    meleebasic = char[1] + basic_char_skill[18]
    sl = (meleebasic - z)/10
    print(f"You rolled {z}.")
    if z <= (meleebasic):
        print(f"You Hit by {sl} SLs!")
    else:
        print(f"You Miss by {sl} SLs!")

    

diz = CharacterStats(natalia[0], natalia[1], natalia[2], natalia[3], natalia[4], natalia[5], natalia[6], natalia[7], natalia[8], natalia[9], natalia[10])
dizbskills = CharacterBasicSkills(basic_nat_skill[0], basic_nat_skill[1], basic_nat_skill[2], basic_nat_skill[3], basic_nat_skill[4], basic_nat_skill[5], basic_nat_skill[6], basic_nat_skill[7], basic_nat_skill[8], basic_nat_skill[9], basic_nat_skill[10], basic_nat_skill[11], basic_nat_skill[12], basic_nat_skill[13], basic_nat_skill[14], basic_nat_skill[15], basic_nat_skill[16], basic_nat_skill[17], basic_nat_skill[18], basic_nat_skill[19], basic_nat_skill[20], basic_nat_skill[21], basic_nat_skill[22], basic_nat_skill[23], basic_nat_skill[24], basic_nat_skill[25])
vent = CharacterStats(luci[0], luci[1], luci[2], luci[3], luci[4], luci[5], luci[6], luci[7], luci[8], luci[9], luci[10])
ventbskills = CharacterBasicSkills(basic_luc_skill[0], basic_luc_skill[1], basic_luc_skill[2], basic_luc_skill[3], basic_luc_skill[4], basic_luc_skill[5], basic_luc_skill[6], basic_luc_skill[7], basic_luc_skill[8], basic_luc_skill[9], basic_luc_skill[10], basic_luc_skill[11], basic_luc_skill[12], basic_luc_skill[13], basic_luc_skill[14], basic_luc_skill[15], basic_luc_skill[16], basic_luc_skill[17], basic_luc_skill[18], basic_luc_skill[19], basic_luc_skill[20], basic_luc_skill[21], basic_luc_skill[22], basic_luc_skill[23], basic_luc_skill[24], basic_luc_skill[25])

def hub():
    print("""What would you like to do today?
    [C]: Choose a character
    [S]: Show current character
    [RC]: Replace characteristics/stats
    [RB]: Replace Basic Skill Advancements
    [M]: Melee roll
    [Q]: Quit
    """)
    
    x = input().upper()
    if x == "C":
        choose()
    elif x == "S":
        showcurrent()    
        hub()
    elif x == "RC":
        c = CharacterStats(char[0], char[1], char[2], char[3], char[4], char[5], char[6], char[7],char[8],char[9],char[10])
        c.changestat()
        hub()
    elif x =="RB":
        cbs = CharacterBasicSkills(basic_char_skill[0], basic_char_skill[1], basic_char_skill[2], basic_char_skill[3], basic_char_skill[4], basic_char_skill[5], basic_char_skill[6], basic_char_skill[7], basic_char_skill[8], basic_char_skill[9], basic_char_skill[10], basic_char_skill[11], basic_char_skill[12], basic_char_skill[13], basic_char_skill[14], basic_char_skill[15], basic_char_skill[16], basic_char_skill[17], basic_char_skill[18], basic_char_skill[19], basic_char_skill[20], basic_char_skill[21], basic_char_skill[22], basic_char_skill[23], basic_char_skill[24], basic_char_skill[25])
        cbs.changebskill()
        hub()
    elif x == "M":
        meleeroll()
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
        dizbskills.function()
    elif x =="2":
        vent.function()
        ventbskills.function()
    hub()

hub()