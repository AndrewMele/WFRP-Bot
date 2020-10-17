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
value_field = {}
skilladv_value = {}
advances_deletion_for_skills = ["CurrentAdvantage", "WSAdvances", "BSAdvances", "SAdvances", "TAdvances", "IAdvances", "AgAdvances", "DexAdvances", "IntAdvances", "WPAdvances", "FelAdvances"]
pc = {}


LOG_PATH = "C:\\Users\\Arthur\\OneDrive\\WFRPTestingbot.log"
BOT_TOKEN = "NzYxMjc4MzU3ODcwMzQ2MzAw.X3YRuA.SDS2rlG-Uym8d2bP1bU082AIT40"


ROLE_ID = 767048275906789388
#^ This is to the new Bot Testing Server.  Only people with this role can use the bot.
#Bot's name is RENALD
PREFIX = "r!"

#Setup Logging

logging.basicConfig(filename= LOG_PATH, filemode= 'a', format= '%(asctime)s - %(message)s', datefmt='%b-%d-%y %H:%M:%S', level= logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler())

client = commands.Bot(command_prefix = PREFIX)
client.remove_command('help')


async def playercharacterstatus(ctx):
    if ctx.guild.get_role(ROLE_ID) in ctx.author.roles:
        try:
            characterpdf = pc.get(ctx.author.id)
            f = PyPDF2.PdfFileReader(characterpdf)
            ff = f.getFields()

            for x in ff:
                if ff[x].value == '' or ff[x].value == None:
                    value_field[ff[x].name] = 0
                else:
                    value_field[ff[x].name] = ff[x].value

            for x in value_field:
                if x.find("Adv") != -1:
                    skilladv_value[f"{x}"] = value_field.get(x)
                    if x in advances_deletion_for_skills:
                        skilladv_value.popitem()
                    elif x.find("AdvRow") != -1:
                        skilladv_value.popitem()
                elif x.find("SkillNameRow") != -1:
                    #if value from SkillNameRow# has Melee in it, create new key using SkillNameRow#'s value as the key and AdvRow1 as the value
                    if value_field.get(x) != 0:
                        name = value_field.get(x)
                if x.find("AdvRow") != -1:
                    if value_field.get(x) != 0:
                        value = value_field.get(x)
                try:        
                    skilladv_value[f"{name}"] =f"{value}"
                    del name
                    del value
                except:
                    pass
        except:
            await ctx.send("Sorry, you do not have a character selected.  Let me help you with that.")
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
    value_field.clear()
    skilladv_value.clear()
    #Reads your response and selects the character to apply to all of the skills.  If your selection did not exist or you selected New Character, it should create a new character for you.
    try:
        characterpdf = character_profiles.get(character_name_list[int(z)])
        pc[ctx.author.id] = character_profiles.get(character_name_list[int(z)])
        logging.info(f"{ctx.author.name} selected {character_name_list[int(z)]} as their character.")
    except:
        await newcharacter(ctx)
        characterpdf = character_profiles.get(character_name_list[int(z)])
        pc[ctx.author.id] = character_profiles.get(character_name_list[int(z)])
        logging.info(f"{ctx.author.name} selected {character_name_list[int(z)]} as their character.")
        await ctx.send(f"Your new character {character_name_list[int(z)]} has been created and selected.")
    
    f = PyPDF2.PdfFileReader(characterpdf)
    ff = f.getFields()

    for x in ff:
        if ff[x].value == '' or ff[x].value == None:
            value_field[ff[x].name] = 0
        else:
            value_field[ff[x].name] = ff[x].value

    for x in value_field:

        if x.find("Adv") != -1:
            skilladv_value[f"{x}"] = value_field.get(x)
            if x in advances_deletion_for_skills:
                skilladv_value.popitem()

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

@client.command(aliases = ["r"])
async def roll(ctx):
    await playercharacterstatus(ctx)
    try: 
        await ctx.message.delete()
    except:
        logging.info("Message already deleted.")
    embed = discord.Embed(colour=discord.Colour.dark_purple(),title="Would you like to roll for Melee, Ranged, or a Skill?")
    embed.add_field(name="Melee",value="[1]")
    embed.add_field(name="Ranged",value="[2]")
    embed.add_field(name="Skill",value="[3]")
    await ctx.send(embed=embed)
    channel = ctx.message.channel
    def check(m):
        return (m.content == "1" or m.content == "2" or m.content == "3") and m.channel == channel
    response = await client.wait_for('message', check=check)
    if response.content == "1":
        await meleeroll(ctx)
    elif response.content == "2":
        await rangedroll(ctx)
    elif response.content == "3":
        await skillroll(ctx)
    await response.delete()


@client.command()
async def addskill(ctx):
    await playercharacterstatus(ctx)
    try: 
        await ctx.message.delete()
    except:
        logging.info("Message already deleted.")
    channel = ctx.message.channel
    await ctx.send("What is the skill called?")
    response = await client.wait_for('message')
    x = response.content
    await ctx.send("How many Advances (Adv) do you have in this skill?")
    response = await client.wait_for('message')
    y = response.content
    
    embed = discord.Embed(colour=discord.Colour.dark_purple(),title=f"You have {y} Advances in {x}.  Is that correct?")
    embed.add_field(name="Yes",value="[1]")
    embed.add_field(name="No",value="[2]")
    await ctx.send(embed=embed)
    def check(m):
        return (m.content == "1" or m.content == "2") and m.channel == channel
    response = await client.wait_for('message', check=check)
    if response.content == "1":
        skilladv_value[f"{x}"] = f"{y}"
        await response.delete()
        await clear(ctx, 5)
    elif response.content == "2":
        await response.delete()
        await clear(ctx, 5)
    

@client.command(aliases=["sr"])
async def skillroll(ctx):
    await playercharacterstatus(ctx)
    try:
        await ctx.message.delete()
    except:
        logging.info("Message already deleted.")
    rp = random.randrange(1, 101)
    pathletics = (int(value_field.get("AgCurrent")) + int(value_field.get("AthleticsAdvances")))
    pcool = (int(value_field.get("WPCurrent")) + int(value_field.get("CoolAdvances")))
    pcharm = (int(value_field.get("FelCurrent")) + int(value_field.get("CharmAdvances")))
    pskill = 0

    embed = discord.Embed(colour=discord.Colour.dark_purple(),title="Would you like to use Athletics, Cool, or Charm?")
    embed.add_field(name="Athletics",value="[1]")
    embed.add_field(name="Cool",value="[2]")
    embed.add_field(name="Charm",value="[3]")
    await ctx.send(embed=embed)
    channel=ctx.message.channel
    def check(m):
        return (m.content == "1" or m.content == "2" or m.content == "3") and m.channel == channel
    response = await client.wait_for('message', check=check)
    if response.content == "1":
        pskill = pathletics
    elif response.content == "2":
        pskill = pcool
    elif response.content == "3":
        pskill = pcharm
    
    psl = (pskill -rp)/10

    embed = discord.Embed(colour = discord.Colour.dark_purple(),title = f"Skill Roll for {ctx.author.name}")
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
    pmeleebasic = (int(value_field.get("WSCurrent")) + int(value_field.get("MeleeBasicAdvances")))
    pmeleebrawl = (int(value_field.get("WSCurrent")) + int(value_field.get("MeleeOtherAdvances")))
    omeleebasic = 20
    omeleebrawl = 30
    ododge = 40
    pskill = 0
    oskill = 0
    
    embed = discord.Embed(colour=discord.Colour.dark_purple(),title="Would you like to use Melee (Basic) or Melee (Brawl)?")
    
    embed.add_field(name="Melee (Basic)",value="[1]")
    embed.add_field(name="Melee (Brawl)",value="[2]")
    await ctx.send(embed=embed)
    channel = ctx.message.channel
    def check(m):
        return (m.content == "1" or m.content == "2") and m.channel == channel
    response = await client.wait_for('message', check=check)
    if response.content == "1":
        pskill = pmeleebasic
    elif response.content == "2":
        pskill = pmeleebrawl

    psl = (pskill - rp)/10
    osl = (omeleebasic - ro)/10

    embed = discord.Embed(colour = discord.Colour.dark_purple(),title = f"Melee Roll for {ctx.author.name}")
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
    prangedbow = (int(value_field.get("BSCurrent")))
    prangedsling = (int(value_field.get("BSCurrent")))
    ododge = 30
    pskill = 0
    oskill = 0
    
    embed = discord.Embed(colour=discord.Colour.dark_purple(),title="Would you like to use Ranged (Bow) or Ranged (Sling)?")
    embed.add_field(name="Ranged (Bow)",value="[1]")
    embed.add_field(name="Ranged (Sling)",value="[2]")
    await ctx.send(embed=embed)
    channel = ctx.message.channel
    def check(m):
        return (m.content == "1" or m.content == "2") and m.channel == channel
    response = await client.wait_for('message', check=check)
    if response.content == "1":
        pskill = prangedbow
    elif response.content == "2":
        pskill = prangedsling

    psl = (pskill - rp)/10
    osl = (ododge - ro)/10

    embed = discord.Embed(colour = discord.Colour.dark_purple(),title = f"Ranged Roll for {ctx.author.name}")
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