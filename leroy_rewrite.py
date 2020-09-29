import discord
from discord.ext import commands
import os
import asyncio
import random
import re
import logging

PREFIX = "l!"
INSULT_PATH = "C:\\Users\\Drew\\Dropbox\\insults.txt"
LOG_PATH = "C:\\Users\\Drew\\Dropbox\\leroy.log"
"""
BOT_TOKEN = "NjU0MDY2NjA4NjA3NzIzNTcx.XfAJgQ.WUxUuPkLok1k6rmSDNcCVhraQmI"
"""
ROLE_ID = 617964909472514048 #Only people with this role or higher can use the bot

#Setup Logging
logging.basicConfig(filename= LOG_PATH, filemode= 'a', format= '%(asctime)s - %(message)s', datefmt='%b-%d-%y %H:%M:%S', level= logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler())

client = commands.Bot(command_prefix = PREFIX)
client.remove_command('help')

#Read Insults Stored in a file
def GetInsults():
    file = open(INSULT_PATH, "r")
    reader = file.readlines()
    y = []
    for x in reader:
        if x[-1:] == "\n": 
            y.append(x[:-1])
        else:
            y.append(x)
    file.close()
    logging.info("Insults read and stored")
    return y

#Adds an insult to the insult.txt file as well as the current list
def Add_Insult(insult):
    insults.append(insult)
    file = open(INSULT_PATH, "a")
    file.write("\n" + insult)
    file.close()
    logging.info(f"Added \"{insult}\" to insults.txt")

#Create a list of statuses
def RandomStatusList():
    x = []
    x.append("She wanna see my purple pickle up in the wind")
    x.append("Chancletas off, bitch get in")
    x.append("And if your nigga don't like me, hit chinny chin chin")
    x.append("Bitch, I'm hotter than a pepper, no mint")
    x.append("Big stepper, no stilts, big tilt")
    x.append("1K, bought my bitch a new kilt")
    x.append("New skirt, I skrrt, big drift")
    x.append("New grills, 10K, big lisp")
    x.append("Diamonds dancin' on my fist, no disc")
    x.append("Gimme lips, rock band, like KISS")
    x.append("Remember days, me and X hittin' licks")
    x.append("Guantanamera, we hit a lick on your bitch")
    x.append("I'm a Goodfella, Maison Margiela my kick")
    x.append("I am faucet failure, my nigga, I got drip")
    x.append("Ashin' on your bitch, this is that Pokémon trainer shit")
    x.append("Who's this? He should be in cockpit")
    x.append("Cause I'm flyer than a fuckin' ostrich")
    x.append("On my wood, that bitch won't give me polish")
    x.append("I'ma put my foot up in it, sock it")
    x.append("Who's this? He should be in cockpit")
    x.append("Cause I'm flyer than a fuckin' ostrich")
    x.append("On my wood, that bitch won't give me polish")
    x.append("I am constructor, that bitch I demolish, ayy!")
    x.append("Yes give me, a girl from Disney")
    x.append("And a Happy Meal, pretty please don't gyp me")
    x.append("On fries (ketchup), on the guys")
    x.append("McDonalds 'cause they still sellin' pies")
    x.append("Just bought a new suit, got mob ties")
    x.append("Said he want beef, pull up, Five Guys")
    x.append("Yes I'm fire, lil' different like pumpkin fries")
    x.append("Um, hol' up, where's my weed guys?")
    x.append("Guantanamera, we hit a lick on your bitch")
    x.append("I'm a Goodfella, Maison Margiela my kick")
    x.append("I am faucet failure, my nigga, I got drip")
    x.append("Ashin' on your bitch, this is that Pokémon trainer shit")
    x.append("Who's this? He should be in cockpit")
    x.append("Cause I'm flyer than a fuckin' ostrich")
    x.append("On my wood, that bitch won't give me polish")
    x.append("I'ma put my foot up in it, sock it")
    x.append("Who's this? He should be in cockpit")
    x.append("Cause I'm flyer than a fuckin' ostrich")
    x.append("On my wood, that bitch won't give me polish")
    x.append("I am constructor, that bitch I demolish, ayy!")
    x.append("ChaseTheMoney, ChaseTheMoney")
    return x

#Create list of Samuel L Jackson quotes
def LQuotes():
    x = []
    logging.info("Loading quotes...")
    x.append("You shut your face! If we want to hear you talk, I will shove my arm up your ass and work your mouth like a puppet.")
    x.append("You think water moves fast? You should see ice. It moves like it has a mind. Like it knows it killed the world once and got a taste for murder. After the avalanche, it took us a week to climb out. Now we took an oath, that I'm breaking now. We said we'd say it was the snow that killed the other two, but it wasn't. Nature is lethal but it doesn't hold a candle to man.")
    x.append("Everybody knows, when you make an assumption, you make an ass out of you and umption.")
    x.append("Ain't that always the way? Elevator music, a nigga with a kilt, and a chick with a nickel-plated nine?")
    x.append("Enough is enough! I've had it with these motherfuckin' snakes on this motherfuckin plane!")
    x.append("Yeah, Zeus! As in, father of Apollo? Mount Olympus? Don't fuck with me or I'll shove a lightning bolt up your ass!")
    x.append("AK-47, the very best there is. When you absolutely, positively got to kill every motherfucker in the room, accept no substitutes.")
    x.append("Yes, they deserve to die, and I hope they burn in hell!")
    x.append("You know me. It's my duty to please that booty.")
    x.append("The path of the righteous man is beset on all sides by the inequities of the selfish and the tyranny of evil men. Blessed is he who in the name of charity and goodwill, shepherds the weak through the valley of the darkness, for he is truly his brothers keeper, and the finder of lost children. And I will strike down upon thee with great vengeance and furious anger those who attempt to poison and destroy my brothers. And you will know I am the Lord when I lay My vengeance upon thee.")
    x.append("Superladies? They're always trying to tell you their secret identity... think it'll strengthen the relationship or something like that. I say, 'Girl, I don't wanna know about your mild-mannered alter ego or anything like that. I mean, you tell me you're, uh... S-Super, Mega, Ultra Lightning Babe, that's alright with me.' I'm good... I'm good.")
    x.append("You refer to the prophecy of The One, who will bring balance to the Force. You believe it's this boy?")
    x.append("If my answers frighten you then you should cease asking scary questions.")
    x.append("Now that we know who you are, I know who I am.")
    x.append("You are allowed on this council, but we do not grant you the rank of master.")
    x.append("You think that you follow a script in a war and things are all right? People die, sometimes they're innocent but in a war innocent people DIE!")
    x.append("You want my blood? Take my blood!")
    x.append("I'm as serious as a heart attack.")
    x.append("I never did one thing right in my life, you know that? Not one. That takes skill.")
    x.append("To a certain type of woman, I am a hero. I need to be a hero.")
    x.append("Now you've seen how bad things can get and how quick they can get that way. Well, they can get a whole lot worse. So we're not going to fight anymore! We're going to pull together and we're gonna find a way to get out of here! First, we're gonna seal off this pool—")
    x.append("Where is my super suit?")
    x.append("Please! God dammit! I hate this hacker crap!")
    x.append("This party's over.")
    x.append("Nobody's gonna hurt anybody. We're all gonna be like three little Fonzies here. And what's Fonzie like? Come on Yolanda, what's Fonzie like?")
    x.append("Yeah, motherfucker, I eat everything. I eat the pussy. I eat the butt. I eat every motherfuckin' thing.")
    x.append("I recognize the council has made a decision, but given that it's a stupid-ass decision, I've elected to ignore it.")
    x.append("You Been Taking Them Dick Pills Again?")
    x.append("Common Motherfucker, do you speak it?")
    x.append("Do as I say, and you live")
    x.append("What's your deepest fear?")
    x.append("But when John Ruth the Hangman catches you...you hang!")
    x.append("What the fuck happend to you, man? Shit, your ass used to be beautiful.")
    x.append("Hey, hey, hey, I ain't your partner. I ain't your neighbor, your brother, or your friend. I'm your total stranger.")
    x.append("I said, 'You said you ain't know him.'")
    x.append("I was not going to stand by and see another Marine die just to live by those fucking rules.")
    x.append("You have the right to remain silent...but I want to hear you scream!")
    x.append("Anything lost can be found again, except for time wasted.")
    x.append("So that's what the little green men are saying now, 'Take me to your therapist'?")
    x.append("You must realize there are not enough Jedi to protect the Republic. We are the keepers of peace, not soldiers.")
    x.append("A Royale with cheese. What do they call a Big Mac?")
    x.append("Too bad Rudy, Danny Roman was **just** starting to like you.")
    x.append("Which one of you spice girls blew my partner away?")
    x.append("Where the fuck all these people come from? I have been drinking in this shithole all my life, I ain't never seen this many people in here at once.")
    x.append("Yeah, you say 'peace'. I think you kind of mean the other thing.")
    x.append("My product is 51 times stronger than cocaine, 51 times more hallucinogenic than acid, and 51 times more explosive than ecstasy. It's like getting a personal visit...from God!")
    x.append("This is an art gallery, my friend, and this is a piece of art.")
    x.append("What do you do when the thing you most wanted, so perfect, just comes?")
    return x

#Toggle Status
async def ToggleStatus():
    await client.wait_until_ready()
    while not client.is_closed():
        status = random.choice(statuses)
        await client.change_presence(activity=discord.Game(name=status))
        await asyncio.sleep(600)

#Search all insults and returns those that have the query in it's contents
def Search_Insults(query):
    r = []
    for x in insults:
        if re.search(query,x):
            r.append(x)
    return r

def HasPerms(ctx):
    if ctx.author.top_role >= ctx.guild.get_role(ROLE_ID):
        return True
    else:
        return False


insults = GetInsults()
quotes = LQuotes()
statuses = RandomStatusList()

@client.event
async def on_ready():
    logging.info(f"Logged in as: {client.user.name}")
    msg = "On servers:"
    for x in client.guilds:
        msg += " " + x.name + ","
    logging.info(msg + " Bot is ready")

@client.command()
@commands.check(HasPerms)
async def add(ctx, *, insult):
    logging.info(f"Adding '{insult}' to insults.txt from user {ctx.author.name}")
    Add_Insult(insult)
    await ctx.message.delete()
    await ctx.channel.send(ctx.author.mention + " Added '" + insult +"' to insults.")

@client.command(aliases = ['ins'])
@commands.check(HasPerms)
async def insult(ctx):
    mentioned = ctx.message.mentions
    await ctx.message.delete()
    if not mentioned:
        logging.info(f"Getting random insult for user {ctx.author.name}")
        await ctx.channel.send(ctx.author.mention + " " + random.choice(insults))
    else:
        print_msg = "Getting random insult for user " + ctx.author.name + " and directing it at "
        msg = ""
        for x in mentioned:
            msg += x.mention + " "
            print_msg += x.name + " "
        logging.info(print_msg)
        await ctx.channel.send(msg + random.choice(insults))

@client.command(aliases = ['qt'])
@commands.check(HasPerms)
async def quote(ctx):
    mentioned = ctx.message.mentions
    await ctx.message.delete()
    if not mentioned:
        logging.info(f"Getting random quote for user {ctx.author.name}")
        await ctx.channel.send(ctx.author.mention + " " + random.choice(quotes))
    else:
        print_msg = "Getting random quote for user " + ctx.author.name + " and directing it at "
        msg = ""
        for x in mentioned:
            msg += x.mention + " "
            print_msg += x.name + " "
        logging.info(print_msg)
        await ctx.channel.send(msg + random.choice(quotes))

@client.command(aliases = ['srh'])
@commands.check(HasPerms)
async def search(ctx, *, query):
    logging.info(f"Searching insults for {ctx.author.name} with query '{query}'")
    result = Search_Insults(query)
    await ctx.message.delete()
    if not result:
        await ctx.channel.send(ctx.author.mention + " Erorr 404, the insults you seek do not exist...")
    else:
        msg = ctx.author.mention + " **Insults Recalled:**\n"
        for x in result:
            msg += x + "\n"
        await ctx.channel.send(msg)

@client.command()
@commands.check(HasPerms)
async def help(ctx):
    logging.info(f"Displaying help information to {ctx.author.name}")
    embed = discord.Embed(colour = discord.Color.dark_purple())
    embed.set_author(name="Help")
    embed.add_field(name=PREFIX+"add", value="Adds an insult into the insult list.", inline=False)
    embed.add_field(name=PREFIX+"quote[qt]", value="Retrieves or directs random quote at mentioned users.", inline=False)
    embed.add_field(name=PREFIX+"insult[ins]", value="Retrieves or directs random insult at mentioned users.", inline=False)
    embed.add_field(name=PREFIX+"search[srh]", value="Searches the list of insults.", inline=False)
    await ctx.message.delete()
    await ctx.channel.send(embed=embed)

client.loop.create_task(ToggleStatus())
client.run(BOT_TOKEN)
