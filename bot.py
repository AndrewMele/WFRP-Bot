import discord
from discord.ext import commands
import os
import asyncio
import random
import logging
import crittable
import PyPDF2

f = PyPDF2.PdfFileReader("C:/Users/Arthur/Desktop/Maptools/Tokens/WFRP Characters/Luci Whisper (Vent)/new_Luci_Character_Sheet.pdf")
ff = f.getFields()
value_field = {}
skilladv_value = {}

advances_deletion_for_skills = ["CurrentAdvantage", "WSAdvances", "BSAdvances", "SAdvances", "TAdvances", "IAdvances", "AgAdvances", "DexAdvances", "IntAdvances", "WPAdvances", "FelAdvances"]


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



LOG_PATH = "C:\\Users\\Arthur\\OneDrive\\WFRPTestingbot.log"
BOT_TOKEN = ""

#ROLE_ID = 761293063238582322
#^ This is to the new Bot Testing Server.  Only people with this role can use the bot.
#Bot's name is RENALD
PREFIX = "r!"

#Setup Logging

logging.basicConfig(filename= LOG_PATH, filemode= 'a', format= '%(asctime)s - %(message)s', datefmt='%b-%d-%y %H:%M:%S', level= logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler())

client = commands.Bot(command_prefix = PREFIX)
client.remove_command('help')



@client.event
async def on_ready():
    logging.info(f"Logged in as: {client.user.name}")
    msg = "On servers:"
    for x in client.guilds:
        msg += " " + x.name + ","
    logging.info(msg + " Bot is ready")


@client.command(aliases = ["r"])
async def roll(ctx):
    await ctx.message.delete()
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
async def clear(ctx, number):
    number = int(number)+1 #Converting the amount of messages to delete to an integer
    msgs = []
    async for msg in ctx.message.channel.history(limit = number):
        msgs.append(msg)
    await ctx.message.channel.delete_messages(msgs)

@client.command(aliases=["sr"])
async def skillroll(ctx):
    try:
        await ctx.message.delete()
    except:
        print("Message already deleted.")
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
    try:
        await ctx.message.delete()
    except:
        print("Message already deleted.")
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
        embed.add_field(name= "Hit Status", value = "You Hit The Opponent",inline = False)#Make sure to put opponent name in {}
            #^^Calculate Damage from STR/10, SL, and weapon damage vs opponent's toughness and armour.^^
    elif psl <= osl and crittable.checkcritical(rp) == False:
        embed.add_field(name= "Hit Status", value = "The Opponent Dodged/Parried", inline = False)#Make sure to put opponent name in {}
   
    await ctx.send(embed=embed)

@client.command(aliases = ["rr"])
async def rangedroll(ctx):
    try:
        await ctx.message.delete()
    except:
        print("Message already deleted.")
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