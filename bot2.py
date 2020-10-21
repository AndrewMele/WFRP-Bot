import discord
from discord.ext import commands
import os
import asyncio
import random
import logging
import crittable
import PyPDF2
import time

character_profiles = {"Natalia Luck" : "C:/Users/Arthur/Desktop/Maptools/Tokens/WFRP Characters/Natalia Luck (Diz)/New Natalia Luck (Diz).pdf", "Luci Whisper" : "C:/Users/Arthur/Desktop/Maptools/Tokens/WFRP Characters/Luci Whisper (Vent)/new_Luci_Character_Sheet.pdf"}
character_name_list = ["Natalia Luck", "Luci Whisper"]
pc = {114826074004783110:"C:/Users/Arthur/Desktop/Maptools/Tokens/WFRP Characters/Natalia Luck (Diz)/New Natalia Luck (Diz).pdf"}
attribute_check_list = ['WS','BS','S','T','I','Ag','Dex','Int','WP','Fel']
attribute_list = []

value_field = {}

basic_skill_check_list = ['Art','Athletics','Bribery','Charm','Climb','Cool','ConsumeAlcohol','Dodge','Drive','Endurnace','Entertain','Gamble','Gossip','Haggle','Intimidate','Intuition','Leadership','MeleeBasic','MeleeOther','Navigation','OutdoorSurvival','Perception','Ride','Row','Stealth']
basicskillcharacteristics = {
    "Art" : "DexCurrent",
    "Athletics" : "AgCurrent",
    "Bribery" : "FelCurrent",
    "Charm": "FelCurrent",
    "Climb": "SCurrent",
    "Cool" : "WPCurrent",
    "ConsumeAlcohol" : "TCurrent",
    "Dodge" : "AgCurrent",
    "Drive" : "AgCurrent",
    "Endurance" : "TCurrent",
    "Entertain" : "FelCurrent",
    "Gamble" : "IntCurrent",
    "Gossip" : "FelCurrent",
    "Haggle" : "FelCurrent",
    "Intimidate" : "SCurrent",
    "Intuition" : "ICurrent",
    "Leadership" : "FelCurrent",
    'MeleeBasic':'WSCurrent',
    'MeleeOther':'WSCurrent',
    "Navigation" : "ICurrent",
    "OutdoorSurvival" : "IntCurrent",
    "Perception" : "ICurrent",
    "Ride" : "AgCurrent",
    "Row" : "SCurrent",
    "Stealth" : "AgCurrent"
}

Skills = []

changecharname = {
    "WS" : "WSCurrent",
    "BS" : "BSCurrent",
    "S" : "SCurrent",
    "T" : "TCurrent",
    "I" : "ICurrent",
    "Ag" : "AgCurrent",
    "Dex" : "DexCurrent",
    "Int" : "IntCurrent",
    "WP" : "WPCurrent",
    "Fel" : "FelCurrent"
}

LOG_PATH = "C:\\Users\\Arthur\\OneDrive\\WFRPTestingbot.log"
BOT_TOKEN = ""
#being funky, so adding this comment so that the github lords are happy

ROLE_ID = 767048275906789388
#^ This is to the new Bot Testing Server.  Only people with this role can use the bot.
#Bot's name is RENALD
PREFIX = "r!"

#Setup Logging

logging.basicConfig(filename= LOG_PATH, filemode= 'a', format= '%(asctime)s - %(message)s', datefmt='%b-%d-%y %H:%M:%S', level= logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler())

client = commands.Bot(command_prefix = PREFIX)
client.remove_command('help')




class characteristics:
    def __init__(self,name,initial,adv,current):
        self.name = name
        self.initial = initial
        self.adv = adv
        self.current = current      
        
class skillsobjectlist:
    def __init__(self,name,char,charval,adv,current):
        self.name = name
        self.char = char
        self.charval = charval
        self.adv = adv
        self.current = current

async def playercharacterstatus(ctx):
    if ctx.guild.get_role(ROLE_ID) in ctx.author.roles:
        try:    
            characterpdf = pc.get(ctx.author.id)
            f = PyPDF2.PdfFileReader(characterpdf)
            ff = f.getFields()

            attribute_list.clear()
            Skills.clear()

            for x in ff:
                #fields.append(ff[x])  Another way of making value_field
                if ff[x].value == '' or ff[x].value == None:
                    value_field[ff[x].name] = '0'
                else:
                    value_field[ff[x].name] = ff[x].value

            for x in attribute_check_list:
                for y in value_field:
                    if y.find(f'{x}') != -1:
                        if y.find("Initial") != -1:
                            initial = value_field.get(y)
                        elif y.find("Advances") != -1:
                            adv = value_field.get(y)
                        elif y.find("Current") != -1:
                            current = value_field.get(y)
                attribute_list.append(characteristics(x,initial,adv,current))
            
            for x in basic_skill_check_list:
                for y in value_field:
                    if y.find(f'{x}') != -1:
                        if y.find("Advances") != -1:
                            adv = value_field.get(y)
                char = basicskillcharacteristics.get(x)
                for y in value_field:
                    if y.find(f'{char}') != -1:
                        charval = value_field.get(y)
                current = int(charval) + int(adv)
                Skills.append(skillsobjectlist(x,char,charval,adv,current))

            for x in value_field:
                if x.find("SkillNameRow") != -1 and value_field.get(x) != '0': #if x has 'SkillNameRow' in its name and has an actual string value
                    name = value_field.get(y)
                elif x.find("CharacteristicRow") != -1 and x.find("_") == -1 and value_field.get(x) in changecharname: #if x has 'CharacteristicsRow' in its name, doesn't have a '_', and is in changecharname
                    char = changecharname.get(value_field.get(x))
                elif x.find("CharacteristicRow") != -1 and x.find("_") != -1:
                    charval = value_field.get(x)
                elif x.find("AdvRow") != -1 and value_field.get(x) != '0': #if x has 'AdvRow' in its name and has an actual int value
                    adv = value_field.get(x)
                
                try:
                    current = int(charval) + int(adv)
                    Skills.append(skillsobjectlist(name,char,charval,adv,current))
                    del name
                    del char
                    del charval
                    del adv
                except:
                    pass
        except:
            ctx.send("Sorry you do not have a character sheet.  Let me help you with that.")
            time.sleep(1)
            await selectcharacter(ctx)

@client.event
async def on_ready():
    logging.info(f"Logged in as: {client.user.name}")
    msg = "On servers:"
    for x in client.guilds:
        msg += " " + x.name + ","
    logging.info(msg + " Bot is ready")

@client.command(aliases = ["sc"])
async def selectcharacter(ctx):
    try: 
        await ctx.message.delete()
    except:
        logging.info("Message already deleted.")
    embed = discord.Embed(colour=discord.Colour.dark_purple(),title="Which Character Sheet would you like to use?")
    y=0
    for x in character_name_list:  #Goes through all the known characters and adds them to the embed.
        embed.add_field(name = f"{x}", value = f"[{y}]")
        if y <= len(character_name_list):
            y=y+1
    embed.add_field(name = "New Character", value = f"[{y}]")
    await ctx.send(embed=embed)
    channel = ctx.message.channel
    response = await client.wait_for('message')
    z = response.content
    #Reads your response and selects the character to apply to all of the skills.  If your selection did not exist or you selected New Character, it should create a new character for you.
    try:
        pc[ctx.author.id] = character_profiles.get(character_name_list[int(z)])
        logging.info(f"{ctx.author.name} selected {character_name_list[int(z)]} as their character.")
    except:
        await newcharacter(ctx)
        pc[ctx.author.id] = character_profiles.get(character_name_list[int(z)])
        logging.info(f"{ctx.author.name} selected {character_name_list[int(z)]} as their character.")
        await ctx.send(f"Your new character {character_name_list[int(z)]} has been created and selected.")
    
    await playercharacterstatus(ctx)

@client.command(aliases = ["nc"])
async def newcharacter(ctx):
    await ctx.send("What is the name of your character?")
    channel = ctx.message.channel
    response = await client.wait_for('message')
    charactername = response.content
    await ctx.send("Please link the location of your pdf.  Do not forget to put in your pdf.  Example: C:\\Users\\Name\\Desktop\\WFRP_Characters\\New Character.pdf")
    response = await client.wait_for('message')
    characterlocation = response.content
    character_name_list.append(f"{charactername}")
    character_profiles[f"{charactername}"] = f"{characterlocation}"
    logging.info(f"{ctx.author.name} has created the {charactername} Character")
    await clear(ctx, 4)
    
@client.command(aliases=["sr"])
async def skillroll(ctx):
    await playercharacterstatus(ctx)
    try:
        await ctx.message.delete()
    except:
        logging.info("Message already deleted.")
    rp = random.randrange(1, 101)
    pskill = 0

    embed = discord.Embed(colour=discord.Colour.dark_purple(),title="Please type which skill you would like to use.")
    await ctx.send(embed=embed)
    channel = ctx.message.channel
    response = await client.wait_for('message')
    z = response.content
    if z.find('Melee') != -1:
        ctx.send("A Melee Skill, eh?  Let's bring you over to the melee roll (r!mr) section.")
        time.sleep(1)
        await meleeroll(ctx)
    elif z.find('Ranged') != -1:
        ctx.send("A Ranged Skill, eh?  Let's bring you over to the ranged roll (r!rr) section.")
        time.sleep(1)
        await rangedroll(ctx)
    for x in Skills:
        if z == x.name:
            pskill = x.current
            break

    await clear(ctx,1)
    psl = (pskill - rp)/10
    time.sleep(1)

    embed = discord.Embed(colour = discord.Colour.dark_purple(),title = f"{z} Roll for {ctx.author.name}")
    embed.add_field(name="Roll", value=f"{rp}")
    if rp <= pskill: 
        embed.add_field(name="You Succeeded by", value =f"{psl}")
    elif rp >= pskill:
        embed.add_field(name="You Failed by", value = f"{psl}")

    await ctx.send(embed=embed)

@client.command(aliases = ["mr"])
async def meleeroll(ctx):
    await playercharacterstatus(ctx)
    try:
        await ctx.message.delete()
    except:
        logging.info("Message already deleted.")
    rp = random.randrange(1, 101) 
    ro = random.randrange(1, 101)
    omeleebasic = 20
    omeleebrawl = 30
    ododge = 40
    pskill = 0
    oskill = 0
    
    embed = discord.Embed(colour=discord.Colour.dark_purple(),title="Please type the Melee Skill that you would like to use.")

    for x in Skills:  #get all the names of the skills in no_combat_skill_name_list
            if x.name.find("Melee") != -1:
                embed.add_field(name = f"{str(x.name)}", value = f"Skill Value: {int(x.current)}")

    await ctx.send(embed=embed)
    channel = ctx.message.channel
    response = await client.wait_for('message')
    z = response.content
    for x in Skills:
        if z == x.name:
            pskill = x.current
            break

    await clear(ctx,1)
    psl = (pskill - rp)/10
    osl = (omeleebasic - ro)/10
    time.sleep(1)

    embed = discord.Embed(colour = discord.Colour.dark_purple(),title = f"{z} Roll for {ctx.author.name}")
    embed.add_field(name="Roll", value=f"{rp}")
    if rp <= pskill: 
        embed.add_field(name="Success Levels", value=f"{psl}") 
        if crittable.checkcritical(rp):
            embed.add_field(name= "Crit", value ="You Crit!")
            temp_crit = crittable.crit()
            embed.add_field(name="Crit Location", value = temp_crit, inline=False)
            if temp_crit != "":
                embed.add_field(name = "They Suffer:", value = crittable.doescritical(temp_crit), inline=False)
    elif rp >= pskill:
        embed.add_field(name = "Success Levels", value=f"{psl} SLs")
        if crittable.checkcritical(rp):
            embed.add_field(name="Crit", value="You Crit Failed!")

    if psl >= osl and crittable.checkcritical(rp) == False:
        embed.add_field(name= "Opponent's SL", value = f"{osl} SLs")
        embed.add_field(name= "Hit Status", value = "You Hit The Opponent",inline = False)#Make sure to put opponent name in {}
            #^^Calculate Damage from STR/10, SL, and weapon damage vs opponent's toughness and armour.^^
    elif psl <= osl and crittable.checkcritical(rp) == False:
        embed.add_field(name= "Opponent's SL", value = f"{osl} SLs")
        embed.add_field(name= "Hit Status", value = "The Opponent Dodged/Parried", inline = False)#Make sure to put opponent name in {}
   
    await ctx.send(embed=embed)

@client.command(aliases = ["rr"])
async def rangedroll(ctx):
    await playercharacterstatus(ctx)
    try:
        await ctx.message.delete()
    except:
        logging.info("Message already deleted.")
    rp = random.randrange(1, 101) 
    ro = random.randrange(1, 101)
    ododge = 30
    pskill = 0
    oskill = 0
    
    embed = discord.Embed(colour=discord.Colour.dark_purple(),title="Please type the Ranged Skill that you would like to use.")

    for x in Skills:  #get all the names of the skills in no_combat_skill_name_list
            if x.name.find("Ranged") != -1:
                embed.add_field(name = f"{str(x.name)}", value = f"Skill Value: {int(x.current)}")
    embed.add_field(name="BS",value = f"Skill Value: {int(value_field.get('BSCurrent'))}")
    await ctx.send(embed=embed)
    channel = ctx.message.channel
    response = await client.wait_for('message')
    z = response.content
    for x in Skills:
        if z == x.name:
            pskill = x.current
            break
        elif z == 'BS':
            pskill = int(value_field.get('BSCurrent'))
            break

    await clear(ctx,1)
    psl = (pskill - rp)/10
    osl = (ododge - ro)/10
    time.sleep(1)

    embed = discord.Embed(colour = discord.Colour.dark_purple(),title = f"{z} Roll for {ctx.author.name}")
    embed.add_field(name="Roll", value=f"{rp}")
    if rp <= pskill: 
        embed.add_field(name="Success Levels", value=f"{psl}")
        if crittable.checkcritical(rp):
            embed.add_field(name= "Crit", value ="You Crit!")
            temp_crit = crittable.crit()
            embed.add_field(name="Crit Location", value = temp_crit, inline=False)
            if temp_crit != "":
                embed.add_field(name = "They Suffer:", value = crittable.doescritical(temp_crit), inline=False)
    elif rp >= pskill:
        embed.add_field(name = "Success Levels", value=f"{psl} SLs")
        if crittable.checkcritical(rp):
            embed.add_field(name="Crit", value="You Crit Failed!")

    if psl >= osl and crittable.checkcritical(rp) == False:
        embed.add_field(name= "Hit Status", value = "You Hit The Opponent",inline = False)#Make sure to put opponent name in {}
            #^^Calculate Damage from STR/10, SL, and weapon damage vs opponent's toughness and armour.^^
    elif psl <= osl and crittable.checkcritical(rp) == False:
        embed.add_field(name= "Hit Status", value = "The Opponent Dodged/Parried", inline = False)#Make sure to put opponent name in {}
   
    await ctx.send(embed=embed)

@client.command()
async def clear(ctx, number):
    number = int(number)+1 #Converting the amount of messages to delete to an integer
    msgs = []
    async for msg in ctx.message.channel.history(limit = number):
        msgs.append(msg)
    await ctx.message.channel.delete_messages(msgs)


@client.command()
async def help(ctx):
    logging.info(f"Displaying help information to {ctx.author.name}")
    embed = discord.Embed(colour = discord.Color.dark_purple())
    embed.set_author(name="Help")
    embed.add_field(name=PREFIX+"roll or r", value="Rolls your Melee (Basic) skill against an opponent.", inline=False)
    embed.add_field(name=PREFIX+"quote[qt]", value="Retrieves or directs random quote at mentioned users.", inline=False)
    embed.add_field(name=PREFIX+"insult[ins]", value="Retrieves or directs random insult at mentioned users.", inline=False)
    embed.add_field(name=PREFIX+"search[srh]", value="Searches the list of insults.", inline=False)
    await ctx.message.delete()
    await ctx.channel.send(embed=embed)


 
client.run(BOT_TOKEN)