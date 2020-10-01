import discord
from discord.ext import commands
import os
import asyncio
import random
import re
import logging


LOG_PATH = "C:\\Users\\Arthur\\OneDrive\\WFRPTestingbot.log"
#BOT_TOKEN = "NzYxMjc4MzU3ODcwMzQ2MzAw.X3YRuA.IFmTkFHVnzXZ7N_afHVotTJN2Uc"

#ROLE_ID = 761293063238582322
#^ This is to the new Bot Testing Server.  Only people with this role can use the bot.

PREFIX = "WF!"

#Setup Logging

"""logging.basicConfig(filename= LOG_PATH, filemode= 'a', format= '%(asctime)s - %(message)s', datefmt='%b-%d-%y %H:%M:%S', level= logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler())
"""
client = commands.Bot(command_prefix = PREFIX)
#client.remove_command('help')



@client.event
async def on_ready():
    print("Bot is Ready.")

    """
    logging.info(f"Logged in as: {client.user.name}")
    msg = "On servers:"
    for x in client.guilds:
        msg += " " + x.name + ","
    logging.info(msg + " Bot is ready")
    print(f"{client.user} has connected to Discord!")"""

"""
def HasPerms(ctx):
    if ctx.author.top_role >= ctx.guild.get_role(ROLE_ID):
        return True
    else:
        return False
"""

client.run('NzYxMjc4MzU3ODcwMzQ2MzAw.X3YRuA.IFmTkFHVnzXZ7N_afHVotTJN2Uc')
