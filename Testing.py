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
        characteristics = ("WS: {0}, BS: {1}, S: {2}, T: {3}, I: {4}, Ag: {5}, Dex: {6}, Int: {7}, WP: {8}, Fel: {9}")
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
        basic_skills = ("""
        Art: {0}                    Athletics: {1}
        Bribery: {2}                Charm: {3}
        Charm Animal: {4}           Climb: {5}
        Cool: {6}                   Consume Alcohol: {7}
        Dodge: {8}                  Drive: {9}
        Endurance: {10}              Entertain: {11}
        Gamble: {12}                 Gossip: {13}
        Haggle: {14}                Intimidate: {15}
        Intuition: {16}              Leadership: {17}
        Melee(Basic): {18}           Melee(Other): {19}
        Navigate: {20}               Outdoor Survival: {21}
        Perception: {22}             Ride: {23}
        Row: {24}                    Stealth: {25}
        """)
        print(basic_skills.format(self.art,self.athletics,self.bribery,self.charm,self.charm_animal,self.climb,self.cool,self.consume_alcohol,self.dodge,self.drive,self.endurance,self.entertain,self.gamble,self.gossip,self.haggle,self.intimidate,self.intuition,self.leadership,self.melee_basic,self.melee_other,self.navigation,self.outdoor_survival,self.perception,self.ride,self.row,self.stealth))
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
            ar = ("""Current Art Advancements: {}
            What value would you like to replace it with?""")
            print(ar.format(self.art))
            x = input()
            basic_char_skill[0] = int(x)
        elif x == "ATH":
            at = ("""Current Athletics Advancements: {}
            What value would you like to replace it with?""")
            print(at.format(self.athletics))
            x = input()
            basic_char_skill[1] = int(x)
        elif x == "BRI":
            br = ("""Current Bribery Advancements: {}
            What value would you like to replace it with?""")
            print(br.format(self.bribery))
            x = input()
            basic_char_skill[2] = int(x)
        elif x == "CHA":
            ch = ("""Current Charm Advancements: {}
            What value would you like to replace it with?""")
            print(ch.format(self.art))
            x = input()
            basic_char_skill[3] = int(x)
        elif x == "ANI":
            ca = ("""Current Charm Animal Advancements: {}
            What value would you like to replace it with?""")
            print(ca.format(self.charm_animal))
            x = input()
            basic_char_skill[4] = int(x)
        elif x == "CLI":
            cl = ("""Current Climb Advancements: {}
            What value would you like to replace it with?""")
            print(cl.format(self.climb))
            x = input()
            basic_char_skill[5] = int(x)
        elif x == "COO":
            co = ("""Current Cool Advancements: {}
            What value would you like to replace it with?""")
            print(co.format(self.cool))
            x = input()
            basic_char_skill[6] = int(x)
        elif x == "CON":
            cn = ("""Current Consume Alcohol Advancements: {}
            What value would you like to replace it with?""")
            print(cn.format(self.consume_alcohol))
            x = input()
            basic_char_skill[7] = int(x)
        elif x == "DOD":
            do = ("""Current Dodge Advancements: {}
            What value would you like to replace it with?""")
            print(do.format(self.dodge))
            x = input()
            basic_char_skill[8] = int(x)
        elif x == "DRI":
            dr = ("""Current Drive Advancements: {}
            What value would you like to replace it with?""")
            print(dr.format(self.drive))
            x = input()
            basic_char_skill[9] = int(x)
        elif x == "END":
            ed = ("""Current Endurance Advancements: {}
            What value would you like to replace it with?""")
            print(ed.format(self.endurance))
            x = input()
            basic_char_skill[10] = int(x)
        elif x == "ENT":
            et = ("""Current Entertain Advancements: {}
            What value would you like to replace it with?""")
            print(et.format(self.entertain))
            x = input()
            basic_char_skill[11] = int(x)
        elif x == "GAM":
            ga = ("""Current Gamble Advancements: {}
            What value would you like to replace it with?""")
            print(ga.format(self.gamble))
            x = input()
            basic_char_skill[12] = int(x)
        elif x == "GOS":
            go = ("""Current Gossip Advancements: {}
            What value would you like to replace it with?""")
            print(go.format(self.gossip))
            x = input()
            basic_char_skill[13] = int(x)
        elif x == "HAG":
            ha = ("""Current Haggle Advancements: {}
            What value would you like to replace it with?""")
            print(ha.format(self.haggle))
            x = input()
            basic_char_skill[14] = int(x)
        elif x == "TIM":
            ti = ("""Current Intimidate Advancements: {}
            What value would you like to replace it with?""")
            print(ti.format(self.intimidate))
            x = input()
            basic_char_skill[15] = int(x)
        elif x == "TUI":
            tu = ("""Current Intuition Advancements: {}
            What value would you like to replace it with?""")
            print(tu.format(self.intuition))
            x = input()
            basic_char_skill[16] = int(x)
        elif x == "LEA":
            le = ("""Current Leadership Advancements: {}
            What value would you like to replace it with?""")
            print(le.format(self.leadership))
            x = input()
            basic_char_skill[17] = int(x)
        elif x == "MEB":
            mb = ("""Current Melee(Basic) Advancements: {}
            What value would you like to replace it with?""")
            print(mb.format(self.melee_basic))
            x = input()
            basic_char_skill[18] = int(x)
        elif x == "MEO":
            mo = ("""Current Melee(Other) Advancements: {}
            What value would you like to replace it with?""")
            print(mo.format(self.melee_other))
            x = input()
            basic_char_skill[19] = int(x)
        elif x == "NAV":
            na = ("""Current Navigation Advancements: {}
            What value would you like to replace it with?""")
            print(na.format(self.navigation))
            x = input()
            basic_char_skill[20] = int(x)
        elif x == "ODS":
            od = ("""Current Outdoor Survival Advancements: {}
            What value would you like to replace it with?""")
            print(od.format(self.outdoor_survival))
            x = input()
            basic_char_skill[21] = int(x)
        elif x == "PER":
            pe = ("""Current Perception Advancements: {}
            What value would you like to replace it with?""")
            print(pe.format(self.perception))
            x = input()
            basic_char_skill[22] = int(x)
        elif x == "RID":
            ri = ("""Current Ride Advancements: {}
            What value would you like to replace it with?""")
            print(ri.format(self.ride))
            x = input()
            basic_char_skill[23] = int(x)
        elif x == "ROW":
            ro = ("""Current Row Advancements: {}
            What value would you like to replace it with?""")
            print(ro.format(self.row))
            x = input()
            basic_char_skill[24] = int(x)
        elif x == "STE":
            st = ("""Current Stealth Advancements: {}
            What value would you like to replace it with?""")
            print(st.format(self.stealth))
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
            
def showcurrent():

    print("Name: " + char[0])
    characteristics = ("WS: {0}, BS: {1}, S: {2}, T: {3}, I: {4}, Ag: {5}, Dex: {6}, Int: {7}, WP: {8}, Fel: {9}")
    print(characteristics.format(char[1], char[2], char[3], char[4], char[5], char[6], char[7],char[8],char[9],char[10]))
    basic_skills = ("""
    Art: {0}                    Athletics: {1}
    Bribery: {2}                Charm: {3}
    Charm Animal: {4}           Climb: {5}
    Cool: {6}                   Consume Alcohol: {7}
    Dodge: {8}                  Drive: {9}
    Endurance: {10}              Entertain: {11}
    Gamble: {12}                 Gossip: {13}
    Haggle: {14}                Intimidate: {15}
    Intuition: {16}              Leadership: {17}
    Melee(Basic): {18}           Melee(Other): {19}
    Navigate: {20}               Outdoor Survival: {21}
    Perception: {22}             Ride: {23}
    Row: {24}                    Stealth: {25}
    """)
    print(basic_skills.format(basic_char_skill[0], basic_char_skill[1], basic_char_skill[2], basic_char_skill[3], basic_char_skill[4], basic_char_skill[5], basic_char_skill[6], basic_char_skill[7], basic_char_skill[8], basic_char_skill[9], basic_char_skill[10], basic_char_skill[11], basic_char_skill[12], basic_char_skill[13], basic_char_skill[14], basic_char_skill[15], basic_char_skill[16], basic_char_skill[17], basic_char_skill[18], basic_char_skill[19], basic_char_skill[20], basic_char_skill[21], basic_char_skill[22], basic_char_skill[23], basic_char_skill[24], basic_char_skill[25]))
    
def meleeroll(): #Will do a basic WeaponSkill roll for the selected character
    z = random.randrange(1, 101)
    meleebasic = char[1] + basic_char_skill[18]
    sl = (meleebasic - z)/10
    r = ("You rolled {}.")
    print(r.format(z))
    if z <= (meleebasic):
        hit = ("You Hit by {} SLs!")
        print(hit.format(sl))
    else:
        hit = ("You Miss by {} SLs!")
        print(hit.format(sl))

    

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
    [Q]: Quit""")
    
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