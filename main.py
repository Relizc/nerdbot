import random
import discord
from discord.ext import commands
from discord.utils import get
from discord_components import DiscordComponents, Button, ButtonStyle, Select, SelectOption
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS, cross_origin
from threading import Thread
import datetime
import asyncio
import json
import time
import base64
import uuid
import urllib.request
import urllib
import requests
import emoji
import re
import os
import traceback
import math
import binascii
from bot import Violation, AntiViolation, ban, UserBot

os.system("")

# LANG COVERED UNTIL LINE 1594

#test_contrib

bot = commands.Bot(command_prefix = "bruh ", intents = discord.Intents.all())

# cog.py

BOT_RUNNING = False

REBOOT = [False, 0, "Error"]

DEBUG_WHITELIST = [707072996346691645, 898912199517556786]
TRUST_SERVERS = [713361830247923713, 913703434279088158,924506697618317402]
OFFICIAL_SERVER = [924506697618317402]

DISABLED = []

############# SLASH COMMANDS ##############################################

####### CHECK ALOWWS

RED = discord.Color.from_rgb(255, 60, 60)
GREEN = discord.Color.from_rgb(132, 255, 128)
YELLOW = discord.Color.from_rgb(255, 255, 128)

UPDATES = """Feburary 5, 2022

__Update1.0.6-48815c3303bd__
- IMPORTANT: THE COMMAND PREFIX SWITCHED TO `bruh <...>`
"""

Commands = {"0":[
  {"name": "auction", "displayName": "Auction", "description": "Auction something from your inventory", "usage": "bruh auction, bruh a", "specific": {"description": "Your inventory have many precious items isn't it! But, many of them cannot be sold in the market. So, that's why you should sell it in the auction house!", "usage": "bruh auction <item> [amount = 1]"}},
  {"name": "auctions", "displayName": "Auction House", "description": "View everything selling on the auction house!", "usage": "bruh auctions"},
  {"name": "guessmynumber", "displayName": "Guess my number", "description": "Play a game with the bot!", "usage": "bruh guessmynumber"},
  {"name": "help", "displayName": "Help", "description": "Well you are browsing it now!", "usage": "bruh help"}, 
  {"name": "market", "displayName": "Nerdmart", "description": "The best market in the NerdPlanet!", "usage": "bruh market"},
  {"name": "poop", "displayName": "Poop", "description": "Go poop on... The server!", "usage": "bruh poop"},
  ],
  "1":[
    {"name": "profile", "displayName": "Profile", "description": "View how much Nerdies you have.", "usage": "bruh profile"},
    {"name": "site", "displayName": "Site", "description": "Check out our awesome site!", "usage": "bruh site"},
    {"name": "notifications", "displayName": "Notifications", "description": "Check out your notifications!", "usage": "bruh notifs, bruh notifications"},
    {"name": "rickroll", "displayName": "Rick, roll?", "description": "Rickroll one of your friends! I promise this will be fun!", "usage": "bruh rickroll"},
    {"name": "message", "displayName": "Send messages!", "description": "Send messages to your friends with the new message software: iNerd™ Notify!", "usage": "bruh message, bruh send"},
    {"name": "youtube", "displayName": "Youtube!", "description": "Wanna crack up? Watch some youtube videos!", "usage": "bruh youtube, bruh yt"}
  ],
  "2": [
    {"name": "vocabulary", "displayName": "Learn vocabularies!", "description": "Suck at English (like me)? Learn some vocabulary from the greatest urban dictionary! (Some of them are funny and incorrect lol)", "usage": "bruh vocabulary, bruh vocab, bruh word"},
    {"name": "sell", "displayName": "Sell stuff!", "description": "Similar to the market command but you sell stuff.", "usage": "bruh sell"},
    {"name": "plot", "displayName": "Your plots", "description": "Okay, the plots are what you build on.", "usage": "bruh plot, bruh plots"},
    {"name": "charades", "displayName": "Charades!", "description": "One actor, the rest are guessers. Try and guess what is the actor's word!", "usage": "bruh charades"}
  ]
}

Commands_cooldown = {
  "hangman": (1, 15, "seconds"),
  "bounty": (5, 1, "day"),
  "_yt": (1, 10, "seconds"),
  "_word": (1, 20, "seconds"),
  "_make5": (1, 10, "seconds"),
  "_disablerick": (1, 1, "minute"),
  "_enablerick": (1, 1, "minute"),
  "rickroll": (5, 10, "minutes"),
  "poop": (1, 30, "seconds"),
  "_message": (1, 20, "seconds"),
  "Notifis": (1, 10, "seconds"),
  "profile": (1, 10, "seconds"),
  "checkInventory": (1, 5, "seconds"),
  "withdrawFromBank": (1, 15, "seconds"),
  "helpOnCommand": (1, 0, "seconds"),
  "NerdMart": (1, 10, "seconds"),
  "_sell": (1, 10, "seconds"),
  "OpenWebSite": (1, 5, "seconds"),
  "menu": (1, 20, "seconds"),
  "api": (1, 2, "minutes"),
  "guesscoin": (1, 10, "seconds")
}

items = json.load(open("items.json"))
pockets = json.load(open("pocket.json"))

shop = {"0":[
    "POOP", "CARROT", "NERDSMILE", "NUKE", "PHONE"
  ]
}



LANGDICT = {"EN_US": json.load(open("lang/EN_US.json")), "ZH_CN": json.load(open("lang/ZH_CN.json"))}

class LANG:

  def __init__(self, userid):
    self.id = userid

  def LANG(self, namespace):

    global LANGDICT
  
    language = next((i for i in json.load(open("game.json"))[str(self.id)]["settings"] if i["name"] == "LANG"), None)
    if language == None:
      return "INVALID_SETTINGS%" + namespace
    try:
      return LANGDICT[language["value"]].get(namespace, namespace)
    except KeyError:
      return "INVALID_SETTINGS_VALUE%" + namespace


  




SHOP_CREDITS = {}
colors = {"white": "", "red": "\u001b[31m", "orange": "\u001b[31;1m", "yellow": "\u001b[33;1m", "green": "\u001b[32;1m"}
dc1 = {"0": "white", "1": "yellow", "2": "red", "3": "magenta"}
dc2 = {"0": "INFO  ", "1": "WARN  ", "2": "ERROR ", "3": "FATAL "}

def clog(string, type):
  string = str(string)
  color = dc1[str(type)]
  cur = datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")
  prefix = f"[{dc2[str(type)]}| {cur}] "
  string = colors[color] + prefix + string + "\u001b[0m"
  print(string)

clog("NerdBot Program booting up.", 0)
clog(random.choice(json.load(open("oneline.json"))), 0)

achievements = json.load(open("achievements.json"))


async def addAchievement(ctx, a_id):

  global achievements
  await checkAccountExsists(id)
  profile = json.load(open("game.json"))
  
  if not a_id in achievements:
    return
    
  profile[str(ctx.author.id)]["achievements"].append(a_id)
  
  embed=discord.Embed(title="Achievement Unlocked!", description=f"Congratulations {ctx.author.name}, you just unlocked another achievement!", color=0xfef000)
  embed.add_field(name="undefined", value="undefined", inline=False)
  await ctx.send(embed=embed)
  

async def checkAccountExsists(id):
  pre = json.load(open("game.json"))
  while True:
    found = False
    phone = random.randint(10000000000, 99999999999)
    for i in pre:
      if pre[i]["phone"] == phone:
        found = True
    if not found:
      break
  if not str(id) in pre:
    pre[str(id)] = {"exp": 0.0, "pocketItems": [], "level": 0, "nerdies": {"wallet": 100.0, "bank": [{"name": "DEFAULT", "amount": 0.0}]}, "settings": [{"name": "DM", "value": False}, {"name": "LANG", "value": "EN_US"}], "deaths": 0.0, "inventory": [{"name": "POOP", "amount": 10, "data": {}}, {"name": "PHONE", "amount": 1, "data": {"additional_description": " Also, this is your first Nerd Phone!"}}], "plots": {"NERD_PLOT": {"texticon": ":poop:", "buildType": "NONE", "displayName": "Brand New Plot", "data": {}}}, "questMilestone": [], "achievements": [], "trophy": [], "phone": phone}
    json.dump(pre, open("game.json", "w"))
  else:
    pass

def user_by_phone(phoneno):
  profile = json.load(open("game.json"))
  usr = None
  for i in profile:
    if profile[i]["phone"] == phoneno:
      usr = int(i)
  return usr

def user_by_phone_str(phoneno):
  profile = json.load(open("game.json"))
  usr = None
  for i in profile:
    if profile[i]["phone"] == phoneno:
      usr = f"**[NPU-{phoneno}-{int(i)}]**"
  return usr

def phonestr(phoneno):
  stat = str(phoneno)
  return f"(+{stat[0]}) {stat[1:4]}-{stat[4:7]}-{stat[7:11]}"

async def newAuction(item_id):
  d = json.load(open("auctions.json"))
  now = datetime.datetime.now()
  timing = datetime.timedelta(minutes = 1)
  end = now + timing
  unix = time.mktime(now.timetuple())
  endunix = time.mktime(end.timetuple())
  d.append({"item":item_id, "start": unix, "end":endunix})
  json.dump(d, open("auctions.json","w"))


async def newNotif(userid, sendBy, title, message, messageType, DM):

  pre = json.load(open("notifications.json"))
  if not str(userid) in pre:
    pre[str(userid)] = []
    json.dump(pre, open("notifications.json", "w"))
  else:
    pass

  RANDOM = discord.Color.from_rgb(random.randint(20,255),random.randint(20,255),random.randint(20,255))

  ID = genID()
  messages = json.load(open("notifications.json"))
  dat = {"id": ID, "name": messageType, "title": title, "details": message, "time": int(round(time.time(), 0)), "sendBy": sendBy}
  usr = bot.get_user(int(userid))
  try:
    messages[str(userid)].append(dat)
  except:
    messages[str(userid)] = []
    messages[str(userid)].append(dat)
  json.dump(messages, open("notifications.json", "w"))
  embed = discord.Embed(color = RANDOM, title = dat["title"], description = dat["details"], timestamp = datetime.datetime.utcfromtimestamp(dat["time"]))
  if messageType == "SYSTEM":
    sendBy = dat["sendBy"]
  else:
    sendBy = bot.get_user(dat["sendBy"]).name
  embed.set_footer(text="%s: %s | " % (random.choice([
    "Sent by the cool",
    "Sent by the troll",
    "Sent by the LOL",
    "Send by- oops grammar",
    "Sent by the glorius*",
    "Sent by the nice"
  ]), sendBy) + await getTime())
  await checkAccountExsists(str(userid))
  if DM:
    sets = json.load(open("game.json"))[str(userid)]["settings"]
    for i in sets:
      if i["name"] == "DM" and i["value"] == True:
        await usr.send("New iNerd™ Message!", embed = embed)
      else:
        pass


FOOTER = [
  "Yee",
  "It was a rainy day.",
  "1+1=3?",
  "1145141919",
  "3838438",
  "That was the time.",
  "OMG!",
  "😂😂😂",
  "I just can't spell.",
  "Just a little social skills.",
  "What sounds does italian dinosaurs make?",
  "I just had a bruh moment.",
  "Yeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
  "Don't click me.",
  "Gonna give you up.",
  "Baka",
  "Discord ping effect.",
  "I AM JUST TOO POOR TO BUY A NITRO.",
  "This is the footer.",
  "Write something for the embed footer.",
  "Chokolat??? WHAT ARE CHOKOLAT?",
  "Ctrl + C to force quit me.",
  "youtu.be/dQw4w9WgXcQ"
]

async def randomFooterNerdTime():
  global FOOTER
  return random.choice(FOOTER) + " | " + await getTime()

async def randomFooter():
  global FOOTER
  return random.choice(FOOTER)







async def death(ctx, who, damageInt):

  RANDOM = discord.Color.from_rgb(random.randint(20,255),random.randint(20,255),random.randint(20,255))

  gm = json.load(open("game.json"))
  amount = round(random.random() * random.randint(1, 100) * damageInt, 1)
  addon = ""
  if gm[str(who)]["nerdies"]["wallet"] >= amount:
    addon += ""
    gm[str(who)]["nerdies"]["wallet"] -= amount
    addon += "\n\nYou paid the doctor %s <:nerdies:932234563579682816>." % amount
  else:
    if genRarity(100):
      addon += "\n\nYou don't have enough money in your wallet. Instead, the doctor paied your bill! What a nice doctor!" % amount
    else:
      addon += "\n\nYou don't have enough money in your wallet. Now you owe the doctor %s <:nerdies:932234563579682816>." % amount
  embed=discord.Embed(color = RANDOM, timestamp = datetime.datetime.utcnow(), title="You died!", description = random.choice([
    "Better luck next time!",
    "The doctor revived you!",
    "Bro, you really suck.",
    "Learn how to play the game first!",
    "Hopefully the doctor save you.",
    "Seriously? How can you die?",
    "Shit.",
    ":(",
    ":/",
    "What does this all means?",
    "DIE IN A EZ GAME??? HOW???????",
    "..."
  ]) + addon)
  embed.set_footer(text="%s | " % random.choice([
    "Bruh.",
    "Dead again?",
    "Be careful!"
  ]) + await getTime())
  gm[str(who)]["deaths"] += 1
  json.dump(gm, open("game.json", "w"))
  await ctx.send(embed=embed) 



badwords = json.load(open("badwords.json"))


def has_bad_word(sentence: str):
  data = False
  pls = sentence.split(sep = " ")
  for i in badwords:
    if i in pls:
        data = True
  return data




async def isBanned(ctx, id):
  cd = json.load(open("banned.json"))
  if str(id) in cd:
    secret = base64.b64encode(cd[str(id)]["id"].encode()).decode()
    if cd[str(id)]["decision"] == 1:
      cstr = "Your account had been banned from using NerdBot. This decision is final and appeals are not accepted."
    else:
      if isinstance(ctx.channel, discord.channel.DMChannel):
        cstr = f"Your account had been banned from using NerdBot. If you believe this is an error and would like to submit an appeal, please submit an appeal [here](https://www.saltyfishstudios.net/nerd/appeal?dat={secret})"
      else:
        cstr = f"Your account had been banned from using NerdBot. If you believe this is an error and would like to submit an appeal, execute any NerdBot command in a Direct Message channel."
    embed=discord.Embed(title="Oops!", color = 0xfef200, timestamp = datetime.datetime.utcnow(), description=cstr)
    if isinstance(ctx.channel, discord.channel.DMChannel):
      if cd[str(id)]["end"] == -1:
        more = "This is a permanent ban."
      else:
        dd = datetime.datetime.utcfromtimestamp(cd[str(id)]["end"]) - datetime.datetime.utcnow()
        if dd.total_seconds() <= 0:
          embed.add_field(name="More information", value=f"**Reason**: `{cd[str(id)]['reason']}`\n**Remaining time**: `Later`\n**Ban ID**: `{cd[str(id)]['id']}`\n\nAs NerdBot only refreshes the ban list every minute, you will have to wait for about a minute if the **Remaining time** appears as `Later`.", inline=False)
        else:
          more = secToStr(int(round(dd.total_seconds(), 0)))
          embed.add_field(name="More information", value=f"**Reason**: `{cd[str(id)]['reason']}`\n**Remaining time**: `{more}`\n**Ban ID**: `{cd[str(id)]['id']}`\n\nAs NerdBot only refreshes the ban list every minute, you will have to wait for about a minute if the **Remaining time** appears as `Later`.", inline=False)
    else:
      if cd[str(id)]["end"] == -1:
        more = "This is a permanent ban."
      else:
        dd = datetime.datetime.utcfromtimestamp(cd[str(id)]["end"]) - datetime.datetime.utcnow()
        if dd.total_seconds() <= 0:
          embed.add_field(name="More information", value=f"**Reason**: `{cd[str(id)]['reason']}`\n**Remaining time**: `Later`\n\nAs NerdBot only refreshes the ban list every minute, you will have to wait for about a minute if the **Remaining time** appears as `Later`.", inline=False)
        else:
          more = secToStr(int(round(dd.total_seconds(), 0)))
          embed.add_field(name="More information", value=f"**Reason**: `{cd[str(id)]['reason']}`\n**Remaining time**: `{more}`\n\nAs NerdBot only refreshes the ban list every minute, you will have to wait for about a minute if the **Remaining time** appears as `Later`.", inline=False)
    embed.set_footer(text = random.choice([
      "Wha????",
      "oof why u got banned.",
      "Go and have an appeal.",
      "APPEAL = BEST",
      "rule breaker?",
    ]))
    await ctx.send(embed=embed)
    return True
  else:
    return False


async def checkAllows(ctx):
  global DISBALED
  if ctx.message.channel.id in DISABLED:
    return True
  else:
    return False

def inttostr(i):
    d = "{:,}".format(i)
    d = d.split(sep=",")
    lenl = ["", "K", "M", "B", "T", "Q"]
    if len(d) == 1:
        return d[0]
    return d[0] + "." + d[1][:2] + lenl[len(d) - 1]

async def checkReboot(ctx):
  global REBOOT, ONGOING_TASKS
  if REBOOT[0]:
    embed=discord.Embed(title="NerdBot is about to reboot!", description="The nerdy workers had worked a lot! Let's give them a small break!", color=0xfef200, timestamp = datetime.datetime.utcnow())
    gg = secToStr(REBOOT[1])
    if gg == "Later":
      if ONGOING_TASKS != 0:
        gg = f"Completing threaded tasks... ({ONGOING_TASKS})"
      else:
        gg = f"Later"
    embed.add_field(name = "Reboot Information", value = f"**Reboot In**: `{gg}`\n**Reboot Type**: {REBOOT[2]} *[What is this?](https://nerdbot.saltyfishstudios.net/reboots)*")
    embed.set_footer(text = "Don't worry your profile is gonna be saved!")
    await ctx.send(embed = embed)
    return True
  else:
    return False

async def rebootcountdown():
  global REBOOT, ONGOING_TASKS
  while True:
    REBOOT[1] -= 1
    if REBOOT[1] <= 0:
      if ONGOING_TASKS <= 0:
        await asyncio.sleep(60)
        os.system("bash reboot.sh")
      else:
        pass
    await asyncio.sleep(1)

async def prepareReboot(time, type):
  global REBOOT
  REBOOT[0] = True
  REBOOT[1] = time
  REBOOT[2] = type
  activity = discord.Streaming(name="NerdBot Reboot Task", url = "https://www.youtube.com/watch?v=ckcDG1j5jWo")
  await bot.change_presence(activity=activity)
  bot.loop.create_task(rebootcountdown())

bots = []
for i in range(10):
  bots.append(UserBot())
  
words = json.load(open("words.json"))

NEXT_REBOOT = 21600
ONGOING_TASKS = 0


TIME = json.load(open("time.json"))
async def updateTime():
  global SHOP_CREDITS
  global TIME
  global font
  global MARKET_GRAPH, NEXT_REBOOT
  global shop, watch
  while True:
    TIME["M"] += 1
    NEXT_REBOOT -= 1
    if NEXT_REBOOT == 0:
      await prepareReboot(60, "RAM Dump (Simple Reboot)")
    if genRarity(5):
      for i in bots:    
        i.aimoment(shop, SHOP_CREDITS)
        if genRarity(30): break
        
    if TIME["M"] == 60:
      if genRarity(10):
        for i in bots:
          i.aimoment(shop, SHOP_CREDITS)
      data = json.load(open("banned.json"))
      for i in list(data):
        if time.mktime(datetime.datetime.utcnow().timetuple()) >= data[i]["end"]:
          data.pop(i)
      json.dump(data, open("banned.json", "w"))
          
      TIME["M"] = 0
      TIME["H"] += 1
    if TIME["H"] == 24:
      for i in bots:
        i.aimoment(shop, SHOP_CREDITS)
      for i in bots:
        i.payout(random.randint(5000,20000))
      TIME["H"] = 0
      TIME["D"] += 1

      ### NEW DAY! ######################
      saveTime()
      # market refill
      market = json.load(open("market.json"))

      for x in list(market):
        d = 0
        for i in market[x]:
          d += i["amount"]
        if d < 5000:
          cost = round(market[x][0]["cost"] - 0.1, 1)
          cost = round(cost, 1)
          if cost < 0.1:
            cost = 0.1
          market[x].append({"amount": 5000, "cost": cost, "author": 898912199517556786, "timestamp": 0})
        pc = market[x]
        for i in pc:
          if i["amount"] <= 0:
            market[x].remove(i)
      json.dump(market, open("market.json", "w"))
      
      # BANK INTREST
      profiles = json.load(open("game.json"))
      banks = json.load(open("banks.json"))
      for i in profiles:
        pf = profiles[i]
        total = 0
        for x in pf["nerdies"]["bank"]:
          intrest = banks[x["name"]]["intrest"]["save"]
          intrest_money = pf["nerdies"]["bank"][pf["nerdies"]["bank"].index(x)]["amount"] * (intrest / 100)
          profiles[i]["nerdies"]["bank"][pf["nerdies"]["bank"].index(x)]["amount"] += round(intrest_money, 1)
          profiles[i]["nerdies"]["bank"][pf["nerdies"]["bank"].index(x)]["amount"] = round(profiles[i]["nerdies"]["bank"][pf["nerdies"]["bank"].index(x)]["amount"], 1)
          total += round(intrest_money, 1)
        if genRarity(0.3):
          names = [
            "Ms. Powley",
            "Ms. Brownie",
            "Mr. Yan",
            "Ms. Sussy",
            "Mr. Tang",
            "Dr. Doctor",
            "Dr. Baka",
            "Ms. Tondo",
            "Mr. Yankee",
            "Mrs. Married",
            "Mr. Banker",
            "Ms. Baker",
            "Mrs. Baker",
            "Dr. Baker",
          ]
          name = random.choice(names)
          await newNotif(int(i), f"Banker - {name}", random.choice([
            "Is this yours?",
            "You left something!",
            "Lost and found.",
            "Look what I've found!",
            "Maybe, this is yours?"
          ]), "When we are fetching money in our safe for your bank intrest, we found a Rainbow Nerdie <:rainbownerdie:932255376160751657>! Maybe it belongs to you? I placed it in your inventory!", "SYSTEM", True)
      json.dump(profiles, open("game.json", "w"))

      #### INFORM SHOP CREDITS ####
      for i in SHOP_CREDITS:
        await newNotif(int(i), "Nerd Mart", "Items sold!", "Your items that are queued to sold in NerdMart had sucessfully sold, gaining %s " % space(round(SHOP_CREDITS[i], 1)), "SYSTEM", False)
      SHOP_CREDITS = {}
      
      
    if TIME["D"] == 31:
      TIME["D"] = 0
      TIME["MN"] += 1
    if TIME["MN"] == 13:
      TIME["MN"] = 0
      TIME["Y"] += 1
    await asyncio.sleep(1)

def saveTime():
  json.dump(TIME, open("time.json", "w"))

async def getTime():
  global TIME
  return "NerdTime Year %s, %s-%s %s:%s" % (TIME["Y"], TIME["MN"], TIME["D"], TIME["H"], TIME["M"])

def genSSID():
  return binascii.b2a_hex(os.urandom(3)).decode().upper()


def genID():
  return binascii.b2a_hex(os.urandom(4)).decode().upper()

async def giveCoins(userid, amount):
  await checkAccountExsists(userid)
  x = json.load(open("game.json"))
  x[str(userid)]["nerdies"]["wallet"] += amount
  x[str(userid)]["nerdies"]["wallet"] = round(x[str(userid)]["nerdies"]["wallet"], 1)
  json.dump(x, open("game.json", "w"))

global UNTIL_NEXT
UNTIL_NEXT = {
  "0": 50.0,
  "1": 100.0,
  "2": 300.0,
  "3": 500.0,
  "4": 750.0,
  "5": 1000.0,
  "6": 1200.0,
  "7": 1500.0,
  "8": 1900.0,
  "9": 2000.0,
  "10": 3000.0,
  "11": 3500.0,
  "12": 3800.0,
  "13": 4000.0,
  "14": 4500.0,
  "15": 5000.0,
  "16+": 7500.0
}

async def giveExp(ctx, userid, amount):
  await checkAccountExsists(userid)
  x = json.load(open("game.json"))
  cs = json.load(open("user-quests.json"))
  copyofamount = amount
  while True:
    if x[str(userid)]["level"] > 15:
      this = UNTIL_NEXT["16+"]
    else:
      this = UNTIL_NEXT[str(x[str(userid)]["level"])]
    if x[str(userid)]["exp"] + amount >= this:
      x[str(userid)]["level"] += 1
      await newNotif(userid, "Nerd Jr.", "Level up!", f"Congratulations for reaching **Level `{x[str(userid)]['level']}`**!", "SYSTEM", True)
      amount -= (this - x[str(userid)]["exp"])
      x[str(userid)]["exp"] = 0
    else:
      amount -= (this - x[str(userid)]["exp"])
      x[str(userid)]["exp"] = this + amount
      x[str(userid)]["exp"] = round(x[str(userid)]["exp"], 1)
      break
  have_actions = False
  for i in cs[str(userid)]["objective"]:
    if i["type"] == "gain-exp":
      have_actions = True
      cs[str(userid)]["objective"][cs[str(userid)]["objective"].index(i)]["current"] += copyofamount
      cs[str(userid)]["objective"][cs[str(userid)]["objective"].index(i)]["current"] = round(cs[str(userid)]["objective"][cs[str(userid)]["objective"].index(i)]["current"], 1)
  falses = 0
  for i in cs[str(userid)]["objective"]:
    if i["current"] >= i["goal"] and not cs[str(userid)]["completed"]:
      pass
    else:
      falses += 1
  if falses <= 0:
    for i in cs[str(userid)]["rewards"]:
      if i["type"] == "next-stage":
        cs[str(userid)]["stage"] += 1
        cs[str(userid)]["completed"] = True
        json.dump(cs, open("user-quests.json", "w"))
        await startQuest(ctx, userid, cs[str(userid)]["name"], isNextStage = True)
      
  if have_actions:
    json.dump(cs, open("user-quests.json", "w"))
  json.dump(x, open("game.json", "w"))

def genRarity(percent_of_occuring):
  return random.choices([True, False], [percent_of_occuring, 100 - percent_of_occuring])[0]

################# BOT COMMANDS #############################################################

def space(integer):
  return "{:,}".format(integer)

  


@bot.event
async def on_ready():

  global DEV
  DEV = False

  global bot
  DiscordComponents(bot)

  global BOT_RUNNING
  BOT_RUNNING = True

  print("Nerd is ready.")
  activity = discord.Game(name="bruh help for help!")
  await bot.change_presence(activity=activity)

  bot.loop.create_task(updateTime())
  
"""
   
  ctx = bot.get_channel(915542406865248276)

  await ctx.purge(limit = 10)

  

  embed=discord.Embed(title="Verify your Account! :white_check_mark:", description="[US] Click the check mark below to verify your account and join the server!\n[CN] 点击下面的绿色对勾来证实您的discord账户\n[CN] 單擊下面的複選標記以驗證您的帳戶並加入服務器。\n[JP] 下のチェックマークをクリックしてアカウントを確認し、サーバーに参加してください。\n[KR] 아래 체크 표시를 클릭하여 계정을 확인하고 서버에 가입하세요.\n[RU] Щелкните галочку ниже, чтобы подтвердить свою учетную запись и присоединиться к серверу.\n[FR] Cliquez sur la coche ci-dessous pour vérifier votre compte et rejoindre le serveur.", color=0xfef200, timestamp = datetime.datetime.utcnow())
  embed.set_footer(text = "If there are any language mistakes, sorry for that, but I use google translate lol\nIf I am offline or unaccessable, please contact any server admins or moderators to manually verify your account.")
  msg = await ctx.send(embed = embed)
  await msg.add_reaction("✅")
  ctx = bot.get_channel(926002835479490610)

  await ctx.purge(limit = 10)

  embed=discord.Embed(title="Verify your Account! :white_check_mark:", description="[US] Click the check mark below to verify your account and join the server!\n[CN] 点击下面的绿色对勾来证实您的discord账户\n[CN] 單擊下面的複選標記以驗證您的帳戶並加入服務器。\n[JP] 下のチェックマークをクリックしてアカウントを確認し、サーバーに参加してください。\n[KR] 아래 체크 표시를 클릭하여 계정을 확인하고 서버에 가입하세요.\n[RU] Щелкните галочку ниже, чтобы подтвердить свою учетную запись и присоединиться к серверу.\n[FR] Cliquez sur la coche ci-dessous pour vérifier votre compte et rejoindre le serveur.", color=0xfef200, timestamp = datetime.datetime.utcnow())
  embed.s  et_footer(text = "If there are any language mistakes, sorry for that, but I use google translate lol\nIf I am offline or unaccessable, please contact any server admins or moderators to manually verify your account.")
  msg = await ctx.send(embed = embed)
  await msg.add_reaction("✅")

  """
  

  




@bot.event
async def on_guild_join(guild):
  for channel in guild.text_channels:
      if channel.permissions_for(guild.me).send_messages:
        embed=discord.Embed(color = 0xfef200, timestamp = datetime.datetime.utcnow(), title="Thank you for adding **Nerd** to your discord server!", description = f"Hello guys! I am, **NerdBot**, or you can call me **Nerd**. Any time you want to use an command on me, remember to add an `bruh` **plus space**, thats my command prefix! To find out some commands, execute the `bruh help` command. If you would like to continue this as a story, maybe you should try the first introduction quest (`bruh quest start introduction`).\n\nHave fun playing with the bot!")
        embed.set_footer(text="Relizc#6918")
        await channel.send(embed=embed)
        break



def checkPerm(id):
  if id in DEBUG_WHITELIST:
    return True
  else:
    return False





def mentionToId(string):
  return int(string.replace("<", "").replace(">", "").replace("!", "").replace("@", ""))


















    

##################### ADMIN COMMANDS ########################################################################
@bot.command(name = "admin.executePythonCommand")
async def _admin1(ctx):

  if await checkReboot(ctx): return

  await ctx.send(ctx.author.__dict__)




@bot.command(name = "admin.sendShopCredits")
async def _admin2(ctx, *args):

  if not checkPerm(ctx.author.id):
    return
    
  global SHOP_CREDITS
  for i in SHOP_CREDITS:
    await newNotif(int(i), "Nerd Mart", "Items sold!", "Remember that you sold stuff in NerdMart? Most are sold resulting in: %s <:nerdies:932234563579682816>. If you want to know how much are left, use the command `bruh market orders`." % space(SHOP_CREDITS[i]), "SYSTEM", True)









@bot.command(name = "admin.sendRules")
async def _admin3(ctx):

  if await checkReboot(ctx): return

  if not checkPerm(ctx.author.id):
    return
    
  embed=discord.Embed(color = 0xfef200, title="Welcome To Nerd's Official Discord Server!", description="This is the official NerdBot server, where you can view the updates, communicate or chat with others about anything of NerdBot. You can even get support if you are needed. For more information, please view the points below:")
  embed.add_field(name="Rules", value="For the rules of the server, please check <#926000028194066442>.", inline=False)
  embed.add_field(name="Verification", value="Verification is needed to fully join the server. Not just only verifying your email, you will need to do a very simple check to confirm you are not a bot. For more, please check <#926002835479490610>.", inline=False)
  embed.add_field(name="Consequences", value="If you do not follow rules, you will have punishments. Again check <#926000028194066442>.", inline=False)
  embed.add_field(name="Support and FAQs", value="We have a channel for it! Please view <#926004991590817833>.\n\nThis is all what we want to say to you, and now, go have fun!", inline=False)
  await ctx.send(embed=embed)



@bot.command(name = "admin.purgechannel")
async def _admin4(ctx, limit):

  if await checkReboot(ctx): return

  if not checkPerm(ctx.author.id):
    return
    
  await ctx.channel.purge(limit = int(limit))



@bot.command(name = "admin.ban")
async def _admin5(ctx, user, reason):

  if await checkReboot(ctx): return

  if not checkPerm(ctx.author.id):
    return
    
  ban(mentionToId(user), reason, datetime.timedelta(days=10))
  await ctx.send("`0`")

@bot.command(name = "admin.reboot")
async def _admin6(ctx, time = 60, type = "Simple Reboot"):

  if await checkReboot(ctx): return

  if not checkPerm(ctx.author.id):
    return

  await prepareReboot(time, type)
    
  await ctx.send(f"Rebooted ({time} / {type})")

@bot.command(name = "admin.giveitem")
async def _admin6(ctx, user = 0, id = "NONE", amount = 0):

  if await checkReboot(ctx): return

  if not checkPerm(ctx.author.id):
    return

  if user == 0 or id == "NONE" or amount == 0:
    await ctx.send("Invalid Arguments")

  


  










def secToStr(seconds):
  x = datetime.timedelta(seconds = seconds)
  x = str(x).replace(" ", "").replace("days", "").replace("day", "").split(sep = ",")
  if seconds <= 0:
    return "Later"
  if len(x) >= 2:
    d = int(x[0])
  else:
    d = 0
  if len(x) >= 2:
    hms = x[1].split(sep = ":")
  else:
    hms = x[0].split(sep = ":")
  if int(hms[2]) <= 0:
    s = 0
  else:
    s = int(hms[2])
  if int(hms[1]) <= 0:
    m = 0
  else:
    m = int(hms[1])
  if int(hms[0]) <= 0:
    h = 0
  else:
    h = int(hms[0])
  li = []
  if d == 0:
    ds = ""
  else:
    ds = f"{d} day(s)"
    li.append(ds)
  if h == 0:
    hs = ""
  else:
    hs = f"{h} hour(s)"
    li.append(hs)
  if m == 0:
    ms = ""
  else:
    ms = f"{m} minute(s)"
    li.append(ms)
  if s == 0:
    ss = ""
  else:
    ss = f"{s} second(s)"
    li.append(ss)
  return " ".join(li)

TAGS = {}

def tag(user, name, data):
  global TAGS
  TAGS[str(user)] = {}
  TAGS[str(user)][name] = data
  return True

def untag(user, name):
  global TAGS
  if not str(user) in TAGS:
    return False
  elif not name in TAGS[str(user)]:
    return False
  else:
    for i in list(TAGS[str(user)]):
      if i == name:
        TAGS[str(user)].pop(name)
      if len(TAGS[str(user)]) <= 0:
        TAGS.pop(str(user))
    return True

def hastag(user, name):
  global TAGS
  if not str(user) in TAGS:
    return False
  else:
    return name in TAGS[str(user)]

def hastagdata(user, name, data):
  global TAGS
  if not str(user) in TAGS:
    return False
  elif not name in TAGS[str(user)]:
    return False
  else:
    return TAGS[str(user)][name] == data


  

@bot.event
async def on_reaction_add(reaction, user):
  if user.bot == True:
    return
  else:
      
    if reaction.message.channel.id == 915542406865248276:
      if reaction.emoji == "✅":
        for roles in user.roles:
          if roles.name == "Member":
            await reaction.message.remove_reaction(reaction, user)
            return
        guild = bot.get_guild(897095973933838416)
        role = get(guild.roles, name = "Member")
        await user.add_roles(role)
        embed=discord.Embed(title="Thank you!", description="You have sucessfully verified your profile in Hypixel Gamers!\nBut you will need to click that check mark again if you are removed from the server in any way (being kicked, or leave by yourself)", color=0xfbff00, timestamp = datetime.datetime.utcnow())
        embed.set_footer(text="Welcome to Hypixel Gamers!")
        await user.send(embed = embed)
        await reaction.message.remove_reaction(reaction, user)
      else:
        await reaction.message.remove_reaction(reaction, user)
    elif reaction.message.channel.id == 926002835479490610:
      if reaction.emoji == "✅":
        for roles in user.roles:
          if roles.name == "Member":
            await reaction.message.remove_reaction(reaction, user)
            return
        guild = bot.get_guild(924506697618317402)
        role = get(guild.roles, name = "Member")
        await user.add_roles(role)
        embed=discord.Embed(title="Thank you!", description="You have sucessfully verified your profile in out discord server, but you will need to click that check mark again if you are removed from the server in any way (being kicked, or leave by yourself)", color=0xfbff00, timestamp = datetime.datetime.utcnow())
        embed.set_footer(text="Welcome to Nerd's Official Discord Server!")
        await user.send(embed = embed)
        await reaction.message.remove_reaction(reaction, user)
      else:
        await reaction.message.remove_reaction(reaction, user)
    else:
      return


LIST_OF_RICKROLL = [
  "https://www.youtube.com/watch?v=oHg5SJYRHA0",
  "https://www.youtube.com/watch?v=6_b7RDuLwcI",
]






@bot.event
async def on_command_error(ctx, error):
  
  if isinstance(error, commands.CommandOnCooldown):
    RANDOM = discord.Color.from_rgb(random.randint(20,255),random.randint(20,255),random.randint(20,255))
    timing = secToStr(int(round(error.retry_after, 0)))
    if timing == None:
      timing = "Error"
    else:
      pass
    embed=discord.Embed(color = RANDOM, timestamp = datetime.datetime.utcnow(), title=random.choice([
      "Yoooooooo too speedy.",
      "Way too fast!",
      "Speed limit!",
      "Step on brakes!",
      "Nerd goes brrrrrrrr...",
      "SKEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEETCH",
      "SLOW DOWN!!!!",
      ":sloth:",
      "Lightning speed?",
      ":children_crossing: CHILDREN CROSSING!!!!!",
      "Be a sloth."
    ]), description=random.choice([
      "C'mon, don't be too fast.",
      "Slow it down bro!",
      "Perhaps you should slow it down!",
      "Don't ride a :rocket:.",
      "LOWER DOWN YOUR SPEED!",
      "Please, lower your speed[.](https://www.youtube.com/watch?v=dQw4w9WgXcQ)"
    ]) + "\n" + random.choice([
      "Use this again in",
      "Try again in",
      "Dowit again in",
      "Next use time in",
      "SEND IT AGAIN IN",
      "Bruh do it again in"
    ]) + f" `{timing}`")
    embed.set_footer(text=random.choice([
      "Speedy Boi?",
      "Fast?"
    ]))
    await ctx.send(embed=embed)
  elif isinstance(error, commands.CommandNotFound):
    pass
  else:
    await ctx.send(f"Sorry, an **Internal Error** occured while handling your request! Please try again!\n```{str(traceback.format_exc())[0:64]}...```")
    raise error



CHARADES_GAME = {}
CHARADES_WORDS = [
  "apple",
  "banana",
  "moneky",
  "television",
  "computer",
  "sound",
  "wavelength",
  "weather",
  "proton",
  "neutron",
  "electron",
  "supersonic",
  "doge",
  "summer",
  "spring",
  "autumn",
  "winter",
  "supercalifragilisticexpialidocious",
  "bruh",
  "development",
  "poop",
  "pee",
  "unique",
  "sad",
  "joyfulness",
  "copyright",
  "soccerway",
  "doobiest",
  "idiot",
  "water",
  "hard-drive",
  "funky",
  "corny",
  "anmie",
  "girlfriend",
  "boyfriend",
  "console",
  "hangman",
  "charades",
  "pink",
  "pig",
  "animal",
  "cars",
  "words",
  "doggo",
  "candy",
  "machine-gun",
  "mouse",
  "matrix",
  "mate",
  "piano",
  "lazy",
  "length",
  "vector"
]


























COMMAND_AS = {'_quest': 'bruh quest','_charades': 'bruh charades','_reset': 'bruh reset','_plot': 'bruh plot','_consume': 'bruh consume','_bounty': 'bruh bounty','_yt': 'bruh youtube','_word': 'bruh vocabulary','_make5': 'bruh make5','_disablerick': 'bruh disablerick','_enablerick': 'bruh enablerick','rickroll': 'bruh rickroll','poop': 'bruh poop','_message': 'bruh send','Notifis': 'bruh notifications','profile': 'bruh profile','checkInventory': 'bruh inventory','withdrawFromBank': 'bruh withdraw','helpOnCommand': 'bruh help','NerdMart': 'bruh market','_sell': 'bruh sell','OpenWebSite': 'bruh site','guessmynumber': 'bruh guessmynumber','guesscoin': 'bruh guesscoin','hangman': 'bruh hangman','menu': 'bruh menu','apikey': 'bruh api','newpoll': 'bruh newpoll','postpoll': 'bruh postpoll'}



quests = json.load(open("quests.json"))

async def startQuest(ctx, user_id, quest_id, isNextStage = False):
  global quests

  data = json.load(open("user-quests.json"))
  if isNextStage:
    embed=discord.Embed(color = 0xfbff00, title="Quest objective complete!", description="You completed all of your quest objectives! Execute the `bruh quest continue` command tp continue on your quest!")
    objstr = ""
    rewstr = ""
    for i in data[str(user_id)]["objective"]:
      if i['type'] == "command-execute":
        objstr += f":white_check_mark: Execute command `{COMMAND_AS[i['data']]}` **({i['current']}/{i['goal']})**\n"
      if i['type'] == "gain-exp":
        objstr += f":white_check_mark: Gain Experience <a:exp:913753763959939092> **({i['current']}/{i['goal']})**\n"
    for i in data[str(user_id)]["rewards"]:
      if i['type'] == "next-stage":
        rewstr += f"Contine the quest\n"
    embed.add_field(name="Objective", value=objstr, inline=True)
    embed.add_field(name="Rewards", value=rewstr, inline=True)
    await ctx.send(embed=embed)
    return
  target = None
  for i in quests:
    for x in quests[i]["data"]:
      if x["name"] == quest_id:
        target = x
  if target == None:
    raise NameError(
      "Quest ID not found."
    )
  data[str(ctx.author.id)]["completed"] = False
  json.dump(data, open("user-quests.json", "w"))
  for i in target["actions"][data[str(user_id)]["stage"]]:
    if i["type"] == "dialogue":
      string = i["data"].format(username = ctx.author.name, userid = ctx.author.id)
      await ctx.send(string)
    elif i["type"] == "wait":
      await asyncio.sleep(i["data"])
    elif i["type"] == "pass":
      pass
    elif i["type"] == "decision":
      obj = i["data"]["statement"].split(sep=" ")
      target = obj[0]
      state = obj[1]
      amount = obj[2]
      boolean = False
      if target == "userWalletNerdies":
        target = json.load(open('game.json'))[str(ctx.author.id)]["nerdies"]["wallet"]
      if state == "<":
        boolean = target < int(amount)
      if state == ">":
        boolean = target > int(amount)
      if state == "<=":
        boolean = target <= int(amount)
      if state == ">=":
        boolean = target >= int(amount)

      if boolean:
        for x in i["data"]["true"]:
          if x["type"] == "dialogue":
            string = x["data"].format(username = ctx.author.name, userid = ctx.author.id)
            await ctx.send(string)
          elif x["type"] == "wait":
            await asyncio.sleep(x["data"])
          elif x["type"] == "pass":
            pass
          elif x["type"] == "objective-set":
            raise RecursionError(
              "Cannot set objective in decision steps."
            )
          elif i["type"] == "decision":
            raise RecursionError(
              "Cannot use decision in decision steps."
            )
      else:
        for x in i["data"]["true"]:
          if x["type"] == "dialogue":
            string = x["data"].format(username = ctx.author.name, userid = ctx.author.id)
            await ctx.send(string)
          elif x["type"] == "wait":
            await asyncio.sleep(x["data"])
          elif x["type"] == "pass":
            pass
          elif x["type"] == "objective-set":
            raise RecursionError(
              "Cannot set objective in decision steps."
            )
          elif x["type"] == "decision":
            raise RecursionError(
              "Cannot use decision in decision steps."
            )
    elif i["type"] == "objective-set":
      embed=discord.Embed(color = 0xfbff00, title="New quest objective!", description="Your quest objective had been updated!")
      data = json.load(open("user-quests.json"))
      objstr = ""
      rewstr = ""
      rewardlist = []
      data[str(user_id)]["objective"] = []
      data[str(user_id)]["rewards"] = []
      for x in i["data"]["objectives"]:
        if x["type"] == "command-execute":
          data[str(user_id)]["objective"].append({"type": x["type"], "data": x['data'], "current": 0, "goal": x["times"]})
        if x["type"] == "gain-exp":
          data[str(user_id)]["objective"].append({"type": x["type"], "data": x['data'], "current": 0.0, "goal": x["times"]})
      for n in i["data"]["rewards"]:
        if n["type"] == "next-stage":
          rewardlist.append({"type": "next-stage", "data": n["data"]})
          rewstr += "Continue the quest\n"
      data[str(user_id)]["rewards"] = rewardlist
      for x in data[str(user_id)]["objective"]:
        if x["type"] == "command-execute":
          objstr += f":x: Execute command `{COMMAND_AS[x['data']]}` **({x['current']}/{x['goal']})**\n"
        if x["type"] == "gain-exp":
          objstr += f":x: Gain Experience <a:exp:913753763959939092> **({x['current']}/{x['goal']})**\n"
      embed.add_field(name="Objective", value=objstr, inline=True)
      embed.add_field(name="Rewards", value=rewstr, inline=True)

      json.dump(data, open("user-quests.json", "w"))

      
      await ctx.send(embed=embed)













@bot.command(aliases = ["items", "item", "listitem"])
async def _items(ctx, specific = None):

  if await checkReboot(ctx): return

  if await isBanned(ctx, ctx.author.id): return

  L = LANG(ctx.author.id)

  if specific != None:
    try:
      target = items[specific.upper()]
    except KeyError:
      await ctx.send(L.LANG(random.choice(["commands.items.unexsist.random.0", "commands.items.unexsist.random.1", "commands.items.unexsist.random.2", "commands.items.unexsist.random.3"])))
      return
    embed=discord.Embed(timestamp = datetime.datetime.now(), color = 0xfbff00, title=f"**{L.LANG(target['displayName'])}**", description = f"{target['rarietyImage']} {target['image']} **{L.LANG(target['displayName'])}** `{target['name']}`")
    embed.set_thumbnail(url=target["thumbnail"])
    embed.add_field(name="Detailed Description", value = L.LANG(target["detailed_description"]), inline = False)
    pockstr = ""
    if target["pocket_abilities"] == None:
      pockstr = L.LANG("commands.items.pocketabilities.null") 
    else:
      for i in target["pocket_abilities"]:
        pockstr += f'{pockets[i]["image"]} **{L.LANG(pockets[i]["displayName"])}** `(Chance: {pockets[i]["chance"]}%)`\n - {L.LANG(pockets[i]["description"])}\n'
    embed.add_field(name=L.LANG("commands.items.pocketabilities.title"), value = pockstr, inline = False)
    rarietyHash = {"0": L.LANG("general.items.rarity.0"), "1": L.LANG("general.items.rarity.1"), "2": L.LANG("general.items.rarity.2"), "3": L.LANG("general.items.rarity.3"), "4": L.LANG("general.items.rarity.4")}
    embed.add_field(name="Statistics", value = f'**Name:** {L.LANG(target["displayName"])}\n**ID:** `{target["name"]}`\n**Instant sell price:** `{space(target["cost"])}` <:nerdies:932234563579682816>\n**Rariety:** `{L.LANG(rarietyHash[str(target["rariety"])])}`', inline = False)
    embed.set_footer(text = await randomFooter())
    await ctx.send(embed=embed)
    return
      
  string = L.LANG("commands.items.description.0")
  for i in items:
    string += f"{items[i]['rarietyImage']} {items[i]['image']} **{L.LANG(items[i]['displayName'])}** `{i}` - {space(items[i]['cost'])} <:nerdies:932234563579682816>\n"
  embed=discord.Embed(timestamp = datetime.datetime.utcnow(), color = 0xfbff00, title=L.LANG("commands.items.title"), description=string)
  embed.set_footer(text=await randomFooter())
  amt = 0
  msg = await ctx.send(embed=embed, components = [Select(placeholder = L.LANG("commands.items.sorter.placeholder"), custom_id = "sortby", options = [
    SelectOption(label = L.LANG("commands.items.sorter.regular"), emoji = emoji.emojize(":scroll:", use_aliases=True), value = "0"),
    SelectOption(label = L.LANG("commands.items.sorter.instprice"), emoji = emoji.emojize(":coin:", use_aliases=True), value = "1"),
    SelectOption(label = L.LANG("commands.items.sorter.rarity"), emoji = emoji.emojize(":gem:", use_aliases=True), value = "2"),
    SelectOption(label = L.LANG("commands.items.sorter.alphaname"), emoji = emoji.emojize(":abc:", use_aliases=True), value = "3"),
    SelectOption(label = L.LANG("commands.items.sorter.alphaid"), emoji = emoji.emojize(":abc:", use_aliases=True), value = "4")
  ])])
  while True:
    try:
      res = await bot.wait_for("select_option", check = lambda i: i.message.id == msg.id, timeout = 20)
      amt += 1
      if res.user.id != ctx.author.id:
        await res.send(L.LANG("general.interaction.fail.no_permission"))
        continue
      if res.values[0] == "0":
        dat = items.keys()
      elif res.values[0] == "1":
        dat = sorted(items, key = lambda i: items[i]["cost"])
      elif res.values[0] == "2":
        dat = sorted(items, key = lambda i: items[i]["rariety"])
      elif res.values[0] == "3":
        dat = sorted(items, key = lambda i: items[i]["displayName"])
      elif res.values[0] == "4":
        dat = sorted(items, key = lambda i: items[i]["name"])
      string = L.LANG("commands.items.description.0")
      for i in dat:
        string += f"{items[i]['rarietyImage']} {items[i]['image']} **{L.LANG(items[i]['displayName'])}** `{i}` - {space(items[i]['cost'])} <:nerdies:932234563579682816>\n"
      embed=discord.Embed(timestamp = datetime.datetime.utcnow(), color = 0xfbff00, title=L.LANG("commands.items.title"), description=string)
      embed.set_footer(text=await randomFooter())
      await res.edit_origin(embed= embed)
      if amt >= 10:
        raise asyncio.exceptions.TimeoutError("0")
      continue
    except asyncio.exceptions.TimeoutError:
      await msg.edit(components = [Select(placeholder = L.LANG("commands.items.sorter.placeholder"), custom_id = "sortby", disabled = True, options = [SelectOption(label = L.LANG("general.interaction.fail.disabled"), emoji = emoji.emojize(":astonished:", use_aliases=True), value = "0")])])
      return










@bot.command(aliases=["quests", "quest"])
async def _quest(ctx, arg1 = None, arg2 = None):

  if await checkReboot(ctx): return
  
  if await isBanned(ctx, ctx.author.id): return

  L = LANG(ctx.author.id)

  global quests
  global items

  await checkAccountExsists(ctx.author.id)

  profile = json.load(open("game.json"))

  if arg1 == "progress":
    data = json.load(open("user-quests.json"))
    objstr = ""
    rewstr = ""
    try:
      cc = data[str(ctx.author.id)]["objective"]
    except KeyError:
      embed=discord.Embed(color = 0xfbff00, title=L.LANG("commands.quest.title.progress"), description=L.LANG("commands.quest.description.noquestactive"))
      await ctx.send(embed=embed)
      return
    embed=discord.Embed(color = 0xfbff00, title=L.LANG("commands.quest.title.progress"), description=L.LANG("commands.quest.description.questactive"))
    for i in cc:
      if i["type"] == "command-execute":
        if i["current"] >= i["goal"]:
          objstr += f":white_check_mark: {L.LANG('commands.quest.goals.command_execute')} `{COMMAND_AS[i['data']]}` **({i['current']}/{i['goal']})**\n"
        else:
          objstr += f":x: {L.LANG('commands.quest.goals.command_execute')} `{COMMAND_AS[i['data']]}` **({i['current']}/{i['goal']})**\n"
      if i["type"] == "gain-exp":
        if i["current"] >= i["goal"]:
          objstr += f":white_check_mark: {L.LANG('commands.quest.goals.gain_exp')} <a:exp:913753763959939092> **({i['current']}/{i['goal']})**\n"
        else:
          objstr += f":x: {L.LANG('commands.quest.goals.gain_exp')} <a:exp:913753763959939092> **({i['current']}/{i['goal']})**\n"
    embed.add_field(name=L.LANG('commands.quest.goals.name'), value=objstr, inline=True)
    for i in data[str(ctx.author.id)]["rewards"]:
      if i["type"] == "next-stage":
        rewstr += L.LANG('commands.quest.rewards.next_stage') + "\n"
    embed.add_field(name=L.LANG('commands.quest.rewards.name'), value=rewstr, inline=True)
    await ctx.send(embed=embed)
    return

  if arg1 == "continue":
    try:
      data = json.load(open("user-quests.json"))
      cc = data[str(ctx.author.id)]
      if not data[str(ctx.author.id)]["completed"]:
        await ctx.send(L.LANG(random.choice([
          "commands.quest.continue.fail.0",
          "commands.quest.continue.fail.1",
          "commands.quest.continue.fail.2"
        ])))
        return
    except KeyError:
      await ctx.send(L.LANG(random.choice([
        "commands.quest.continue.fail.3",
        "commands.quest.continue.fail.4",
        "commands.quest.continue.fail.5",
        "commands.quest.continue.fail.6"
      ])))
      return
    await startQuest(ctx, ctx.author.id, cc["name"])
    return


  if arg1 == "start":
    data = json.load(open("user-quests.json"))
    try:
      if data[str(ctx.author.id)] != None:
        await ctx.reply(L.LANG("commands.quest.start.fail." + random.choice(
          list("01234")
        )))
        return
    except:
      pass
    if arg2 == None:
      await ctx.reply(L.LANG("commands.quest.start.fail." + random.choice(
          list("567")
        )))
      return
    id = arg2.upper()
    target = None
    for i in list(quests):
      for x in quests[i]["data"]:
        if x["name"] == id:
          target = x
          break
    if target == None:
      await ctx.reply(L.LANG("commands.quest.start.fail." + random.choice(
          ["8", "9", "10"]
        )))
      return
    embed=discord.Embed(color = 0xfbff00, title=f"{L.LANG('commands.quest.start.confirm.title')} - **{L.LANG(target['displayName'])}** `{target['name']}`", description=f"{L.LANG(target['description'])}\n\n**{L.LANG('commands.quest.start.authorby')}**: {target['author']}")
    costStr = ""
    for i in list(target["startFee"]):
      if i == "nerdies":
        costStr += f"**{L.LANG('general.nerdies.name')}** <:nerdies:932234563579682816>: {space(target['startFee']['nerdies'])}\n"
      else:
        costStr += f"**{items[i]['displayName']}** {items[i]['image']}: {space(target['startFee'][i])}\n"
    embed.add_field(name=L.LANG('commands.quest.start.confirm.costs'), value=costStr, inline=True)
    rewardStr = ""
    for i in list(target["endFee"]):
      if i == "nerdies":
        rewardStr += f"**{L.LANG('general.nerdies.name')}** <:nerdies:932234563579682816>: {space(target['endFee']['nerdies'])}\n"
      elif i == "exp":
        rewardStr += f"**{L.LANG('general.expierence.name')}** <a:exp:913753763959939092>: {space(target['endFee']['exp'])}\n"
      else:
        rewardStr += f"**{L.LANG(items[i]['displayName'])}** {items[i]['image']}: {space(target['endFee'][i])}\n"
    embed.add_field(name=L.LANG('commands.quest.rewards.name'), value=rewardStr, inline=True)
    msg = await ctx.send(embed=embed, components=[Button(style = ButtonStyle.green, label = L.LANG('commands.quest.start.confirm.title'), custom_id = "start")])
    try:
      errs = 0
      while True:
        click = await bot.wait_for("button_click", check = lambda i: i.message.id == msg.id, timeout = 30)
        if click.user.id != ctx.author.id:
          await click.send(L.LANG("general.interaction.fail.no_permission"))
          errs += 1
          if errs > 5:
            raise asyncio.exceptions.TimeoutError("False")
        else:
          await msg.edit(components=[Button(style = ButtonStyle.green, label = L.LANG('commands.quest.start.confirm.title'), disabled=True)])
          profile = json.load(open("game.json"))
          requirelist = {}
          fill = {}
          for i in list(target['startFee']):
            if i == "nerdies":
              if profile[str(ctx.author.id)]["nerdies"]["wallet"] < target['startFee']["nerdies"]:
                requirelist["nerdies"] = target['startFee']["nerdies"] - profile[str(ctx.author.id)]["nerdies"]["wallet"]
            else:
              dat = [x for x in profile[str(ctx.author.id)]["inventory"] if x["name"] == i]
              for x in dat:
                if len(dat) <= 0:
                  fill[x["name"]] = 0
                elif x["name"] in list(fill):
                  fill[x["name"]] += x["amount"]
                else:
                  fill[x["name"]] = x["amount"]
          for i in list(fill):
            requirelist[i] = target["startFee"][i] - fill[i]
          requireStr = ""
          for i in requirelist:
            if i == "nerdies":
              requireStr += f"**{L.LANG('general.nerdies.name')}** <:nerdies:932234563579682816>: {requirelist['nerdies']} ({L.LANG('commands.quest.start.fail.insufficientnerdies')})\n" % (profile[str(ctx.author.id)]['nerdies']['wallet'])
            else:
              if requirelist[i] > 0:
                requireStr += f"**{L.LANG(items[i]['displayName'])}** {items[i]['image']}: {requirelist[i]} ({L.LANG('commands.quest.start.fail.insufficientitems')})\n" % fill[i]
          if requireStr != "":
            embed=discord.Embed(color=0xfef200, title=L.LANG('commands.quest.start.fail.title'), description=L.LANG('commands.quest.start.fail.description') + requireStr)
            await click.send(embed=embed, ephemeral = False)
            return
          embed=discord.Embed(color =0xfef200, title=L.LANG('commands.quest.start.sucess.title'), description=L.LANG('commands.quest.start.sucess.description'))
          await click.send(embed=embed, ephemeral = False)
          data = json.load(open("user-quests.json"))
          data[str(ctx.author.id)] = {"name": target["name"], "stage": 0, "startTime": int(time.mktime(datetime.datetime.utcnow().timetuple())), "objective": [], "rewards": [], "completed": False}
          json.dump(data, open("user-quests.json", "w"))

          await startQuest(ctx, ctx.author.id, target["name"])

    except asyncio.exceptions.TimeoutError:
      await msg.edit(components=[Button(style = ButtonStyle.green, label = L.LANG('commands.quest.start.confirm.title'), disabled=True)])
      return
    return

  embed=discord.Embed(color = 0xfef200, title= L.LANG("commands.quest.menu.title") % ctx.author.name, description=L.LANG("commands.quest.menu.description"))
  for i in list(quests):
    string = ""
    qcount = 0
    for x in list(quests[i]["data"]):
      if x["name"] in profile[str(ctx.author.id)]["questMilestone"]:
        string += f":white_check_mark: **{L.LANG(x['displayName'])}** `{x['name']}`\n"
      else:
        string += f":grey_question: **{L.LANG(x['displayName'])}** `{x['name']}`\n"
      qcount += 1
      if qcount > 4:
        break
    string += L.LANG("commands.quest.menu.list.more") % (len(list(quests[i]['data'])) - qcount)
    embed.add_field(name=f"**{L.LANG(x['displayName'])}** `{i}`", value = string)
  await ctx.send(embed=embed)












@bot.command(aliases = ["reset", "resetprofile"])
@commands.cooldown(1, 86400, commands.BucketType.user) 
async def _reset(ctx):

  if await checkReboot(ctx): return

  L = LANG(ctx.author.id)

  profile = json.load(open("game.json"))
  if not str(ctx.author.id) in profile:
    await ctx.send("What? Who are you? Did you have a profile?")
    return

  embed=discord.Embed(title=L.LANG("commands.reset.title"), description=L.LANG("commands.reset.description"), color=0xff0000)
  msg1 = await ctx.send(embed=embed, components = [Button(style=ButtonStyle.gray, label=L.LANG("commands.reset.button.disabled") % 5, disabled = True)])
  await asyncio.sleep(1)
  await msg1.edit(components = [Button(style=ButtonStyle.gray, label=L.LANG("commands.reset.button.disabled") % 4, disabled = True)])
  await asyncio.sleep(1)
  await msg1.edit(components = [Button(style=ButtonStyle.gray, label=L.LANG("commands.reset.button.disabled") % 3, disabled = True)])
  await asyncio.sleep(1)
  await msg1.edit(components = [Button(style=ButtonStyle.gray, label=L.LANG("commands.reset.button.disabled") % 2, disabled = True)])
  await asyncio.sleep(1)
  await msg1.edit(components = [Button(style=ButtonStyle.gray, label=L.LANG("commands.reset.button.disabled") % 1, disabled = True)])
  await asyncio.sleep(1)
  await msg1.edit(components = [Button(style=ButtonStyle.red, label=L.LANG("commands.reset.button.ready"), custom_id = "VERYFUCKINGSURE")])
  try:
    errs = 0
    while True:
      gg = await bot.wait_for("button_click", check = lambda i: i.custom_id == "VERYFUCKINGSURE", timeout = 15)
      if gg.user.id != ctx.author.id:
        errs += 1
        await gg.send(L.LANG("general.interaction.fail.no_permission"))
        if errs >= 5:
          await msg1.edit(components = [Button(style=ButtonStyle.gray, label=L.LANG("commands.reset.button.ready"), disabled = True)])
      else:
        profile = json.load(open("game.json"))
        profile.pop(str(ctx.author.id))
        json.dump(profile, open("game.json", "w"))
        await gg.send(L.LANG("commands.reset.sucess"), ephemeral = False)
        await msg1.edit(components = [Button(style=ButtonStyle.gray, label=L.LANG("commands.reset.button.ready"), disabled = True)])
        return
  except asyncio.exceptions.TimeoutError:
    await msg1.edit(components = [Button(style=ButtonStyle.gray, label=L.LANG("commands.reset.button.ready"), disabled = True)])














@bot.command(name = "report")
@commands.cooldown(1, 1, commands.BucketType.user) 
async def report(ctx, arg1 = None):

  if arg1 == None:
    await ctx.send("You need to mention a user to report! Usage: `bruh report <mention a user>`")
    return

  try:
    id = int(arg1.replace("<", "").replace(">", "").replace("@", "").replace("!", ""))
  except ValueError:
    await ctx.send("Please mention a valid user!")
    return

  if id == ctx.author.id:
    await ctx.send("You can't report yourself! Unless you did something wrong.")
    return

  user = bot.get_user(id)

  if user.bot:
    await ctx.send("I'm sure that bots won't do anything bad, right?")
    return

  m1 = await ctx.send("Please pick a reason for reporting:", components = [
    Select(
        placeholder = "Pick a reason...",
        options = [
          SelectOption(label = "Scamming", value = "0", description = "Lead towards abusive traps containing scams."),
          SelectOption(label = "Abusive Contents", value = "1", description = "Posting messages that includes threats, NSFW, or bad words."),
          SelectOption(label = "Spam Contents", value = "2", description = "Posting messages that includes ABUSIVE ADVERTISEMENTS."),
          SelectOption(label = "Unfair Advantages", value = "3", description = "Usage of any tools to gain advantage than others."),
          SelectOption(label = "Other", value = "4", description = "We will take a look at their profile and decide."),
        ]
    )
  ])

  try:
    c = await bot.wait_for("select_option", check = lambda i: True, timeout = 30)
  except asyncio.TimeoutError:
    await m1.edit(components = [Select(disabled = True, placeholder = "Pick a reason...", options = [SelectOption(label = "None", value = "0")])])

  select = c.values[0]
  hashmap = {
    "0": "Scamming",
    "1": "Abusive Contents",
    "2": "Spam Contents",
    "3": "Unfair Advantages",
    "4": "Other Reasons",
  }

  id = genID()

  d = json.load(open("reports.json"))
  d[id] = {"target": user.id, "from": ctx.author.id, "class": int(c.values[0]), "timestamp": int(round(time.mktime(datetime.datetime.utcnow().timetuple()), 0))}
  json.dump(d, open("reports.json", "w"))

  await c.send(f"You have sucessfully sent a report of **{user.name}#{user.discriminator}** on **{hashmap[select]}**!\n**Asscociated Report ID:** `{id}`\n\n> We will be looking at the report as soon as possible. Message of the report response will be delivered to your **NerdBot Inbox**. Use `bruh notifications` to check it out!\n\n**We thank you sincerely on your support for the NerdBot Community!**", ephemeral = False)








@bot.command(aliases=["plot", "plots", "land", "lands"])
@commands.cooldown(1, 10, commands.BucketType.user) 
async def _plot(ctx):

  L = LANG(ctx.author.id)

  if await checkReboot(ctx): return

  if await isBanned(ctx, ctx.author.id): return

  await checkAccountExsists(ctx.author.id)

  profile = json.load(open("game.json"))

  if len(profile[str(ctx.author.id)]["plots"]) == 0:
    embed=discord.Embed(title=f"{ctx.author.name}'s Plot Menu", description=L.LANG("commands.plot.insufficient"), color=0xfef000, timestamp = datetime.datetime.utcnow())
    embed.set_footer(text=L.LANG(random.choice([
      "commands.plot.footer.0",
      "commands.plot.footer.1",
      "commands.plot.footer.2",
      "commands.plot.footer.3"
    ])) + " | " + await getTime())
    await ctx.send(embed=embed)
    return

  plots = profile[str(ctx.author.id)]["plots"]
  current = list(plots)[0]

  options = []
  for i in plots:
    if i == current:
      options.append(SelectOption(label = plots[i]["displayName"], emoji = emoji.emojize(plots[i]["texticon"], use_aliases = True), value = i, default = True, description = i))
    else:
      options.append(SelectOption(label = plots[i]["displayName"], emoji = emoji.emojize(plots[i]["texticon"], use_aliases = True), value = i, default = False, description = i))
      
  plotselect = Select(placeholder = "Select a plot", options = options, custom_id = "select")

  embed=discord.Embed(title=f"{ctx.author.name}'s Plot Menu", description=L.LANG("commands.plot.current") % (plots[current]["texticon"], plots[current]["displayName"], current), color=0xfef000, timestamp = datetime.datetime.utcnow())
  embed.set_footer(text=L.LANG(random.choice([
      "commands.plot.footer.0",
      "commands.plot.footer.1",
      "commands.plot.footer.2",
      "commands.plot.footer.3"
    ])) + " | " + await getTime())

  await ctx.send(embed =embed, components = [plotselect, [Button(style = ButtonStyle.blue, label = "Upgrade", disabled = True, custom_id = "upgrade"), Button(style = ButtonStyle.red, label = "Remove", custom_id = "remove")]])

  while True:
    done, pending = await asyncio.wait([
                    bot.wait_for('button_click'),
                    bot.wait_for('select_option')
                ], return_when=asyncio.FIRST_COMPLETED)
    target = list(done)[0].result()
    
    if target.custom_id == "select":
      current = target.values[0]

    options = []
    for i in plots:
      if i == current:
        options.append(SelectOption(label = plots[i]["displayName"], emoji = emoji.emojize(plots[i]["texticon"], use_aliases = True), value = i, default = True, description = i))
      else:
        options.append(SelectOption(label = plots[i]["displayName"], emoji = emoji.emojize(plots[i]["texticon"], use_aliases = True), value = i, default = False, description = i))
        
    plotselect = Select(placeholder = "Select a plot", options = options, custom_id = "select")
  
    embed=discord.Embed(title=f"{ctx.author.name}'s Plot Menu", description=L.LANG("commands.plot.current") % (plots[current]["texticon"], plots[current]["displayName"], current), color=0xfef000, timestamp = datetime.datetime.utcnow())
    embed.add_field(name = "Specifiers", value = f"**{L.LANG('general.list.specifiers.name')}:** {plots[current]['displayName']}\n**{L.LANG('general.list.specifiers.id')}:** `{current}`\n**{L.LANG('general.list.specifiers.icon')}:** {plots[current]['texticon']}")
    embed.set_footer(text=L.LANG(random.choice([
        "commands.plot.footer.0",
        "commands.plot.footer.1",
        "commands.plot.footer.2",
        "commands.plot.footer.3"
      ])) + " | " + await getTime())
  
    await target.edit_origin(embed =embed, components = [plotselect, [Button(style = ButtonStyle.blue, label = "Upgrade", disabled = True, custom_id = "upgrade"), Button(style = ButtonStyle.red, label = "Remove", custom_id = "remove")]])
  
  return
    







@bot.command(aliases=["use", "consume"])
@commands.cooldown(1, 5, commands.BucketType.user) 
async def _consume(ctx, citem=None, amount = None):

  if await checkReboot(ctx): return

  if await isBanned(ctx, ctx.author.id): return

  global items

  if citem == None:
    await ctx.send(random.choice([
      "What do you want to use??",
      "WHAT THE HEKC DO YOU WANT TO USE??",
      "Use what? Tell me.",
      "What thing you wanna use?",
      "I DONT KNOW WHATCHUA THINKING TELL ME WHAT YOU WANT TO USE."
    ]))
    return
  if amount == None:
    amount = 1
  else:
    try:
      amount = int(amount)
    except ValueError:
      await ctx.send(random.choice([
        "Whatta heck is a **%s**? That is not how you use to describe AMOUNT." % amount,
        "Gimme the proper amount.",
        "WHAT PART OF AMOUNT YOU DON'T UNDERSTAND????????",
        "Tell me the proper amount!"
      ]))
      return
  lower = citem
  item = citem.upper()
  if not item in items:
    await ctx.send(random.choice([
      f"`NERD`: Whattafuk is a **{lower}**?",
      f"Okay I'm very dumb what is a **{lower}**?",
      f"Uhh... I don't really think a **{lower}** is in my item dictionary...",
      f"I had lived 9999 years and never seen a **{lower}** before, does it even exsist?",
      f"If **{lower}** exsists, You'll send me to jesus."
    ]))
    return
  if items[item]["multiuse"] == None:
    await ctx.send(random.choice([
      "Hmm, I dunno if you can use this thing.",
      f"I don't think **{lower}** is useable.",
      "This item isn't useable.",
      "Unusable item! I cannot help you! :cry:"
    ]))
    return
  pre = ""
  if not items[item]["multiuse"] and amount > 1:
    amount = 1
    pre += f"Because item **{lower}** is not multiusable, the amount is resetted to **1**\n\n"


  # COMPLETED ITEM CHECK
  profile = json.load(open("game.json"))
  pitems = [x for x in profile[str(ctx.author.id)]["inventory"] if x["name"] == item]
  if len(pitems) <= 0:
    await ctx.send(random.choice([
      f"Does **{lower}** exsist in your inventory?",
      f"I feel sad, because **{lower}** isn't in your inventory.",
      f"**{lower}** is not in your inventory!",
      f"What comes first than using a **{lower}**? Well definitely, to obtain it!",
      f"None of **{lower}** exsist in your inventory, not even an atom of it."
    ]))
    return

  gg = True
  deathC = False
  #####
  if item == "POOP":
    if genRarity(10):
      pre += "You tried to observe the :poop: poop under the sun, but it accidently fall into your mouth!\nEwwww how disgusting are you!"
    else:
      pre += "You look at the poop under the sun.\nThe poop vanished, leaving nothing."

  #####
  elif item == "HANGMAN":
    if genRarity(50):
      if hastagdata(ctx.author.id, "--has-hangman-card", True):
        pre += "You showed the **Hangman Card** to the hangman.\nHe looks happy! :smile:\nHowever, he said you already saw your hangman card before, and he thinks you are cheating.\nThe hangman is angry and removed your free-hangman-guess."
        untag(ctx.author.id, "--has-hangman-card")
      else:
        pre += "You showed the **Hangman Card** to the hangman.\nHe looks happy! :smile:\n\nYou will gain **1 Free Guess** at the next round of hangman!"
        tag(ctx.author.id, "--has-hangman-card", True)
    else:
      pre += "You showed the **Hangman Card** to the hangman.\n" + random.choice([
        "Somehow, the hangman is short-sighted.",
        "Unfortunately, the hangman don't even recognize his own item!",
        "He have no idea what the heck are you holding.",
        "`HANGMAN`: Hmm... What is that?"
      ]) + "\nThe hangman denied your hangman card, and it vanished into nowhere."

  #####
  elif item == "NUKE":
    await ctx.send("Nuke isn't usable for now!")
    return

  #####
  elif item == "CARROT":
    if genRarity(10):
      amount = round(random.random() * random.randint(50, 300), 1)
      pre += f"You ate a **carrot** and found {space(amount)} <:nerdies:932234563579682816>, good for you!"
      await giveCoins(ctx.author.id, amount)
    else:
      pre += "You at a carrot, " + random.choice([
        "and whats inside a carrot? A carrot.",
        "there is nothing inside the carrot.",
        "and it is a useless carrot.",
        "and it's gone."
      ])

  #####
  elif item == "PLOT":
    if amount > 1:
      s = "s"
    else:
      s = ""
    pre += f"You gave {amount} **plot contract{s}** to the Plot Master."
    if len(profile[str(ctx.author.id)]["plots"]) > 5:
      pre += "\n" + random.choice([
        "`PLOT MASTER`: Dude seriously you already got 5 plots you still want more? No way.",
        "`PLOT MASTER`: Don't find me again because you already have 5 plots.",
        "`PLOT MASTER`: DIDN'T YOU READ THE RULES?? EACH PERSON CAN ONLY OWN 5 PLOTS MAXIUM!",
        "`PLOT MASTER`: Stop bragging infront of me because you have 5 plots.",
        "`PLOT MASTER`: Okay, you have 5 plots, you can't have more.",
        "`PLOT MASTER`: Find me again if you have less than 5 plots."
      ])
      pre += "\nThe Plot Master rejected your plot contract."
      gg = False
    elif len(profile[str(ctx.author.id)]["plots"]) + amount > 5:
      pre += "\n" + random.choice([
        f"`PLOT MASTER`: Hmm lemme count... {len(profile[str(ctx.author.id)]['plots'])} plots plus {amount} more plots equal to... {len(profile[str(ctx.author.id)]['plots']) + amount} plots????? Dude that\'s too much get out of here.",
        f"`PLOT MASTER`: Dude you already got {len(profile[str(ctx.author.id)]['plots'])} plots. If you have more that's not gonna be good.",
        "`PLOT MASTER`: Bro you already have that much plots if you want more it's gonna rise above 5 plots. I'm not a fool."
      ])
      pre += "\nThe Plot Master rejected your plot contract."
      gg = False
    else:
      pre += "\n" + random.choice([
        f"`PLOT MASTER`: Hmm... Okay, I'll give you {amount} more plots!",
        f"`PLOT MASTER`: I give you {amount} more plots! Take them!",
        f"`PLOT MASTER`: Wow a plot contract? I'll give you {amount} plots!"
      ])
      pre += "\nThe Plot Master took away your plot contract."
      profile = json.load(open("game.json"))
      for i in range(amount):
        profile[str(ctx.author.id)]["plots"][genSSID()] = {"texticon": ":poop:", "buildType": "NONE", "displayName": "Brand New Plot", "data": {}}
      json.dump(profile, open("game.json", "w"))
      

  profile = json.load(open("game.json"))
  for i in profile[str(ctx.author.id)]["inventory"]:
    if i["name"] == item:
      left = i["amount"] - amount
      if i["amount"] - amount == 0:
        profile[str(ctx.author.id)]["inventory"].remove(i)
      elif i["amount"] - amount < 0:
        await ctx.send(random.choice([
          "Bruh you don't have enough items to use it!",
          "Hey you don't have enough items!"
        ]) + f"\nYou choose to use **{space(amount)}** {items[item]['image']} **{items[item]['displayName']}**, but you only have **{space(i['amount'])}**")
        return
      else:
        profile[str(ctx.author.id)]["inventory"][profile[str(ctx.author.id)]["inventory"].index(i)]["amount"] -= 1
  json.dump(profile, open("game.json", "w"))
  if gg:
    await ctx.send(pre + "\n\n" + items[item]["image"] + " **" + items[item]["displayName"] + "** `" + item + f"` **-{amount}** ({left} left)")
  else:
    await ctx.send(items[item]["image"] + " **" + items[item]["displayName"] + "** `" + item + f"` **-{amount}** ({left} left)")
  if deathC:
    await death(ctx, ctx.author.id, 10)











@bot.command(name="bounty")
@commands.cooldown(5, 86400, commands.BucketType.user)
async def _bounty(ctx):

  if await checkReboot(ctx): return

  if await isBanned(ctx, ctx.author.id): return

  if isinstance(ctx.channel, discord.channel.DMChannel):
    return

  if ctx.message.guild.id != 897095973933838416:
    return

  RANDOM = discord.Color.from_rgb(random.randint(20,255),random.randint(20,255),random.randint(20,255))

  who_ask = False
  what_ask = False

  def check(message):
      return message.channel == ctx.channel and message.author.id == ctx.author.id

  who_ask = True
  embed=discord.Embed(color = RANDOM, timestamp = datetime.datetime.utcnow(), title="Setting up a bounty", description="Who do you want the bounty to be on? Tell me in the next 20 seconds!")
  ask_who_message = await ctx.send(embed=embed)
  try:
    who = await bot.wait_for("message", check = check, timeout=20)
  except asyncio.exceptions.TimeoutError:
    msg = await ctx.send("Well, I guess this is not going to set up.")
    return

  RANDOM = discord.Color.from_rgb(random.randint(20,255),random.randint(20,255),random.randint(20,255))

  embed=discord.Embed(color = RANDOM, timestamp = datetime.datetime.utcnow(), title="Setting up a bounty", description="What do you want the bounty reward to be? Tell me in the next 20 seconds!")
  await ctx.send(embed=embed)
  try:
    what = await bot.wait_for("message", check = check, timeout=20)
  except asyncio.exceptions.TimeoutError:
    await ctx.send("Well, I guess this is not going to set up.")
    return

  BOUNTY_ID = genSSID()

  RANDOM = discord.Color.from_rgb(random.randint(20,255),random.randint(20,255),random.randint(20,255))
  embed=discord.Embed(color = RANDOM, timestamp = datetime.datetime.utcnow(), title="Bounty Set!", description="Bounty will be posted at #bounty channel in Hypixel Gamers!\nThe bounty is: %s\n\nBounty ID: `%s`" % (what.content, BOUNTY_ID))
  await ctx.send(embed=embed)

  EXPIRES = datetime.datetime.utcnow() + datetime.timedelta(days = 7)

  f = json.load(open("smp-bounty.json"))

  channel = bot.get_channel(927902576295415871)
  embed=discord.Embed(timestamp = EXPIRES, color = 0xfbff00, title="New bounty!", description = f"A new bounty is made!\n\n**Bounty Hoster**: {ctx.author.name}\n**Bounty Target**: {bot.get_user(int(who.content.replace('<', '').replace('>', '').replace('!', '').replace('@', ''))).name}\n**Bounty Reward**: {what.content}\n**Bounty Expiration**: `{EXPIRES.strftime('%Y/%m/%d %H:%M:%S')} UTC`\n\n**This bounty is still valid!** Click the button below to send a message to the bounty hoster!")
  embed.set_footer(text = "This bounty expires at your time zome 👉")
  msg = await channel.send(embed=embed, components = [Button(style=ButtonStyle.blue, label="I'm done!", custom_id=f"_submitBounty.{BOUNTY_ID}", disabled = True)])
  f[BOUNTY_ID] = {"time": int(round(time.mktime(datetime.datetime.utcnow().timetuple()), 0)), "expires": int(round(time.mktime(EXPIRES.timetuple()), 0)), "hoster": ctx.author.id, "reward": what.content, "victim": int(who.content.replace("<", "").replace(">", "").replace("!", "").replace("@", "")), "bountyMsg": msg.id}
  json.dump(f, open("smp-bounty.json", "w"))

  








@bot.command(aliases=["vocab", "vocabulary", "urbandictionary", "word"])
@commands.cooldown(1, 2, commands.BucketType.user)
async def _word(ctx):

  if await checkReboot(ctx): return

  RANDOM = discord.Color.from_rgb(random.randint(20,255),random.randint(20,255),random.randint(20,255))

  with urllib.request.urlopen("https://api.urbandictionary.com/v0/random") as response:
    response_text = response.read()
    data = json.loads(response_text.decode())

  worddict = random.choice(data["list"])
  defin = worddict["definition"].replace("[", "").replace("]", "")
  ex = worddict["example"].replace("[", "").replace("]", "")
  if len(defin) >= 1021:
    defin = defin[0:1021] + "..."
  if len(ex) >= 1021:
    ex = ex[0:1021] + "..."
  embed=discord.Embed(description = "[Urban Dictionary](https://www.urbandictionary.com/) | Word By: %s" % worddict["author"], color = RANDOM, timestamp = datetime.datetime.utcnow(), title=worddict["word"], url = worddict["permalink"])
  embed.add_field(name="Definition:", value=defin, inline=False)
  embed.add_field(name="Example:", value=ex, inline=False)
  embed.set_footer(text = "👍 %s | 👎 %s" % (worddict["thumbs_up"], worddict["thumbs_down"]))
  await ctx.send(embed=embed)







make5_ver = "pre-1020220102"
make5_type = "build"
make5_name = "m5"

@bot.command(aliases=["make5", "hitechmake5"])
@commands.cooldown(1, 1, commands.BucketType.user)
async def _make5(ctx, *args):

  if await checkReboot(ctx): return

  if await isBanned(ctx, ctx.author.id): return
    
  global make5players
  if len(args) == 0:
    await ctx.send("Dude who do you want to play against with? Mention someone!")
    return

  make5players = []
  sets = []
  for i in args:
    try:
      if i[0] == "-" and i[1] == "-":
        sets.append(i)
      else:
        make5players.append(int(i.replace("<", "").replace(">", "").replace("!","").replace("@","")))
    except ValueError:
      await ctx.send("Sorry, who is %s" % i)
      return

  for i in make5players:
    usr = bot.get_user(i)
    if usr == None:
      await ctx.send("Hey! Did you type something wrong?")
      return
    if usr.bot:
      await ctx.send("Bruh you can't play with bots dude!")
      return
    if i == ctx.author.id:
      await ctx.send("You are already in the game, do not mention yourself!")
      return

  make5players.append(ctx.author.id)

  RANDOM = discord.Color.from_rgb(random.randint(20,255),random.randint(20,255),random.randint(20,255))

  embed=discord.Embed(color = RANDOM, timestamp = datetime.datetime.utcnow(), title="Super Make-5 Game!", description='This is a game that was build on the classic "five in a row" game.\nIn this game, I am going to make a channel, a new channel for the round in the make-5 category.\nAre you sure you want to start a game? This game will not end until no one have done a reaction in 3 minutes!')
  embed.set_footer(text="Cool game? | " + await getTime())
  
  if "--no-confirm" in sets:
    pass
  else:
    msg = await ctx.send(embed=embed, components = [[Button(style=ButtonStyle.green, label="Yes", custom_id="yes"), Button(style=ButtonStyle.red, label="No", custom_id="no")]])

    async def check(i):
      if not i.user.id == ctx.author.id:
        await i.send("You are not the host, so you cannot make the choice!")
        return False
      else:
        return True

    def check(i):
      return i.user.id == ctx.author.id

    try:
      reaction = await bot.wait_for("button_click", check = check, timeout = 10)
    except asyncio.exceptions.TimeoutError:
      await ctx.send("Well, I will assume thats a no.")
      return
    
    if reaction.custom_id == "no":
      await reaction.send(random.choice([
        "Well, let's say nothing happened.",
        "Whatever.",
        "k, ur choice.",
        "Well, fine."
      ]))
      await msg.edit(components = [[Button(style=ButtonStyle.green, label="Yes", custom_id="yes", disabled = True), Button(style=ButtonStyle.red, label="No", custom_id="no", disabled = True)]])
      return

    if reaction.custom_id == "yes":
      await msg.edit(components = [[Button(style=ButtonStyle.green, label="Yes", custom_id="yes", disabled = True), Button(style=ButtonStyle.red, label="No", custom_id="no", disabled = True)]])

  ide = random.choice(list("0123456789ABCDEF")) + random.choice(list("0123456789ABCDEF"))  + random.choice(list("0123456789ABCDEF")) + random.choice(list("0123456789ABCDEF")) + random.choice(list("0123456789ABCDEF")) + random.choice(list("0123456789ABCDEF"))
  name = 'make5-' + ide
  channel  = await ctx.message.guild.create_text_channel(name)

  global DISABLED
  DISABLED.append(channel.id)
  mentions = ""
  for i in make5players:
    mentions += "<@%s> " % i
  await ctx.send("%sPlease check <#%s>" % (mentions, channel.id))




  # GAME SETUP
  CLID = genID()

  pre = "`Make-5 By EricPooMan (Players: %s, SessionID: %s, GameID: %s)`" % (len(make5players), CLID, ide)
  await channel.send(pre)
  usr = []
  for i in make5players:
    usr.append({"id": i, "readyState": False})

  global make5_ver, make5_name, make5_type
  topic = "(%s) %s %s <%s>" % (make5_name, make5_type, make5_ver, CLID)
  await channel.edit(topic=topic)
  
  loopready = True

  plrstr = ""
  for i in usr:
    us = bot.get_user(i["id"])
    if i["readyState"] == False:
      plrstr += ":x: **%s**\n" % us.name
    if i["readyState"] == True:
      plrstr += ":white_check_mark: **%s**\n" % us.name

  embed=discord.Embed(color = RANDOM, timestamp = datetime.datetime.utcnow(), title="Step 1 - Check confirm", description="Now, we are going to check that if all the players are ready.\nMake sure to click the ready button in the next 30 seconds to prepare!")
  embed.add_field(name="Players:", value=plrstr, inline=False)
  embed.set_footer(text="Cool game? | " + await getTime())

  msg = await channel.send(embed=embed)

  
  while loopready:
    plrstr = ""
    readys = 0
    for i in usr:
      us = bot.get_user(i["id"])
      if i["readyState"] == False:
        plrstr += ":x: **%s**\n" % us.name
      if i["readyState"] == True:
        plrstr += ":white_check_mark: **%s**\n" % us.name
        readys += 1
      if readys == len(usr):
        loopready = False

    embed=discord.Embed(color = RANDOM, timestamp = datetime.datetime.utcnow(), title="Step 1 - Check confirm", description="Now, we are going to check that if all the players are ready.\nMake sure to click the ready button in the next 30 seconds to prepare!")
    embed.add_field(name="Players:", value=plrstr, inline=False)
    embed.set_footer(text="Cool game? | " + await getTime())

    await msg.edit(embed=embed, components = [Button(style=ButtonStyle.blue, label="I'm ready!", custom_id="ready", disabled = False)])

    def check(i):
      return i.custom_id == "ready" and i.author.id in make5players

    if loopready:
      try:
        res = await bot.wait_for("button_click", check = check, timeout = 30)
      except asyncio.exceptions.TimeoutError:
        await channel.delete()
        await ctx.send("Because not all the members are prepared in time, the game was disbanded.")
        return

    

    if res.custom_id == "ready":
      for i in usr:
        if res.user.id == i["id"]:
          usr[usr.index(i)]["readyState"] = True

  # STEP 2:  MODIFY CONFIG
  game = {"clid": CLID, "CHID" : ide, "players": make5players, "deckType": 0, "openCards": True, "inPrivateChat": False, "totalCards": 256}
  setstr = ""
  for i in game:
    if i == "players":
      setstr += "players: `%s` :no_entry_sign:\n" % len(game[i])
    if i == "deckType":
      const = {"0": "Noob", "1": "Beginner", "2": "Advanced", "3": "Master", "4": "Championship"}
      setstr += "deckType: `%s`\n" % const[str(game[i])]
    if i == "openCards":
      setstr += "openCards: `%s`\n" % str(game[i]).lower()
    if i == "inPrivateChat":
      setstr += "inPrivateChat: `%s` :no_entry_sign:\n" % str(game[i]).lower()
    if i == "totalCards":
      setstr += "totalCards: `%s`\n" % game[i]
  embed=discord.Embed(color = RANDOM, timestamp = datetime.datetime.utcnow(), title="Step 2 - Config variables", description="If you have anything to change with the variables, tell me in the next 30 seconds!\n**NOTE:** Only game master (game hoster) can modify the settings!\n*(Settings with :no_entry_sign: icon cannot be modified)*\n\n- Type `modify <variable>` to modify.\n- Type `confirm` to confirm.\n")
  embed.add_field(name="Variables:", value=setstr, inline=False)
  embed.set_footer(text="Cool game? | " + await getTime())
  await msg.edit(embed = embed)

  confirm = False

  try:
    choice = bot.wait_for("message", check=check, timeout=30)
  except asyncio.exceptions.TimeoutError:
    await channel.send("Well I will assume that is a confirm.")
    confirm = True

  if confirm != True:
    if choice == "confirm":
      confirm = True
    elif choice == "modify":
      pass


@bot.command()
@commands.cooldown(1, 300, commands.BucketType.user)
async def iwantnerdies(ctx):

  if await checkReboot(ctx): return

  if genRarity(50):
    await checkAccountExsists(ctx.author.id)
    await ctx.send("Fine, I'll give you 100,000 <:nerdies:932234563579682816>, don't beg me again!")
    profile = json.load(open("game.json"))
    profile[str(ctx.author.id)]["nerdies"]["wallet"] += 100000
    profile[str(ctx.author.id)]["nerdies"]["wallet"] = round(profile[str(ctx.author.id)]["nerdies"]["wallet"], 1)
    json.dump(profile, open("game.json", "w"))
  else:
    await ctx.send(random.choice([
      "Let's just do work and gain more Nerdies!",
      "Let's try and do work instead of begging me!",
      "Stop begging me! I don't have Nerdies!"
    ]))


    

@bot.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def simon(ctx):

  if await checkReboot(ctx): return

  
  await ctx.send("Say something to me in the next 10 seconds!")

  def check(message):
    return message.channel == ctx.channel and message.author.id == ctx.author.id

  try:
    msg = await bot.wait_for("message", check = check, timeout = 10)
  except asyncio.exceptions.TimeoutError:
    await ctx.send("Hmm, I guess I can't send a poop message anymore.")
    return
  await ctx.send(msg.content + " :poop:\n" + "My reaction delay is **" + str(round(bot.latency * 1000)) + "ms**!")





@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def poop(ctx):

  if await checkReboot(ctx): return

  
  await ctx.send("Say something to me in the next 10 seconds!")

  def check(message):
    return message.channel == ctx.channel and message.author.id == ctx.author.id

  try:
    msg = await bot.wait_for("message", check = check, timeout = 10)
  except asyncio.exceptions.TimeoutError:
    await ctx.send("Hmm, I guess I can't send a poop message anymore.")
    return
  await ctx.send(msg.content + " :poop:\n" + "My reaction delay is **" + str(round(bot.latency * 1000)) + "ms**!")




@bot.command(aliases = ["message", "send"])
@commands.cooldown(1, 20, commands.BucketType.user)
async def _message(ctx, target = None):

  if await checkReboot(ctx): return

  if await isBanned(ctx, ctx.author.id): return

  profile = json.load(open("game.json"))[str(ctx.author.id)]
  found = False
  for i in profile["inventory"]:
    if i["name"] == "PHONE":
      found = True

  if not found:
    await ctx.send(random.choice([
      "You need a NerdPhone in order to message people!",
      "Go buy a NerdPhone before sending messages!",
      "How can you send messages without NerdPhone?"
    ]) + " Go in **NerdMart** to buy one! `(bruh market buy phone)`")
    return
    
  if target == None:
    await ctx.send("Bruh you gotta mention someone! You can't send messages to air!\n*Remember to use `bruh message <mention a user>`, then continue!")
    return
  a = target.replace("<", "")
  b = a.replace(">", "")
  c = b.replace("!", "")
  d = c.replace("@", "")
  usrid = int(d)
  usr = bot.get_user(usrid)
  if usr == None:
    await ctx.send(random.choice([
      "I'm not sure if the mentioned guy is in my memory...",
      "Who is that guy? I never see them.",
      "I never see that guy before.",
      "Who is that guy? Don't know."
    ]))
    return
  if usr.bot:
    await ctx.send(random.choice([
      "Why would u sent to bots?",
      "Why bots?",
      "Dude not bots please",
      "BOTS CAN'T READ! (I'm sure they can)",
      "NO BOTS, a human!",
      "NO BOTSSSSSSS"
    ]))
    return

  def check(message):
    return message.channel == ctx.channel and message.author.id == ctx.author.id
  
  try:

    await ctx.send("What do you want the title to be? Tell me in the next 60 seconds!")

    title = await bot.wait_for("message", check = check, timeout = 60)

    await ctx.send("What do you want the content to be? Tell me in the next 60 seconds!")

    msg = await bot.wait_for("message", check = check, timeout = 60)
  
  
  except asyncio.exceptions.TimeoutError:
    await ctx.send("What??? Why won't you tell me something in time!")
    return

  await ctx.send("*Beep* You send the message!")
  await newNotif(usr.id, ctx.author.id, title.content, msg.content, "MESSAGE", True)






@bot.command(name = "notifications", aliases = ["notifs"])
@commands.cooldown(1, 10, commands.BucketType.user)
async def notifications(ctx, arg1 = None, arg2 = None, arg3 = None):

  if await checkReboot(ctx): return

  if await isBanned(ctx, ctx.author.id): return
  
  RANDOM = discord.Color.from_rgb(random.randint(20,255),random.randint(20,255),random.randint(20,255))

  page = 0

  messages = json.load(open("notifications.json"))

  try:
    messages[str(ctx.author.id)]
  except:
    await ctx.send("You don't have any messages! Find your friends and tell them to send you some messages!")
    return
  
  if arg1 == None:
    page = 0
  if arg1 == "page":
    try:
      page = int(arg2) - 1
    except:
      page = 0
    if page < 0:
      page = 0
  elif arg1 == "view":
    if arg2 == None:
      await ctx.send("You need to provide a message ID!")
      return

    found = False
    for i in messages[str(ctx.author.id)]:
      if i["id"] == arg2.upper():
        found = True
        target = i

    if not found:
      await ctx.send(random.choice([
        "Did you enter the message ID correctly?",
        "That ID dosen't exsist, *I guess*.",
        "Bruh I can't even find that message ID."
      ]))
      return

    dict1 = {"MESSAGE": "User Notification", "SYSTEM": "System Notification <a:sendBySystem:942783261174820884>"}

    add = ""

    if target['name'] == "SYSTEM":
      add = "<a:sendBySystem:942783261174820884>"
      author = target['sendBy']
    else:
      if len(str(i['sendBy'])) == 18:
        usr = bot.get_user(target['sendBy'])
        author = usr.name + "#" + str(usr.discriminator)
      else:
        author = phonestr(str(i['sendBy']))
    
    embed=discord.Embed(color = 0xfef000, timestamp = datetime.datetime.utcnow(), title="Message Viewer", description=f"**Sent Time**: {datetime.datetime.utcfromtimestamp(target['time']).strftime('%Y/%m/%d %H:%M:%S')} **(UTC)** | <t:{target['time']}>\n**Message Type**: {dict1[target['name']]}\n**Message Author**: {author}")
    embed.add_field(name=f"`{target['id']}` {target['title']} {add}", value=target["details"], inline=False)
    embed.set_footer(text = await randomFooterNerdTime())
    if target['name'] == "SYSTEM" or target['name'] == "PHONE_MESSAGE":
      cp = [[Button(style = ButtonStyle.blue, label = "Reply", disabled = True), Button(style = ButtonStyle.red, label = "Report", disabled = True), Button(style = ButtonStyle.red, label = "Delete", custom_id = "delete")]]
    elif target['name'] == "PHONE_MESSAGE":
      cp = [[Button(style = ButtonStyle.blue, label = "Reply", disabled = True), Button(style = ButtonStyle.red, label = "Report", custom_id = "report"), Button(style = ButtonStyle.red, label = "Delete", custom_id = "delete")]]
    else:
      cp = [[Button(style = ButtonStyle.blue, label = "Reply", disabled = True), Button(style = ButtonStyle.red, label = "Report", custom_id = "report"), Button(style = ButtonStyle.red, label = "Delete", custom_id = "delete")]]
      
    prev = await ctx.send(embed=embed, components = cp)

    try:
      r = await bot.wait_for("button_click", check = lambda i: i.message.id == prev.id, timeout = 30)
      if r.custom_id == "delete":
        messages[str(ctx.author.id)].remove(target)
        await r.send("Deleted this message! Poor message.", ephemeral = False)
        json.dump(messages, open("notifications.json"))
        raise asyncio.TimeoutError
      elif r.custom_id == "report":
        await r.send("This function is a stub! Check back later.", ephemeral = False)
        raise asyncio.TimeoutError
    except asyncio.TimeoutError:
      await prev.edit(components = [[Button(style = ButtonStyle.blue, label = "Reply", disabled = True), Button(style = ButtonStyle.red, label = "Report", custom_id = "report", disabled = True), Button(style = ButtonStyle.red, label = "Delete", custom_id = "delete", disabled = True)]])
    return

  elif arg1 == "delete":
    if arg2 == None:
      await ctx.send("You need to provide a message ID!")
      return
    found = False
    for i in messages[str(ctx.author.id)]:
      if i["id"] == arg2.upper():
        found = True
        target = i

    if not found:
      await ctx.send(random.choice([
        "Did you enter the message ID correctly?",
        "That ID dosen't exsist, *I guess*.",
        "Bruh I can't even find that message ID."
      ]))
      return
    messages[str(ctx.author.id)].remove(target)
    json.dump(messages, open("notifications.json", "w"))
    await ctx.send(random.choice([
      "Okay, I deleted the message. Poor message...",
      "Message message say goodbye! It's deleted!",
      "Goodbye message, see you next time! Deleted!"
    ]))
    return

  elif arg1 == "deleteall":
    messages.pop(str(ctx.author.id))
    json.dump(messages, open("notifications.json", "w"))
    await ctx.send(random.choice([
      "ALL OF YOUR MESSAGES ARE GONE!!! Deleted.",
      "Okay, I cleared your notifications.",
      "\*You have 0 notifications left!\*"
    ]))
    return

  if len(messages[str(ctx.author.id)]) % 6 == 0:
    maxpg = len(messages[str(ctx.author.id)]) / 6
  else:
    maxpg = (len(messages[str(ctx.author.id)]) // 6) + 1

  if page + 1 > maxpg:
    page = maxpg - 1

  if id == None:
    pass
  else:
    embed=discord.Embed(color = RANDOM , title="iNerd™ Messages", description="Use `bruh notifications page <page-number>` to view a specific page.\nUse `bruh notifications view <msg-ID>` to view details of a specific message.\n Use `bruh notifications delete <msg-id>` to delete a message.\nUse `bruh notifications deleteall` to clear all messages.", timestamp = datetime.datetime.utcnow())
    cnt = 0
    for i in messages[str(ctx.author.id)][page * 6:(page + 1) * 6]:
      cnt += 1
      if i["name"] == "SYSTEM":
        isSystem = "<a:sendBySystem:942783261174820884>"
      else:
        isSystem = ""
      if len(i["details"]) > 256:
        detailmsg = i["details"][0:256] + "..."
      else:
        detailmsg = i["details"]
      embed.add_field(name = "%s. `%s` %s %s" % (cnt, i["id"], i["title"], isSystem), value = detailmsg, inline=False)
      if cnt == 6:
        break

    
    embed.set_footer(text = f"Page {page + 1} out of {maxpg} | " + await getTime())
    await ctx.send(embed = embed)











@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def profile(ctx, target = None):

  if await checkReboot(ctx): return

  if await isBanned(ctx, ctx.author.id): return

  global UNTIL_NEXT

  card_footer = ["Why would you do that?",
      "Mr. Bob",
       "Why not a episode of sponge bob?",
       "Go away!",
       "Awesome!",
       "YUM!",
       "check our awesome site! bruh site"]

  await checkAccountExsists(ctx.author.id)

  if target != None:
    stuff = target.replace("<", "").replace(">", "").replace("@", "").replace("!", "")
    try:
      stuff = int(stuff)
    except ValueError:
      await ctx.send(random.choice([
        "Hey! You should mention a user not the stuff you entered!",
        "The user you specified is not valid.",
        "Please mention a valid user."
      ]))
      return

    try:
      profile = json.load(open("game.json"))[str(stuff)]
    except KeyError:
      await ctx.send("Looks like the user you mentioned either don't exsist or haven't use NerdBot yet, so we can't find a profile of that user.")
      return
    try:
      trophystr = ""
      name = ""
      des = ""
      if stuff in DEBUG_WHITELIST:
        des += "This is a **ADMIN** profile. They can change everything about their profile. [Learn more](https://www.saltyfishstudios.net/nerd/admin-profiles)\n"
      if ctx.guild.get_member(stuff) == None:
        name = "`Anonymous`"
        des += "This user's name is displayed as `Anonymous` because the user you specified is not in this server. [Learn more](https://www.saltyfishstudios.net/nerd/admin-profiles)\n"
      else:
        name = bot.get_user(stuff).name
      for i in profile["trophy"]:
        trophystr += items[i]["image"] + " "
      
      embed=discord.Embed(title = f"{name}'s profile {trophystr}", description = des, color = 0xfef000, timestamp = datetime.datetime.utcnow())
    except:
      embed=discord.Embed(title = f"`Unknown User`'s profile", color = 0xfef000, timestamp = datetime.datetime.utcnow(), description = "**WARNING!** This profile is marked as `Unknown User` because this user's discord ID is invalid, or this user could be a NerdBot Automaticly Generated User. [Learn More](https://www.saltyfishstudios.net/nerd/automatic-generated-users)")
    embed.add_field(name="Wallet", value="**Nerdies:** {:,}".format(profile["nerdies"]["wallet"]) + " <:nerdies:932234563579682816>", inline=True)
    if profile["level"] <= 15:
      embed.add_field(name="Experience", value="**LVL:** {:,}".format(profile["level"]) + "\n**EXP:** {:,}".format(profile["exp"]) + "/{:,}".format(UNTIL_NEXT[str(profile["level"])]) + " <a:exp:913753763959939092>", inline=True)
    else:
      embed.add_field(name="Experience", value="**LVL:** {:,}".format(profile["level"]) + "\n**EXP:** {:,}".format(profile["exp"]) + "/{:,}".format(UNTIL_NEXT["16+"]) + " <a:exp:913753763959939092>", inline=False)
    bankd = json.load(open("banks.json"))
    bank = profile["nerdies"]["bank"]
    banks = []
    for i in bank:
      targ = bankd[i["name"]]
      if targ["name"] == "DEFAULT":
        banks.append({"name":"DEFAULT", "displayName": targ["displayName"], "amount":i["amount"]})
      else:
        banks.append({"name":targ["name"], "displayName": targ["displayName"], "amount":i["amount"]})
    value = ""
    
    for i in banks:
      value += "**" + i["displayName"] + "** `" + i["name"] +  "`" +  ": " + "{:,}".format(i["amount"]) + " <:nerdies:932234563579682816>\n"
    embed.add_field(name="Banks", value=value, inline=False)
    pocketstr = ""
    pocketcount = 0
    change = False
    for i in profile["pocketItems"]:
      pocketcount += 1
      pocketstr += f"{items[i]['rarietyImage']} {items[i]['image']} **{items[i]['displayName']}**\n"
      change = True
    if not change:
      pocketstr = "`No pocket items :(`"
    embed.add_field(name=f"Pocket Items **({pocketcount}/5)**", value=pocketstr, inline=False)
    embed.set_footer(text=random.choice(card_footer) + " | " + await getTime())
    await ctx.send(embed = embed)
    return
  profile = json.load(open("game.json"))[str(ctx.author.id)]
  trophystr = ""
  for i in profile["trophy"]:
    trophystr += items[i]["image"] + " "
  embed=discord.Embed(title = f"{ctx.author.name}'s profile {trophystr}", color = 0xfef000, timestamp = datetime.datetime.utcnow())
  embed.add_field(name="Your Wallet", value="**Nerdies:** {:,}".format(profile["nerdies"]["wallet"]) + " <:nerdies:932234563579682816>", inline=True)
  if profile["level"] <= 15:
    embed.add_field(name="Your Experience", value="**LVL:** {:,}".format(profile["level"]) + "\n**EXP:** {:,}".format(profile["exp"]) + "/{:,}".format(UNTIL_NEXT[str(profile["level"])]) + " <a:exp:913753763959939092>", inline=True)
  else:
    embed.add_field(name="Your Experience", value="**LVL:** {:,}".format(profile["level"]) + "\n**EXP:** {:,}".format(profile["exp"]) + "/{:,}".format(UNTIL_NEXT["16+"]) + " <a:exp:913753763959939092>", inline=False)
  bankd = json.load(open("banks.json"))
  bank = profile["nerdies"]["bank"]
  banks = []
  for i in bank:
    targ = bankd[i["name"]]
    if targ["name"] == "DEFAULT":
      banks.append({"name":"DEFAULT", "displayName": targ["displayName"], "amount":i["amount"]})
    else:
      banks.append({"name":targ["name"], "displayName": targ["displayName"], "amount":i["amount"]})
  value = ""
  
  for i in banks:
    value += "**" + i["displayName"] + "** `" + i["name"] +  "`" +  ": " + "{:,}".format(i["amount"]) + " <:nerdies:932234563579682816>\n"
  embed.add_field(name="Your Banks", value=value, inline=False)
  pocketstr = ""
  pocketcount = 0
  change = False
  for i in profile["pocketItems"]:
    pocketcount += 1
    pocketstr += f"{items[i]['rarietyImage']} {items[i]['image']} **{items[i]['displayName']}**\n"
    change = True
  if not change:
    pocketstr = "`No pocket items :(`"
  embed.add_field(name=f"Your Pocket Items **({pocketcount}/5)**", value=pocketstr, inline=False)
  embed.set_footer(text=random.choice(card_footer) + " | " + await getTime())
  await ctx.send(embed = embed)





@bot.command(aliases = ["inv", "inventory", "bag"])
@commands.cooldown(1, 5, commands.BucketType.user)
async def checkInventory(ctx, page = None):

  if await checkReboot(ctx): return

  if await isBanned(ctx, ctx.author.id): return
    
  global items

  await checkAccountExsists(str(ctx.author.id))
  
  inv_footer = [
    "Toxic bag.",
    "Inventory power!",
    "Heavy, so heavy.",
    "Fill it up!"
  ]

  profile = json.load(open("game.json"))[str(ctx.author.id)]
  if page == None:
    page = 0
  else:
    try:
      page = int(page) - 1
    except ValueError:
      page = 0
  if len(profile["inventory"]) % 6 == 0:
    maxPage = len(profile["inventory"]) // 6
  else:
    maxPage = (len(profile["inventory"]) // 6) + 1
  if page + 1 > maxPage:
    page = maxPage - 1
  if page <= 0:
    page = 0
  embed=discord.Embed(timestamp = datetime.datetime.utcnow(), color = 0xfef000, title="Your inventory")
  embed.set_thumbnail(url="https://www.saltyfishstudios.net/assets/inventory.png")
  if len(profile["inventory"]) == 0:
    embed.add_field(name="Your stuff:", value="Sad, its empty!", inline=False)
    embed.set_footer(text=random.choice(inv_footer) + " | " + await getTime())
    await ctx.send(embed=embed)
    return
  count = 0
  targlist = profile["inventory"][page * 6: (page + 1) * 6]
  for i in targlist:
    count += 1
    if "replace_description" in i["data"]:
      description = i["data"]["replace_description"]
    elif "additional_description" in i["data"]:
      description = items[i["name"]]["description"] + i["data"]["additional_description"]
    else:
      description = items[i["name"]]["description"]
    embed.add_field(name="%s %s **%s** `%s` (%s)" % (items[i["name"]]["rarietyImage"], items[i["name"]]["image"], items[i["name"]]["displayName"], i["name"], i["amount"]), value="- %s" % description, inline=False)
    if count == 6:
      break
  embed.set_footer(text="Page %s out of %s | " % (page + 1, maxPage) + await getTime())
  await ctx.send(embed=embed)







@commands.cooldown(1, 15, commands.BucketType.user)
@bot.command(aliases = ['with', 'withdraw']) 
async def withdrawFromBank(ctx, amount = None, bank = "DEFAULT"):

  if await checkReboot(ctx): return

  if await isBanned(ctx, ctx.author.id): return

  global DEV
  if DEV:
    await ctx.reply("Sorry! The bot is in developement! Please perform actions to me when I am avaliable!")
    return
    
  if amount == None:
    quote = random.choice([
      "What are you withdrawing? (Use bruh with [amount] [bank account (default: DEFAULT)])",
      "ARE YOU WITHDRAWING BANANAS? TELL ME SOMETHING! (Use bruh with [amount] [bank account (default: DEFAULT)])",
      "YOU CAN'T WITHDRAW AIR YOU IDIOT. (Use bruh with [amount] [bank account (default: DEFAULT)])",
    ])
    if quote == "%send_image%":
      await ctx.send("Use bruh with [amount] [bank account (default: DEFAULT)]!!!!")
      await ctx.send("https://saltyfishstudios.net/memes/meme1.png")
      return
    else:
      await ctx.send(quote)
      return
  try:
    amount = int(amount)
  except ValueError:
    await ctx.send(random.choice([
      "Sorry bro, I never been to primary school, so I can't read text.",
      "CAN'T YOU COUNT? WHAT DO YOU MEAN BY TEXT????",
      "Bruh I can't read text",
      "qw3rjouojsbruh  kjhSJJHN MHJ I CAN'T READT EXT!!!!",
      "Uhhhhhhhhhhhhhhhh... NO TEXT PLEASE!",
      "I H.A.T.E. TEXT!",
      "Stop typing text, I want number!"
    ]))
    return
  if amount == 0:
    await ctx.send(random.choice([
      "Bro you can't withdraw 0 right?",
      "Dude what is 0??",
      "Hmm, I would prefer air than 0"
    ]))
    return
  if amount < 0:
    await ctx.send(random.choice([
      "WHAT? WHY A NEGATIVE?",
      "My math teacher never tought me about negatives.",
      "FIND THE ABSOLUTE VALUE OF IT! I DON'T LIKE NEGATIVE NUMBERS!",
      "Please, MAKE IT POSITIVE!",
      "Would you prefer absolute it? |%s|" % amount
    ]))
    return
  bank = bank.upper()
  target = json.load(open("game.json"))
  loop = target[str(ctx.message.author.id)]["nerdies"]["bank"]
  for i in loop:
    if i["name"] == bank:
      if target[str(ctx.message.author.id)]["nerdies"]["bank"][loop.index(i)]["amount"] - amount < 0:
        await ctx.send(random.choice([
          "Well I guess thats too much!",
          "Poor %s don't have enough nerdies to support for %s nerdies." % (i["displayName"], "{:,}".format(amount)),
          "Your bank don't have enough nerdies.",
          "well, I guess, u don't have enough nerdies dude!",
          "I CAN'T HELP YOU! ITS OUT OF NERDIES!"
        ]))
        return
      target[str(ctx.message.author.id)]["nerdies"]["bank"][loop.index(i)]["amount"] -= amount
      target[str(ctx.message.author.id)]["nerdies"]["wallet"] += amount
      break
  json.dump(target, open("game.json", "w"))


















  



bot.remove_command("help")
@bot.command(aliases = ["help"])
@commands.cooldown(1, 0, commands.BucketType.user)
async def helpOnCommand(ctx, data1 = None):

  if await checkReboot(ctx): return

  if await isBanned(ctx, ctx.author.id): return

  global DEV
  if DEV:
    await ctx.reply("Sorry! The bot is in developement! Please perform actions to me when I am avaliable!")
    return

  embed=discord.Embed(title="All commands", description="Use bruh help [page number] to swap pages!", color = 0xfef000, timestamp = datetime.datetime.utcnow())
  embed.set_thumbnail(url="https://www.saltyfishstudios.net/assets/commandBanner.png")
  total_page_number = len(Commands) - 1
  if data1 == None:
    page_number = 0
  else:
    try:
      page_number = int(data1) - 1
    except ValueError:
      help_command = data1
      target = None
      for i in Commands:
        for x in Commands[i]:
          if x["name"] == help_command:
            target = x
      if target == None:
        await ctx.send("What do you mean by %s I never seen that command before." % help_command)
        return
      embed=discord.Embed(color =0xfef000, title="Helping on command `bruh %s`" % help_command, description=target["specific"]["description"], timestamp = datetime.datetime.utcnow())
      embed.add_field(name="Usage", value=target["specific"]["usage"], inline=True)
      await ctx.send(embed=embed)
      return
  try:
    f = Commands[str(page_number)]
  except KeyError:
    f = Commands[str(total_page_number)]
    page_number = total_page_number
  for i in f:
    embed.add_field(name=i["displayName"] + " `" + i["usage"] + "`", value="- " + i["description"], inline=False)
  embed.set_footer(text="Page " + str(page_number + 1) + " out of " + str(total_page_number + 1) + " | " + await getTime())
  await ctx.send(embed=embed)





@bot.command(aliases = ["market", "shop", "nerdmart"])
@commands.cooldown(1, 5, commands.BucketType.user)
async def NerdMart(ctx, data=None, item = None, amount = None):

  if await checkReboot(ctx): return

  if await isBanned(ctx, ctx.author.id): return
    
  global SHOP_CREDITS

  await checkAccountExsists(ctx.author.id)

  if data != None and data.upper() == "BUY":
    await ctx.send("The buy command had moved to a individual command!\nUse `bruh buy <item> [amount]` to buy stuff now!")
    return

  if data != None and data in ["stock", "stocks"]:
    await ctx.send("The command `bruh market stocks...` is no longer avaliable.")
    return

  market = json.load(open("market.json"))
  backmarket = json.load(open("market.json"))
  for i in market:
    for x in market[i]:
      if x["amount"] == 0:
        market[i].remove(x)
        if len(market[i]) == 0:
          market[i] = [backmarket[i][0]]
        else:
          backmarket[i].remove(x)

    try:
      page_number = int(data) - 1
    except TypeError:
      page_number = 0
    except ValueError:
      page_number = 0

  embed=discord.Embed(title="Welcome to Nerdmart!", description="Use `bruh buy [item ID] [amount]` to buy something.\nIDs are in `Code Snippets`", color = 0xfef000, timestamp = datetime.datetime.utcnow())
  embed.set_thumbnail(url="https://www.saltyfishstudios.net/assets/nerdmart.png")
  total_page_number = len(shop) - 1
  try:
    f = shop[str(page_number)]
  except KeyError:
    f = shop[str(total_page_number)]
    page_number = total_page_number
  for i in f:
    prices = sorted(market[i], key = lambda a: a['cost'])
    supply = sum(x["amount"] for x in prices)
    cheapest = prices[0]
    if supply <= 0:
      ############# HERE
      embed.add_field(name=items[i]["rarietyImage"] + " " + items[i]["image"] + " " + items[i]["displayName"] + " `" + i + "` - " + "**:warning: Out of stock!" + "**", value="- " + items[i]["description"], inline=False)
    else:
      embed.add_field(name=items[i]["rarietyImage"] + " " + items[i]["image"] + " " + items[i]["displayName"] + " `" + i + "`" + " - " + space(cheapest["cost"]) + " <:nerdies:932234563579682816> (" + inttostr(supply) + ")", value="- " + items[i]["description"], inline=False)
  embed.set_footer(text="Page " + str(page_number + 1) + " out of " + str(total_page_number + 1) + " | " + await getTime())
  await ctx.send(embed=embed)




@bot.command(name = "buy")
@commands.cooldown(1, 10, commands.BucketType.user)
async def buy(ctx, item = None, amount = None):

  if await checkReboot(ctx): return

  await checkAccountExsists(ctx.author.id)
  
  if item == None:
    quote = [
        "Bruh are you going to buy air? Tell me the right thing!",
        "Hmm, air is not fun! Probably go buy some other stuff.",
        "WON'T YOU CHECK THE MENU LIST??????"
      ]
    await ctx.send(random.choice(quote))
    return
  else:
    try:
      try:
        itemd = items[item.upper()]
        found = False
        for i in shop:
          if item.upper() in shop[i]:
            found  = True
            break
        if not found:
          raise KeyError
            
      except KeyError:
        await ctx.send(random.choice([
          "What is an **%s**?",
          "Sorry, what is an **%s**?",
          "`Cashier`: There is no **%s**, don't waste my life by asking these questions."
        ]) % item)
        return
      market = json.load(open("market.json"))
      data = json.load(open("game.json"))
      prices = sorted(market[item.upper()], key = lambda a: a['cost'])
      cheapest = prices[0]
      supply = sum(x["amount"] for x in prices)
      if amount == None:
        amount = 1
      elif amount.isdigit():
        amount = int(amount)
      elif amount.upper() == "SUPPLYMAX":
        sup = 0
        for i in market[item.upper()]:
          sup += i["amount"]
        amount = sup
      elif amount.upper() == "MAX":
        profile = json.load(open("game.json"))
        usern = profile[str(ctx.author.id)]["nerdies"]["wallet"]
        amount = usern / round(cheapest["cost"], 1)
        amount = int(math.floor(amount))
        if amount > supply:
          amount = supply
      if supply <= 0:
        await ctx.send(random.choice([
          "We are out of supply! Sorry!",
          "Sorry it's sold out!",
          "We are out of stock!"
        ]) + " We will refill it tomorrow!")
        return
      if data[str(ctx.author.id)]["nerdies"]["wallet"] < round(cheapest["cost"] * amount, 1):
        quote = [
          "*Beep* Your card ran out of money!",
          "Bruh your card is quite empty!",
          "CHECK UR WALLET!",
          "Heh get more moeney.",
          "Cries! You don't have enough money!"
        ]
        await ctx.send(random.choice(quote) + f" You need {space(round(cheapest['cost'] * amount, 1))} <:nerdies:932234563579682816>")
        return
      elif amount > supply:
        await ctx.send(random.choice([
          "Yo boy are you going to be a huge customer? We don't have that much stuff boy.",
          "Can't you see the supply number? We don't have enough!",
          "We don't have enough! Sorry!"
        ]))
        return

      else:
        find = True
        samount = amount
        totalprice = 0
        pc = sorted(market[item.upper()], key = lambda a: a['cost'])
        credits = {}
        while find:
          samount -= 1
          if pc[0]["amount"] <= 0:
            pc.remove(pc[0])
          pc[0]["amount"] -= 1
          if not credits.get(str(pc[0]["author"]), False):
            credits[str(pc[0]["author"])] = pc[0]["cost"]
          else:
            credits[str(pc[0]["author"])] += pc[0]["cost"]
          totalprice += pc[0]["cost"]
          if samount == 0:
            break
          pc = sorted(pc, key = lambda a: a['cost'])

          
        market[item.upper()] = pc
        json.dump(market, open("market.json", "w"))

        additional = json.load(open("additional.json"))
        addtax = round(totalprice * additional["NERDMART_LOCAL_TAX"], 1)
        totalprice += addtax
        totalprice = round(totalprice, 1)
              

        found = False
        for i in data[str(ctx.author.id)]["inventory"]:
          if i["name"] == item.upper() and i["data"] == {}:
            data[str(ctx.author.id)]["inventory"][data[str(ctx.author.id)]["inventory"].index(i)]["amount"] += amount
            found = True
            break
        if not found:
          data[str(ctx.author.id)]["inventory"].append({"name": item.upper(), "amount": amount, "data": {}})

        
        if data[str(ctx.author.id)]["nerdies"]["wallet"] < round(totalprice, 1):
          quote = [
            "*Beep* Your card ran out of money!",
            "Bruh your card is quite empty!",
            "CHECK UR WALLET!",
            "Well, this shit is too much, you don't have enough money!",
            "Cries! You don't have enough money!"
          ]
          await ctx.send(random.choice(quote) + f" You need {space(round(totalprice, 1))} <:nerdies:932234563579682816>")
          return

      data[str(ctx.author.id)]["nerdies"]["wallet"] -= round(totalprice, 1)
      data[str(ctx.author.id)]["nerdies"]["wallet"] = round(data[str(ctx.author.id)]["nerdies"]["wallet"],1)

      for i in credits:
        data[i]["nerdies"]["wallet"] += round(credits[i], 1)
        if i in SHOP_CREDITS:
          SHOP_CREDITS[i] += round(credits[i], 1)
        else:
          SHOP_CREDITS[i] = round(credits[i], 1)

      json.dump(data, open("game.json", "w"))

      embed=discord.Embed(color = 0xfef000, title="Thanks for visiting Nerdmart!", description="You sucessfully purchased " + inttostr(amount) + " " + itemd["image"] + " " + itemd["displayName"] + " for " + inttostr(round(totalprice, 1) - addtax) + f" <:nerdies:932234563579682816>, with addition of {inttostr(addtax)} <:nerdies:932234563579682816> of tax, resulting on a total price of **{inttostr(round(totalprice, 1))} <:nerdies:932234563579682816>**\n\n**Daily NerdMart Tax:** `{round(additional['NERDMART_LOCAL_TAX'] * 100, 1)}%` (+{addtax} <:nerdies:932234563579682816>)", timestamp = datetime.datetime.utcnow())
      embed.set_footer(text="Thanks for your purchase! | " + await getTime())
      await ctx.send(embed=embed)
      return
    except ValueError:
      pass






@bot.command(aliases = ["selltomarket", "idontcareijustwannasellmystuffplsdudecmon"])
@commands.cooldown(1, 10, commands.BucketType.user)
async def sell(ctx, wtf = None, howmuch = None, cost = None):

  if await checkReboot(ctx): return

  if await isBanned(ctx, ctx.author.id): return

  global items

  market = json.load(open("market.json"))

  profile = json.load(open("game.json"))
  if wtf == None:
    await ctx.send("Bro what are you going to sell todayyy??")
    return
  elif wtf == "BRO_BRO_BRO_LISTEN_TO_ME":
    await ctx.send("Sorry your bro is not going to respond to you lol.")
    return

  if howmuch == None:
    howmuch = 1

  found = False
  for i in profile[str(ctx.author.id)]["inventory"]:
    if i["name"] == wtf.upper():
      found = True
      break
  if not found:
    await ctx.send(random.choice([
      "Bruh please check your inventory I don't think that exsists in your inventory.",
      "Does that item exsist in your inventory?",
      "DO YOU HAVE THE ITEM???",
      "Dude check your inventory please.",
      "If you don't have this item, please buy it before selling it."
    ]))
    return

  try:
    int(howmuch)
  except ValueError:
    if howmuch.upper() == "MAX":
      all = [i for i in profile[str(ctx.author.id)]["inventory"] if i["name"] == wtf.upper()]
      totalamount = sum([i["amount"] for i in all])
      howmuch = totalamount
    else:
      await ctx.send(random.choice([
        "You must made a typo on entering your amount! It must be a number or `max`!",
        "Hey! Did you specify your amount correctly? It must be a number or `max`!"
      ]))
      return


  market = json.load(open("market.json"))
  wtf = wtf.upper()
  try:
    pc = sorted(market[wtf], key = lambda a: a['cost'])
  except KeyError:
    await ctx.send(random.choice([
      "You can't sell that, it's dosen't exsist in NerdMart.",
      "Bruh that thing isn't sellable in NerdMart.",
      "Dude that thing dosen't exsist in NerdMart."
    ]))
    return

  print("U")

  for i in profile[str(ctx.author.id)]["inventory"]:
    if i["name"] == wtf.upper():
      if int(howmuch) > i["amount"]:
        await ctx.send(random.choice([
          "Dude do you have that much?",
          "Bruh I don't think you have that much.",
          "Look at how much you have.",
          "Oops, you do not have that much!"
        ]) + f" You have {space(i['amount'])} {items[wtf.upper()]['image']} **{items[wtf.upper()]['displayName']}** in your inventory.")
        return
      if int(howmuch) < 1:
        await ctx.send(random.choice([
          "You can't just sell *nothing*.",
          "You must sell at least 1 item, thats the rules.",
          "You can't sell 0 items.",
        ]))
        return
      break

  
    
  if cost == None:
    lowest = pc[0]["cost"]
    if pc[0]["amount"] == 0:
      msg = await ctx.send(f"Because you didn't specify how much you want to sell this item for **(Argument #3)**, pick one of the 3 choices below...\n**Lowest price**: *Nobody is selling this item! Pick you own price!*", components = [[Button(style = ButtonStyle.blue, label = "Pick my own price", emoji = bot.get_emoji(955030104419995698), custom_id = "choice0"), Button(style = ButtonStyle.blue, label = "Same as lowest price", emoji = bot.get_emoji(955028874213875802), disabled = True), Button(style = ButtonStyle.blue, label = "0.1 cheaper than lowest price", emoji = bot.get_emoji(955026117499183154), disabled = True)]])
    else:
      if round(lowest, 1) <= 0.1:
        msg = await ctx.send(f"Because you didn't specify how much you want to sell this item for **(Argument #3)**, pick one of the 3 choices below...\n**Lowest price**: {space(round(lowest, 1))} <:nerdies:932234563579682816>", components = [[Button(style = ButtonStyle.blue, label = "Pick my own price", emoji = bot.get_emoji(955030104419995698), custom_id = "choice0"), Button(style = ButtonStyle.blue, label = "Same as lowest price", emoji = bot.get_emoji(955028874213875802), custom_id = "choice1"), Button(style = ButtonStyle.blue, label = "0.1 cheaper than lowest price", emoji = bot.get_emoji(955026117499183154), disabled = True)]])
      else:
        msg = await ctx.send(f"Because you didn't specify how much you want to sell this item for **(Argument #3)**, pick one of the 3 choices below...\n**Lowest price**: {space(round(lowest, 1))} <:nerdies:932234563579682816>", components = [[Button(style = ButtonStyle.blue, label = "Pick my own price", emoji = bot.get_emoji(955030104419995698), custom_id = "choice0"), Button(style = ButtonStyle.blue, label = "Same as lowest price", emoji = bot.get_emoji(955028874213875802), custom_id = "choice1"), Button(style = ButtonStyle.blue, label = "0.1 cheaper than lowest price", emoji = bot.get_emoji(955026117499183154), custom_id = "choice2")]])
    while True:
      try:
        inter = await bot.wait_for("button_click", check = lambda i: i.message.id == msg.id, timeout = 30)
        if inter.user.id != ctx.author.id:
          await ctx.send(random.choice([
            "Go away! You are not the one selling this!",
            "Shoo! You are not the one selling this!",
            "Scram! You are not the one selling this!"
          ]))
          continue
        if inter.custom_id == "choice0":
          if pc[0]["amount"] == 0:
            await msg.edit(components = [[Button(style = ButtonStyle.blue, label = "Pick my own price", emoji = bot.get_emoji(955030104419995698), disabled = True), Button(style = ButtonStyle.blue, label = "Same as lowest price", emoji = bot.get_emoji(955028874213875802), disabled = True), Button(style = ButtonStyle.blue, label = "0.1 cheaper than lowest price", emoji = bot.get_emoji(955026117499183154), disabled = True)]])
            await inter.send("Tell me in the next 30 seconds the cost that you want to sell it for! **(Nobody is selling this item! Pick your own price!)**", ephemeral = False)
          else:
            await inter.send("Tell me in the next 30 seconds the cost that you want to sell it for! **(Lowest market price for item `%s`: %s <:nerdies:932234563579682816>)**" % (wtf, space(lowest)), ephemeral = False)
          try:
            cost = await bot.wait_for("message", check = lambda i: i.author.id == ctx.author.id, timeout = 30)
          except asyncio.exceptions.TimeoutError:
            await ctx.send(random.choice([
              "SELLING IS OVER!",
              "I guess you don't wanna sell it anymore.",
              "Well I guess you don't wanna sell stuff anymore?"
            ]))
            return
          cost = cost.content
          try:
            cost = float(cost)
          except ValueError:
            await ctx.send(random.choice([
              "What the? What is that?? I never go to school.",
              "Hey! Check your format!",
              "Bruuuuh tell me a number! Actully a float number.",
              "Hmm did you type that correctly?"
            ]))
            return
          if cost < 0.1:
            await ctx.send(random.choice([
              "Do you want to lose money?",
              "You are going to lose money if you are going to pick that price.",
              "That is not a good price.",
            ]) + " Your price must be at least `0.1` <:nerdies:932234563579682816>")
            return
          if cost > 1000000000000:
            await ctx.send(random.choice([
              "Your **price** is too high!",
              "Hey! You can't set the price that high!",
              "Lower down your price!",
              "Nobody is gonna buy that if your price is gonna be that high."
            ]) + " Your price can be at most 1,000,000,000,000 <:nerdies:932234563579682816>")
            return
          abc = str(float(cost))
          sept = abc.split(sep=".")
          if len(sept[1]) > 1:
            cost = round(float(cost), 1)
            await ctx.send("Because the cost you applied is %s decimal places and only need 3 decimal place, we will round it to 1 decimal places with value being %s <:nerdies:932234563579682816>" % (space(len(sept[1])), cost))
          break
        elif inter.custom_id == "choice1":
          cost = round(lowest, 1)
          await inter.respond(type = 6)
          await msg.edit(components = [[Button(style = ButtonStyle.blue, label = "Pick my own price", emoji = bot.get_emoji(955030104419995698), disabled = True), Button(style = ButtonStyle.blue, label = "Same as lowest price", emoji = bot.get_emoji(955028874213875802), disabled = True), Button(style = ButtonStyle.blue, label = "0.1 cheaper than lowest price", emoji = bot.get_emoji(955026117499183154), disabled = True)]])
          break
        elif inter.custom_id == "choice2":
          cost = round(lowest - 0.1, 1)
          await inter.respond(type = 6)
          await msg.edit(components = [[Button(style = ButtonStyle.blue, label = "Pick my own price", emoji = bot.get_emoji(955030104419995698), disabled = True), Button(style = ButtonStyle.blue, label = "Same as lowest price", emoji = bot.get_emoji(955028874213875802), disabled = True), Button(style = ButtonStyle.blue, label = "0.1 cheaper than lowest price", emoji = bot.get_emoji(955026117499183154), disabled = True)]])
          break
      except asyncio.TimeoutError:
        await msg.edit(components = [[Button(style = ButtonStyle.blue, label = "Pick my own price", emoji = bot.get_emoji(955030104419995698), disabled = True), Button(style = ButtonStyle.blue, label = "Same as lowest price", emoji = bot.get_emoji(955028874213875802), disabled = True), Button(style = ButtonStyle.blue, label = "0.1 cheaper than lowest price", emoji = bot.get_emoji(955026117499183154), disabled = True)]])
        return
  try:
    abc = str(float(cost))
    cost = float(cost)
  except:
    await ctx.send(random.choice([
      "You must made a typo on entering your price! It must be a float number!",
      "Hey! Did you specify your cost correctly? It must be a float number!"
    ]))
  if cost > 1000000000000:
    await ctx.send(random.choice([
      "Your **price** is too high!",
      "Hey! You can't set the price that high!",
      "Lower down your price!",
      "Nobody is gonna buy that if your price is gonna be that high."
    ]) + " Your price can be at most 1,000,000,000,000 <:nerdies:932234563579682816>")
    return
  sept = abc.split(sep=".")
  if len(sept[1]) > 1:
    cost = round(float(cost), 1)
    await ctx.send("Because the cost you applied is %s decimal places and only need 1 decimal place, we will round it to 1 decimal places with value being %s <:nerdies:932234563579682816>" % (space(len(sept[1])), cost))
  market = json.load(open("market.json"))
  
  market[wtf.upper()].append({"amount": int(howmuch), "cost": float(cost), "author": ctx.author.id, "timestamp": int(round(time.mktime(datetime.datetime.utcnow().timetuple()), 0))})

  for i in profile[str(ctx.author.id)]["inventory"]:
    if i["name"] == wtf.upper():
      profile[str(ctx.author.id)]["inventory"][profile[str(ctx.author.id)]["inventory"].index(i)]["amount"] -= int(howmuch)
      found = True
      break
  for i in profile[str(ctx.author.id)]["inventory"]:
    if i["amount"] <= 0:
      profile[str(ctx.author.id)]["inventory"].remove(profile[str(ctx.author.id)]["inventory"][profile[str(ctx.author.id)]["inventory"].index(i)])

  pc = market[wtf.upper()]
  for i in pc:
    if i["amount"] <= 0:
      market[wtf.upper()].remove(i)
        
  json.dump(market, open("market.json", "w"))
  json.dump(profile, open("game.json", "w"))
  embed=discord.Embed(color = 0xfef000, title="Thanks for visiting Nerdmart!", description="You sucessfully queued " + str(space(int(howmuch))) + " " + items[wtf.upper()]["image"] + " " + items[wtf.upper()]["displayName"] + " for " + space(round(float(float(cost) * int(howmuch)),1)) + " <:nerdies:932234563579682816> in the NerdMart.\n\n" + "You will have to wait for others to buy your stuff in NerdMart to gain your nerdies! To check your queue, use `bruh sellqueue` to check your sell item's stats.", timestamp = datetime.datetime.utcnow())
  embed.set_footer(text="Market Power! | " + await getTime())
  await ctx.reply(embed=embed, mention_author = False)
  return
    









@bot.command(aliases = ["sq"])
@commands.cooldown(1, 5, commands.BucketType.user)
async def sellqueue(ctx, pagenum = None):

  if await checkReboot(ctx): return

  global shop, items

  market = json.load(open("market.json"))

  user = {}

  for i in market:
    thisfound = False
    kn = []
    for x in market[i]:
      if x["author"] == ctx.author.id:
        thisfound = True
        kn.append(x)
    if thisfound:
      user[i] = kn

  if isinstance(pagenum, str):
    item = pagenum.upper()
    try:
      dat = user[item]
    except KeyError:
      if item in items:
        await ctx.send(random.choice([
          "We don't sell those stuff in NerdMart.",
          "That item is not on NerdMart.",
          "You can't find those items in NerdMart."
        ]))
        return
      else:
        await ctx.send(random.choice([
          "Hey! That item dosen't exsist on NerdPlanet.",
          "I had never seen that item before. Does it even exsist?",
        ]))
        return
    queuestr = ""
    c = 0
    for i in dat:
      c += 1
      if c > 15:
        queuestr += f"`And {space(len(dat))} more queues...`\n"
        break
      else:
        try:
          queuestr += f"{c}. **Time**: <t:{i['timestamp']}>, **Amount**: {space(i['amount'])}, **Price**: {space(i['cost'])}\n"
        except:
          queuestr += f"{c}. **Time**: `Unknown`, **Amount**: {space(i['amount'])}, **Price**: {space(i['cost'])}\n"
    embed=discord.Embed(title=f"Sell queues on item **{items[item]['displayName']}**", color = 0xfef000)
    embed.set_thumbnail(url="https://www.saltyfishstudios.net/assets/sellrec.png")
    embed.add_field(name=f"{items[item]['rarietyImage']} {items[item]['image']} **{items[item]['displayName']}** `{items[item]['name']}`", value=queuestr, inline=False)
    await ctx.send(embed=embed)
    return

  if pagenum == None:
    pagenum = 0
  else:
    pagenum = int(pagenum)

  embed=discord.Embed(color = 0xfef000, title = "Your sell queues")
  embed.set_thumbnail(url = 'https://www.saltyfishstudios.net/assets/sellrec.png')
  count = 0
  costtotal = 0
  amounttotal = 0
  for i in shop[str(pagenum)]:
    try:
      amount = round(sum(item["amount"] for item in user[i]), 1)
      total = round(sum(item["cost"] for item in user[i]), 1)
      average = round(total / amount, 1)

      costtotal += total
      amounttotal += amount
    except:
      valuestr = f"*You didn't sell any of this item.*"
    else:
      valuestr = f"**Amount**: {inttostr(amount)}\n**Worth**: {inttostr(total)} <:nerdies:932234563579682816>\n**Average price per**: {inttostr(average)} <:nerdies:932234563579682816>"
    count += 1
    embed.add_field(name = f"{count}. {items[i]['rarietyImage']} {items[i]['image']} **{items[i]['displayName']}** `{items[i]['name']}`", value = valuestr, inline = False)
  embed.description = f"You have sold **{inttostr(amounttotal)}** items, in a total worth of **{inttostr(costtotal)}** <:nerdies:932234563579682816>\nUse `bruh sellqueue <item-id>` to view all sell queues you've made on that item."
  await ctx.send(embed=embed)








@bot.command(aliases = ["site", "website"])
@commands.cooldown(1, 5, commands.BucketType.user)
async def OpenWebSite(ctx):

  if await checkReboot(ctx): return

  card_footer = ["Why would you do that?",
      "Mr. Bob",
       "Why not a episode of sponge bob?",
       "Go away!",
       "Awesome!",
       "YUM!",
       "check our awesome site! bruh site"]
  

  embed=discord.Embed(color=0xfef000, timestamp = datetime.datetime.utcnow())
  embed.add_field(name="Our Amazing Site", value="Visit our amazing site over here!\nhttps://saltyfishstudios.net/nerd", inline=True)
  embed.set_footer(text=random.choice(card_footer) + " | " + await getTime())
  await ctx.send(embed=embed)












@bot.command(name = "credits", aliases = ["credit"])
@commands.cooldown(1, 5, commands.BucketType.user)
async def _credits(ctx):

  if await checkReboot(ctx): return

  embed=discord.Embed(color=0xfef000, title="Wonderful credit page", description="Check the list of wonderful credits!", timestamp = datetime.datetime.utcnow())
  embed.set_thumbnail(url="https://i.kym-cdn.com/photos/images/original/001/923/854/b67")
  embed.add_field(name="General Credits", value="• Website hoster - [GitHub](https://github.com/)\n• Bot hosting - [Replit](https://replit.com)", inline=True)
  embed.add_field(name="Inspiration & Influence", value="• Hypixel Skyblock - [Fourms](https://hypixel.net/forums/skyblock-general-discussion.157/), [Hypixel](https://hypixel.net)", inline=True)
  embed.set_footer(text=" | " + await getTime())
  await ctx.send(embed=embed)












@bot.command()
async def guessmynumber(ctx):

  if await checkReboot(ctx): return
  
  if await isBanned(ctx, ctx.author.id): return
    
  await ctx.send("I am thinking of a number between 1 to 100!\nTell me in the next 10 seconds!")
  number = random.randint(1, 100)

  def check(message):
    return message.channel == ctx.channel and message.author.id == ctx.author.id

  try:
    guess = True
    while guess:
      msg = await bot.wait_for("message", check = check, timeout = 10)
      try:
        if int(msg.content) == number:
          coins = round(random.random() * 50, 1)
          await ctx.send(random.choice([
        "WOW! YOU GOT IT!",
        "Nice job dude!",
        "Wow, you have it.",
        "OMG NICE!"
      ]) + " I was thinking %i.\nTake your %s <:nerdies:932234563579682816>" % (number, coins))
          await giveCoins(ctx.author.id, coins)
          return
        elif int(msg.content) > number:
          await ctx.send("Too large! Try again!")
        elif int(msg.content) < number:
          await ctx.send("Too small! Try again!")
      except ValueError:
        await ctx.send(random.choice([
          "WHY TEXT???",
          "You know I don't like text.",
          "I wan't a number not a text.",
          "`$ sudo nuke text` I am going to nuke your text and make it a number.",
          "Please send numbers :(",
          "NO NUMBERS!",
          "Please, no numbers."
        ]))
        return
  except asyncio.exceptions.TimeoutError:
    await ctx.send(random.choice([
      "Aww man. No games.",
      "TOO LONG, WAY TOOOOOOOOOO LONG!",
      "Bruh I am not going to wait you.",
      "10 seconds is long dude, no need to think that long."
    ]))
    return
  await ctx.send(msg.content + " :poop:")







@bot.command(name="guesscoin")
@commands.cooldown(1, 10, commands.BucketType.user)
async def guesscoin(ctx):

  if await checkReboot(ctx): return

  if await isBanned(ctx, ctx.author.id): return

  coin = random.choice(["head", "tail"])

  msg = await ctx.send("I flipped a coin! Is it heads or tails?", components = [[Button(style=ButtonStyle.gray, label="Heads", custom_id = "0"), Button(style=ButtonStyle.gray, label="Tails", custom_id = "1")]])


  try:
    errs = 0
    while True:
      choice = await bot.wait_for("button_click", check = lambda i: i.channel.id == ctx.channel.id, timeout = 10)
      if choice.user.id != ctx.author.id:
        errs += 1
        if errs >= 20:
          await ctx.reply("Looks like too many people are playing with your coin, not their own!\nI have to stop this guessy-coin-thingy.")
          return
        else:
          await choice.send(random.choice([
            "Hey! This is not your coin!.",
            "Play your own game.",
            "This is not your coin.",
            "Use your own coin!",
            f"This is {ctx.author.name}'s coin! Not yours!"
          ]))
      else:
        break
    if choice.custom_id == "0":
      c = "head"
    elif choice.custom_id == "1":
      c = "tail"
    
    if c == coin:
      c = round(random.random() * 50, 1)
      await choice.send(f"Wow! You are correct!\nTake your {c} <:nerdies:932234563579682816>", ephemeral = False)
      await giveCoins(ctx.author.id, c)
      return
    else:
      await choice.send(f"Nope! It is {coin}s", ephemeral = False)
      return
  except asyncio.exceptions.TimeoutError:
    await msg.edit(components = [[Button(style=ButtonStyle.gray, label="Heads", disabled = True), Button(style=ButtonStyle.gray, label="Tails", disabled = True)]])
    return


HANGMAN_SHOP = ["HANGMAN"]

@bot.command(name="hangman")
@commands.cooldown(1, 15, commands.BucketType.user)
async def hangman(ctx, arg1 = None, arg2 = None, arg3 = None):

  if await isBanned(ctx, ctx.author.id): return
  
  RANDOM = discord.Color.from_rgb(random.randint(20,255),random.randint(20,255),random.randint(20,255))
  



  if arg1 == "shop":

    if arg2 == "buy":
      if arg3 == None:
        await ctx.send("Well what do you want to buy?")
        return

      if arg3.upper() == "HANGMAN":
        profile = json.load(open("game.json"))
        if profile[str(ctx.author.id)]["nerdies"]["wallet"] < 150:
          await ctx.send("`HANGMAN`: %s" % random.choice([
            "HEY! I AM NOT DUMB! YOU DON'T HAVE ENOUGH MONEY!",
            "I'M NOT A FOOL, YOU DON'T HAVE ENOUGH MONEY- I MEAN NERDIES!",
            "Get 150 nerdies then find me.",
            "Find your 150 nerdies first."
          ]))
          return
        else:
          found = False
          for i in profile[str(ctx.author.id)]["inventory"]:
            if i["name"] == "HANGMAN" and i["data"] == {}:
              profile[str(ctx.author.id)]["inventory"][profile[str(ctx.author.id)]["inventory"].index(i)]["amount"] += 1
              found = True
              break
          if not found:
            profile[str(ctx.author.id)]["inventory"].append({"name": "HANGMAN", "amount": 1, "data": {}})
          json.dump(profile, open("game.json", "w"))
          embed=discord.Embed(color = RANDOM, title="Thanks for visiting Hangman shop!", description="You sucessfully purchased 1" + " " + "<:hangmancard:935880264180191302>" + " " + "Hangman Card" + " for " + space(round(150.0, 1)) + "<:nerdies:932234563579682816>", timestamp = datetime.datetime.utcnow())
          embed.set_footer(text="Thanks for your purchase! | " + await getTime())
          await ctx.send(embed=embed)
          return
      else:
        await ctx.send("Well does that thing exsist?")
        return
    global items
    global HANGMAN_SHOP
    embed=discord.Embed(color = RANDOM, timestamp = datetime.datetime.utcnow(), title="Hangman Shop", description=f"Welcome to the hangman shop, {ctx.author.name}! Use `bruh hangman shop buy <id>` to buy something!\nIf you are finding NerdMart, use `bruh market`")
    for i in HANGMAN_SHOP:
      embed.add_field(name=items[i]["rarietyImage"] + " " + items[i]["image"] + " " + items[i]["displayName"] + " `" + i + "`" + " - " + space(items[i]["cost"]) + " <:nerdies:932234563579682816>", value="- " + items[i]["description"], inline=False)
    await ctx.send(embed=embed)
    return

  global words
  embed=discord.Embed(color = RANDOM, title="Hangman Game!", description = "The classic hangman game! You have 10 seconds for each guess!")
  rand = random.choice(words)
  onguess = True
  guess = 10
  guess_str = ""
  cur_str = ""
  used = []
  got = []
  errors = 0

  if hastagdata(ctx.author.id, "--has-hangman-card", True):
    untag(ctx.author.id, "--has-hangman-card")
    await ctx.send(random.choice([
      "Because you have a peechy-poochy-hangman-guess-thingy, the hangman gave you a free guess! (correct letters + 1)",
    ]))
    got.append(random.choice(list(rand)))
    for i in rand:
      if i in got:
        guess_str += "%s " % i.upper()
        cur_str += "%s" % i.lower()
      elif not i.isalpha():
        guess_str += "  "
        cur_str += " "
      elif i.isalpha():
        guess_str += "_ "
        cur_str += "_"
  else:
    
    for i in rand:
      if i.isalpha():
        guess_str += "_ "
      elif not i.isalpha():
        guess_str += "  "
        cur_str += " "
  embed.add_field(name="%s guesses left!" % guess, value="`%s`" % guess_str, inline=True)
  if len(used) == 0:
    embed.add_field(name=":x: Wrong Guesses", value="None!", inline=False)
  else:
    embed.add_field(name=":x: Wrong Guesses", value=" ".join(used), inline=False)
  await ctx.send(embed=embed)

  def check(message):
    return message.channel == ctx.channel and message.author.id == ctx.author.id

  while onguess:
    try:
      guess_str = ""
      cur_str = ""
      char = await bot.wait_for("message", check = check, timeout = 10)
      if len(char.content) > 1:
        errors += 1
        if errors >= 5:
          raise SyntaxError
        await ctx.send("Hey! Just guess a character! Try again.")
        continue
      if not char.content.isalpha():
        errors += 1
        if errors >= 5:
          raise SyntaxError
        await ctx.send("Hey! Send me alphabets! Not illegal charachers! Try again.")
        continue

      if char.content.upper() in used:
        errors += 1
        if errors >= 5:
          raise SyntaxError
        await ctx.send("Dude, you already guessed this character and it is wrong! Try again.")
        continue

      if char.content.lower() in got:
        errors += 1
        if errors >= 5:
          raise SyntaxError
        await ctx.send("Dude, you already guessed this character and it is correct! Try again.")
        continue
      
      if char.content.lower() in rand:
        got.append(char.content.lower())
        embed=discord.Embed(color = RANDOM, title="Hangman Game!", description = random.choice([
        "You got one of the characters! It is %s",
        "Wow, you got one! It is %s",
        "Nice guess! It is %s",
        "Cool! You got one! It is %s"
        ]) % char.content.upper())
        
      else:
        used.append(char.content.upper())
        embed=discord.Embed(color = RANDOM, title="Hangman Game!", description = random.choice([
        "Nope, it is not %s",
        "Definitly not %s",
        "It is not %s",
        "Bad guess! Not %s"
        ]) % char.content.upper())
        guess -= 1

      for i in rand:
        if i in got:
          guess_str += "%s " % i.upper()
          cur_str += "%s" % i.lower()
        elif not i.isalpha():
          guess_str += "  "
          cur_str += " "
        elif i.isalpha():
          guess_str += "_ "
          cur_str += "_"
      if guess <= 0:
        embed.add_field(name="You Lose!", value="The word is: `%s`" % rand, inline=True)
        await ctx.send(embed=embed)
        return
      if cur_str == rand:
        amount = round(random.random() * random.randint(50, 1000), 1)
        embed.add_field(name="Congratulations! You got it!", value=f"The word is: `%s`\nTake your {amount} <:nerdies:932234563579682816>" % rand, inline=True)
        profile = json.load(open("game.json"))
        profile[str(ctx.author.id)]["nerdies"]["wallet"] += amount
        profile[str(ctx.author.id)]["nerdies"]["wallet"] = round(profile[str(ctx.author.id)]["nerdies"]["wallet"], 1)
        json.dump(profile, open("game.json", "w"))
        await ctx.send(embed=embed)
        if genRarity(1):
          await ctx.send(f"Also, the hangman was so happy, so he gave you {space(100000)} <:nerdies:932234563579682816>! What a guy!")
          profile = json.load(open("game.json"))
          profile[str(ctx.author.id)]["nerdies"]["wallet"] += 100000
          profile[str(ctx.author.id)]["nerdies"]["wallet"] = round(profile[str(ctx.author.id)]["nerdies"]["wallet"], 1)
          json.dump(profile, open("game.json", "w"))
        elif genRarity(0.1):
          await ctx.send(f"Also, the hangman was so happy, so he gave you {space(1000000)} <:nerdies:932234563579682816>! What a guy!")
          profile = json.load(open("game.json"))
          profile[str(ctx.author.id)]["nerdies"]["wallet"] += 1000000
          profile[str(ctx.author.id)]["nerdies"]["wallet"] = round(profile[str(ctx.author.id)]["nerdies"]["wallet"], 1)
          json.dump(profile, open("game.json", "w"))

        if genRarity(10):
          await ctx.send("The hangman give you a reminder of his shop! Use `bruh hangman shop`.")

        return
      embed.add_field(name="%s guesses left!" % guess, value="`%s`" % guess_str, inline=True)
      if len(used) == 0:
        embed.add_field(name=":x: Wrong Guesses", value="None!", inline=False)
      else:
        embed.add_field(name=":x: Wrong Guesses", value=" ".join(used), inline=False)
      await ctx.send(embed=embed)

      

      
    except asyncio.exceptions.TimeoutError:
      await ctx.send("Hmm, hangman is over.")
      return
    except SyntaxError:
      await ctx.send(random.choice([
        "Bro why are you making so many mistakes? This game is gone now!",
        "You are making too much mistakes and the game stopped.",
        "Too many simple mistakes! The game crashed!"
      ]))
      return
  


@bot.command(aliases = ['tip'])
async def tips(ctx):

  if await checkReboot(ctx): return

  await ctx.send("**DO YOU KNOW?** " + random.choice([
    "This is a useless tip.",
    "You can get more tips by using `bruh tips`",
    "Most of the commands have aliases! Check out a full list of command aliases using `bruh help` or visiting https://nerdbot.saltyfishstudios.net/commands.",
  ]))





@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def pay(ctx, who = None, amount = None):

  if await checkReboot(ctx): return

  await checkAccountExsists(ctx.author.id)

  phone = False

  if who == None:
    await ctx.send("You can't pay *nobody*! Mention a user that you want to pay for!\nThe format for paying people is `bruh pay <user or phone number> <amount>`")
    return

  if amount == None:
    await ctx.send("How much Nerdies do you wanna pay???\nThe format for paying people is `bruh pay <user or phone number> <amount>`")
    return

  try:
    amount = int(amount)
  except:
    await ctx.send(f"I can't give **{amount}** Nerdies! That's not a valid number!")
    return

  try:
    user = bot.get_user(int(who.replace("<", "").replace(">", "").replace("@", "").replace("!", "")))
  except:
    await ctx.send(f"Please mention a valid user or provide a valid phone number! Not {who}.\nThe format for paying people is `bruh pay <user or phone number> <amount>`")
    return

  if ctx.guild.get_member(int(who.replace("<", "").replace(">", "").replace("@", "").replace("!", ""))) == None:
    user = user_by_phone(int(who))
    if user == None:
      await ctx.send(f"The user that you specified either dosen't exsist or isn't in your server! You can try paying to them using their phone number *(if you know)*.\nThe format for paying people is `bruh pay <user or phone number> <amount>`") 
      return
    if user == ctx.author.id:
      await ctx.send(f"You cannot pay yourself Nerdies! That's not fun at all!\nThe format for paying people is `bruh pay <user or phone number> <amount>`")
      return
    phone = True

  if user == None:
    await ctx.send(f"Please mention a valid user! Not {who}.\nThe format for paying people is `bruh pay <user or phone number> <amount>`")
    return

  if not phone:
    if user.bot:
      await ctx.send("You can't pay *BOTS*, they won't spend it!\nThe format for paying people is `bruh pay <user or phone number> <amount>`")
      return

  

  profile = json.load(open("game.json"))
  
  if profile[str(ctx.author.id)]["nerdies"]["wallet"] < amount:
    await ctx.send("You need more Nerdies to give that much!")
    return

  if phone:
    user = user_by_phone(int(who))
  else:
    user = who.replace("<", "").replace(">", "").replace("@", "").replace("!", "")
    
  profile[str(ctx.author.id)]["nerdies"]["wallet"] -= amount
  profile[str(ctx.author.id)]["nerdies"]["wallet"] = round(profile[str(ctx.author.id)]["nerdies"]["wallet"], 1)
  profile[str(user)]["nerdies"]["wallet"] += amount
  profile[str(user)]["nerdies"]["wallet"] = round(profile[str(user)]["nerdies"]["wallet"], 1)
  json.dump(profile, open("game.json", "w"))
  if phone:
    embed=discord.Embed(title="Sucessful Pay!", description=f'You had sucessfully paid **{space(amount)}** <:nerdies:932234563579682816> to {user_by_phone_str(int(who))}', color=0xfef000)
  else:
    embed=discord.Embed(title="Sucessful Pay!", description=f'You had sucessfully paid **{space(amount)}** <:nerdies:932234563579682816> to <@{who.replace("<", "").replace(">", "").replace("@", "").replace("!", "")}>', color=0xfef000)
  if phone:
    await newNotif(int(user), "SYSTEM", "You recieved Nerdies!", f"You have recieved **{space(amount)}** <:nerdies:932234563579682816> from **{phonestr(profile[str(ctx.author.id)]['phone'])}**", "SYSTEM", True)
  else:
    await newNotif(int(user), "SYSTEM", "You recieved Nerdies!", f"You have recieved **{space(amount)}** <:nerdies:932234563579682816> from **{ctx.author.name}#{ctx.author.discriminator}**", "SYSTEM", True)
  await ctx.send(embed=embed)
  




@bot.command(name="menu")
@commands.cooldown(1, 20, commands.BucketType.user)
async def menu(ctx):

  if await checkReboot(ctx): return

  if await isBanned(ctx, ctx.author.id): return
  
  card_footer = ["Why would you do that?",
      "Mr. Bob",
       "Why not a episode of sponge bob?",
       "Go away!",
       "Awesome!",
       "YUM!",
       "check our awesome site! bruh site"]
  f = json.load(open("game.json"))
  totaleco = 0
  for i in f:
    targ = f[i]
    totaleco += targ["nerdies"]["wallet"]
    for i in targ["nerdies"]["bank"]:
      totaleco += i["amount"]
  totalecostr = "{:,}".format(totaleco)


  value = "Profiles: `%i`\nTotal Economy Money: `%s`\nServer Count: `%s`" % (len(json.load(open("game.json"))), totalecostr, len(bot.guilds))

  embed=discord.Embed(color = 0xfef200, title="Hi %s, I am Nerd!" % ctx.author.name, description="Nerd Bot Does Nerdie Stuff.", timestamp = datetime.datetime.utcnow())
  embed.add_field(name="Statistics", value=value, inline=False)
  embed.add_field(name="Recent Updates", value=UPDATES, inline=True)
  embed.set_footer(text=random.choice(card_footer) + " | " + await getTime())
  await ctx.send(embed=embed)





@bot.command(aliases = ["phonenum", "pn"])
@commands.cooldown(1, 10, commands.BucketType.user)
async def phone(ctx):

  if await checkReboot(ctx): return

  await checkAccountExsists(ctx.author.id)
  
  if await isBanned(ctx, ctx.author.id): return
  
  msg = await ctx.send("Click the `Read My Phone Information` button below to get your phone information!", components = [Button(style = ButtonStyle.blue, custom_id = "READ", label = "Read My Phone Information")])

  try:
    data = await bot.wait_for("button_click", check = lambda i: i.message.id == msg.id and i.custom_id == "READ", timeout = 20)
    profile = json.load(open("game.json"))
    embed=discord.Embed(title="Your phone information", color=0xfef000)
    embed.add_field(name="Full Phone Number", value=f"This parameter is the full string of your phone number.\n`{profile[str(ctx.author.id)]['phone']}`", inline=True)
    embed.add_field(name="String Phone Number", value=f"This parameter is the string version of your phone number. Displayed in messages and notifications\n`{phonestr(profile[str(ctx.author.id)]['phone'])}`", inline=True)
    await data.send(embed=embed)
    raise asyncio.TimeoutError
  except asyncio.TimeoutError:
    await msg.edit(components = [Button(style = ButtonStyle.blue, disabled = True, label = "Read My Phone Information")])






@bot.command(name = "api")
@commands.cooldown(1, 120, commands.BucketType.user)
async def apikey(ctx, arg1 = None):

  if await checkReboot(ctx): return

  if await isBanned(ctx, ctx.author.id): return

  d = json.load(open("apikey.json"))
  if d[str(ctx.author.id)]["expires"] < round(time.time()) and arg1 == None:
    await ctx.send("Your API key is outdated or expired. Use `bruh api regenerate` to regenerate a new one.")
    return

  if str(ctx.author.id) in d:
    if arg1 in ["regen", "regenerate"]:
      pass
    else:
      await ctx.send("You already had generated an API key. Use `bruh api regenerate` to regenerate a new one.")
      return

  dat = json.load(open("apiuse.json"))
  if dat.get(str(ctx.author.id), None) == None:
    dat[str(ctx.author.id)] = 1
  else:
    dat[str(ctx.author.id)] += 1
  if dat[str(ctx.author.id)] > 3:
    await ctx.send("You have reached your API key regeneration limit. Please try again after today.")
    return
  json.dump(dat, open("apiuse.json", "w"))

  

  expires = (datetime.datetime.utcnow() + datetime.timedelta(days=30))
  K = generatekey(ctx.author.id, expires)
  
  msg = await ctx.send("We have generated a new API key for you! Click the button in the next 20 secodns to reval!", components = [Button(style=ButtonStyle.blue, label="Fetch API Key", custom_id="btn1")])
  try:
    interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "btn1", timeout = 20)
  except asyncio.exceptions.TimeoutError:
    await msg.edit(components = [Button(style=ButtonStyle.blue, label="Fetch API Key", disabled = True)])
    return
  await interaction.send("API key: `%s`" % K)
  await msg.edit(components = [Button(style=ButtonStyle.blue, label="Fetch API Key", custom_id="btn1", disabled = True)])

  





COOLDOWN_BYPASS = json.load(open("cooldown-bypass.json"))




### AFTER INVOKE QUEST AREA ###############
async def commandAfterInvoke(command_name, ctx):

  global COOLDOWN_BYPASS, ONGOING_TASKS
  
  await checkExsistingCommandUserQuests(command_name, ctx)

  if ctx.author.id in COOLDOWN_BYPASS:
    ctx.command.reset_cooldown(ctx)

  
  
async def commandBeforeInvoke(command_name, ctx):

  pass

  


async def checkExsistingCommandUserQuests(command_name, ctx):
  data = json.load(open("user-quests.json"))
  try:
    cc = data[str(ctx.author.id)]["objective"]
  except KeyError:
    return
  for i in cc:
    if i["type"] == "command-execute" and command_name == i["data"] and not data[str(ctx.author.id)]["completed"]:
      data[str(ctx.author.id)]["objective"][data[str(ctx.author.id)]["objective"].index(i)]["current"] += 1
      json.dump(data, open("user-quests.json", "w"))
  falses = 0
  for i in data[str(ctx.author.id)]["objective"]:
    if i["current"] >= i["goal"] and not data[str(ctx.author.id)]["completed"]:
      pass
    else:
      falses += 1
  if falses <= 0:
    for i in data[str(ctx.author.id)]["rewards"]:
      if i["type"] == "next-stage":
        data[str(ctx.author.id)]["stage"] += 1
        data[str(ctx.author.id)]["completed"] = True
        json.dump(data, open("user-quests.json", "w"))
        await startQuest(ctx, ctx.author.id, data[str(ctx.author.id)]["name"], isNextStage = True)
  else:
    pass

  
  




@_quest.before_invoke
async def _quest_before_invoke(ctx): await commandBeforeInvoke('_quest', ctx)
@_reset.before_invoke
async def _reset_before_invoke(ctx): await commandBeforeInvoke('_reset', ctx)
@_plot.before_invoke
async def _plot_before_invoke(ctx): await commandBeforeInvoke('_plot', ctx)
@_consume.before_invoke
async def _consume_before_invoke(ctx): await commandBeforeInvoke('_consume', ctx)
@_bounty.before_invoke
async def _bounty_before_invoke(ctx): await commandBeforeInvoke('_bounty', ctx)
@_word.before_invoke
async def _word_before_invoke(ctx): await commandBeforeInvoke('_word', ctx)
@_make5.before_invoke
async def _make5_before_invoke(ctx): await commandBeforeInvoke('_make5', ctx)
@poop.before_invoke
async def poop_before_invoke(ctx): await commandBeforeInvoke('poop', ctx)
@_message.before_invoke
async def _message_before_invoke(ctx): await commandBeforeInvoke('_message', ctx)
@notifications.before_invoke
async def notifications_before_invoke(ctx): await commandBeforeInvoke('Notifis', ctx)
@profile.before_invoke
async def profile_before_invoke(ctx): await commandBeforeInvoke('profile', ctx)
@checkInventory.before_invoke
async def checkInventory_before_invoke(ctx): await commandBeforeInvoke('checkInventory', ctx)
@withdrawFromBank.before_invoke
async def withdrawFromBank_before_invoke(ctx): await commandBeforeInvoke('withdrawFromBank', ctx)
@helpOnCommand.before_invoke
async def helpOnCommand_before_invoke(ctx): await commandBeforeInvoke('helpOnCommand', ctx)
@NerdMart.before_invoke
async def NerdMart_before_invoke(ctx): await commandBeforeInvoke('NerdMart', ctx)
@sell.before_invoke
async def sell_before_invoke(ctx): await commandBeforeInvoke('_sell', ctx)
@OpenWebSite.before_invoke
async def OpenWebSite_before_invoke(ctx): await commandBeforeInvoke('OpenWebSite', ctx)
@guessmynumber.before_invoke
async def guessmynumber_before_invoke(ctx): await commandBeforeInvoke('guessmynumber', ctx)
@guesscoin.before_invoke
async def guesscoin_before_invoke(ctx): await commandBeforeInvoke('guesscoin', ctx)
@hangman.before_invoke
async def hangman_before_invoke(ctx): await commandBeforeInvoke('hangman', ctx)
@menu.before_invoke
async def menu_before_invoke(ctx): await commandBeforeInvoke('menu', ctx)
@apikey.before_invoke
async def apikey_before_invoke(ctx): await commandBeforeInvoke('apikey', ctx)
@iwantnerdies.before_invoke
async def iwantnerdies_before_invoke(ctx): await commandBeforeInvoke('iwantnerdies', ctx)




@_quest.after_invoke
async def _quest_after_invoke(ctx): await commandAfterInvoke('_quest', ctx)
@_reset.after_invoke
async def _reset_after_invoke(ctx): await commandAfterInvoke('_reset', ctx)
@_plot.after_invoke
async def _plot_after_invoke(ctx): await commandAfterInvoke('_plot', ctx)
@_consume.after_invoke
async def _consume_after_invoke(ctx): await commandAfterInvoke('_consume', ctx)
@_bounty.after_invoke
async def _bounty_after_invoke(ctx): await commandAfterInvoke('_bounty', ctx)
@_word.after_invoke
async def _word_after_invoke(ctx): await commandAfterInvoke('_word', ctx)
@_make5.after_invoke
async def _make5_after_invoke(ctx): await commandAfterInvoke('_make5', ctx)
@poop.after_invoke
async def poop_after_invoke(ctx): await commandAfterInvoke('poop', ctx)
@_message.after_invoke
async def _message_after_invoke(ctx): await commandAfterInvoke('_message', ctx)
@notifications.after_invoke
async def notifications_after_invoke(ctx): await commandAfterInvoke('Notifis', ctx)
@profile.after_invoke
async def profile_after_invoke(ctx): await commandAfterInvoke('profile', ctx)
@checkInventory.after_invoke
async def checkInventory_after_invoke(ctx): await commandAfterInvoke('checkInventory', ctx)
@withdrawFromBank.after_invoke
async def withdrawFromBank_after_invoke(ctx): await commandAfterInvoke('withdrawFromBank', ctx)
@helpOnCommand.after_invoke
async def helpOnCommand_after_invoke(ctx): await commandAfterInvoke('helpOnCommand', ctx)
@NerdMart.after_invoke
async def NerdMart_after_invoke(ctx): await commandAfterInvoke('NerdMart', ctx)
@sell.after_invoke
async def sell_after_invoke(ctx): await commandAfterInvoke('_sell', ctx)
@OpenWebSite.after_invoke
async def OpenWebSite_after_invoke(ctx): await commandAfterInvoke('OpenWebSite', ctx)
@guessmynumber.after_invoke
async def guessmynumber_after_invoke(ctx): await commandAfterInvoke('guessmynumber', ctx)
@guesscoin.after_invoke
async def guesscoin_after_invoke(ctx): await commandAfterInvoke('guesscoin', ctx)
@hangman.after_invoke
async def hangman_after_invoke(ctx): await commandAfterInvoke('hangman', ctx)
@menu.after_invoke
async def menu_after_invoke(ctx): await commandAfterInvoke('menu', ctx)
@apikey.after_invoke
async def apikey_after_invoke(ctx): await commandAfterInvoke('apikey', ctx)
@iwantnerdies.after_invoke
async def iwantnerdies_after_invoke(ctx): await commandAfterInvoke('iwantnerdies', ctx)





def generatekey(authorid, expires):
  KEYS = json.load(open("apikey.json"))
  key = base64.b64encode(str(uuid.uuid4()).replace("-", "").encode("ascii")).decode("ascii")
  KEYS[str(authorid)] = {"value": key, "expires": round(time.mktime(expires.timetuple()))}
  json.dump(KEYS, open("apikey.json", "w"))
  return key


def checkKey(key):
  KEYS = json.load(open("apikey.json"))
  found = False
  for i in KEYS:
    if KEYS[i]["value"] == key:
      found = True
      if KEYS[i]["expires"] == -1:
        pass
      elif KEYS[i]["expires"] < time.mktime(datetime.datetime.utcnow().timetuple()):
        return (False, "The API key is expired and unusable anymore. Please regenerate a new API key using the NerdBot.", 401)
      return (True, None, 200)
    if not found:
      return (False, "The API key is invalid and does not exsist. Did you type something wrong?", 401)
    else:
      return (True, None, 200)
    
app = Flask('')
cors = CORS(app, resources={r"/v0/get-ban-information": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.errorhandler(404)
def e404(e):
  return jsonify({"sucess": False, "message": "Not found."}), 404

@app.errorhandler(405)
def e405(e):
  return jsonify({"sucess": False, "message": "Method not allowed."}), 405

@app.errorhandler(500)
def e500(e):
  return jsonify({"sucess": False, "message": "The server occured a fatal error. Please contact the server administrator if you have a concern about this."}), 500






  



@app.route('/v0/get-ban-information', methods=["GET"])
@cross_origin(origin='*',headers=['Content-Type','Auth'])
def get_ban():
  
  
  ck = checkKey(request.headers.get("Auth", None))
  if not ck[0]:
    return jsonify({"sucess": ck[0], "message": ck[1]}), ck[2]
  
  banid = request.args.get("banid", None)
  if banid == None:
    return jsonify({"sucess": False, "message": "Bad request: one or more parametes missing."}), 400
  select = json.load(open("banned.json"))
  find = None
  for i in select:
    if select[i]["id"] == banid:
      find = select[i]
  if find == None:
    return jsonify({"sucess": False, "message": "Ban ID not found."}), 404
  return jsonify(find), 200


  






@app.route('/v0/submit-ban-appeal', methods=["POST"])
@cross_origin(origin='*',headers=['Content-Type','Auth', "Id", "Explaination"])
def post_ban():
  ck = checkKey(request.headers.get("Auth", None))
  if not ck[0]:
    return jsonify({"sucess": ck[0], "message": ck[1]}), ck[2]

  banid = request.headers.get("Id", None)
  exp = request.headers.get("Explaination", None)

  if banid == None or exp == None:
    return jsonify({"sucess": False, "message": "Bad request: one or more parametes missing."}), 400
  
  select = json.load(open("banned.json"))
  find = None
  d = None
  for i in select:
    if select[i]["id"] == banid:
      find = select[i]
      d = i
  if find == None:
    return jsonify({"sucess": False, "message": "Ban ID not found."}), 404
  dd = json.load(open("appeals.json"))
  dd.append({"user": d, "explaination": exp, "id": banid})
  json.dump(dd, open("appeals.json", "w"))
  return jsonify({"sucess": True}), 200


def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()
    
keep_alive()
try:
  pass
  bot.run(os.environ['token'])
except:
  n = requests.get("https://discord.com/api/v9/users/707072996346691645", headers = {"Authorization": "Bot ODk4OTEyMTk5NTE3NTU2Nzg2.YWrHOQ.2lj7JAj0ulTmhHM3cjAWeQ4H5Jc"})
  retryAfter = n.headers.get("Retry-After")
  delta = datetime.timedelta(seconds=int(retryAfter))
  now = datetime.datetime.utcnow()
  retry = now + delta
  print(f"""BOT IS RATE LIMITED
Retry After:    {retryAfter} seconds.
Retry At (UTC): {retry}
Now (UTC):      {now}
""")
