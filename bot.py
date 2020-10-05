import discord
from discord.ext import commands
import os
import asyncio
import random
import logging
import Testing
import crittable


LOG_PATH = "C:\\Users\\Arthur\\OneDrive\\WFRPTestingbot.log"
BOT_TOKEN = ""

#ROLE_ID = 761293063238582322
#^ This is to the new Bot Testing Server.  Only people with this role can use the bot.

PREFIX = "WF!"

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


"""@client.command()
async def mroll(ctx):
    await ctx.message.delete()
    embed = discord.Embed(colour=discord.Colour.dark_purple(),title="Would you like to use Melee(Basic)?")
    embed.add_field(name="Yes",value="[Y]")
    embed.add_field(name="No",value="[N]")
    await ctx.send(embed=embed)
                        #This is the part that is messing up.  Need to find a way to include choosing which skill they would want to use in case they want to use a different Melee or Dodge
                        #Would need to have an input/ctx.message reader that would accept their choice and then do the meleeroll function.
    await ctx.message()
    if ctx.message() == "Y" or ctx.message() == "Yes":
        await ctx.message.delete()
        meleeroll()
    else:
        await ctx.message.delete()
"""

@client.command(aliases=["mroll"])
async def meleeroll(ctx):
    await ctx.message.delete()
    rp = random.randrange(1, 101) 
    ro = random.randrange(1, 101)
    pmeleebasic = 35 #Replace Later on to read actual character sheet info
    pdodge = 25
    omeleebasic = 20
    ododge = 30
    psl = (pmeleebasic - rp)/10
    osl = (omeleebasic - ro)/10
    embed = discord.Embed(colour = discord.Colour.dark_purple(),title = f"Melee Roll for {ctx.author.name}")
    embed.add_field(name="Roll", value=f"{rp}")
    if rp <= pmeleebasic: 
        embed.add_field(name="Success Levels", value=f"{psl}")
        if crittable.checkcritical(rp):
            embed.add_field(name= "Crit", value ="You Crit!")
            temp_crit = crittable.crit()
            embed.add_field(name="Crit Location", value = temp_crit, inline=False)
            if temp_crit != "":
                embed.add_field(name = "They Suffer:", value = crittable.doescritical(temp_crit), inline=False)
    elif rp >= pmeleebasic:
        embed.add_field(name = "Success Levels", value=f"{psl} SLs")
        if crittable.checkcritical(rp):
            embed.add_field(name="Crit", value="You Crit Failed!")

    if psl >= osl and crittable.checkcritical(rp) == False:
        embed.add_field(name= "Hit Status", value = "You Hit the Opponent",inline = False)#Make sure to put opponent name in {}
            #Calculate Damage from STR/10, SL, and weapon damage.
    elif psl <= osl and crittable.checkcritical(rp) == False:
        embed.add_field(name= "Hit Status", value = "The Opponent Dodged/Parried", inline = False)#Make sure to put opponent name in {}
   
    await ctx.send(embed=embed)

@client.command()
async def help(ctx):
    logging.info(f"Displaying help information to {ctx.author.name}")
    embed = discord.Embed(colour = discord.Color.dark_purple())
    embed.set_author(name="Help")
    embed.add_field(name=PREFIX+"mroll", value="Rolls your Melee(Basic) skill against an opponent.", inline=False)
    embed.add_field(name=PREFIX+"quote[qt]", value="Retrieves or directs random quote at mentioned users.", inline=False)
    embed.add_field(name=PREFIX+"insult[ins]", value="Retrieves or directs random insult at mentioned users.", inline=False)
    embed.add_field(name=PREFIX+"search[srh]", value="Searches the list of insults.", inline=False)
    await ctx.message.delete()
    await ctx.channel.send(embed=embed)

client.run(BOT_TOKEN)