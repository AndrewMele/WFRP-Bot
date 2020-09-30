import discord
from discord.ext import commands
import os
import asyncio
import random
import re
import logging


PREFIX = "WF!"

#Setup Logging
logging.basicConfig(filename= LOG_PATH, filemode= 'a', format= '%(asctime)s - %(message)s', datefmt='%b-%d-%y %H:%M:%S', level= logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler())

client = commands.Bot(command_prefix = PREFIX)
client.remove_command('help')