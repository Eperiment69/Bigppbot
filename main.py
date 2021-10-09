#import stuff
import os
import discord
from discord.ext import commands
import random
from replit import db
import requests
import json
from links import hugs, pissedoff, waifuu, topicsfw, topicnsfw
# import interactions
description = "A bot, with big pp"
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='$', description=description, intents=intents)

def get_quote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + "    - ryan"
  return(quote)

sad_words = ["sad",'unhappy','depressed', 'wanna die', 'want to die', 'sed', 'bored']
discouragments = [
  'haha, sucks to be you',
  'Hope you give up',
  'You are worth nothing lmao',
  'You are an accident',
  'Never Gonna Give You Up'
]

@client.event
async def on_ready():
  print('You have a big pp {0.user} '.format(client))

@client.event
async def on_message(message):
      if message.author == client.user:
          return   
      elif any(word in message.content for word in sad_words):
          await message.channel.send(random.choice(discouragments))
      await client.process_commands(message)

def update_discouragement(discouraging_message):
  if discouragments in db.keys():
    pass

#commands
@client.command()
async def howbigpp(ctx):
    await ctx.send("U big pp man")

@client.command()
async def inspireusryan(ctx):
    quote = get_quote()
    await ctx.send(quote)

@client.command()
async def howgayami(ctx):
  gayperc = random.randint(1,100)
  await ctx.send("You are " + str(gayperc) + '% gay :rainbow_flag:')

@client.command()
async def toss(ctx):
  coin = random.randint(0,1)
  if coin == 0:
    await ctx.send("Heads")
  if coin == 1:
    await ctx.send('Tails')
    
@client.command()
async def ppsize(ctx):
    rand1 = random.choice([True, False])
    rand2 = random.randint(1,10)
    if rand1 == True:
        rand2 = int(rand2/2)
        ppsize = "=" * rand2
    else:
        ppsize = "=" * rand2
    if rand2 <= 5:
        comment = "smol pp"
    elif rand2 > 5:
        comment = "beeg pp"
    await ctx.send('your pp size is ' + '`8'+ ppsize + 'D`' + f'\n{comment}')
    
@client.command()
async def hug(ctx):
  hug = hugs
  await ctx.send(random.choice(hug))

@client.command()
async def pissoff(ctx):
  pissoff = pissedoff
  await ctx.send(random.choice(pissoff))  
  
@client.command()
async def waifu(ctx):
  waifu = waifuu
  await ctx.send(random.choice(waifu))
  
@client.command()
async def nudes(ctx):
  link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
  #gif = 'http://dozydozy.tumblr.com/post/3750667564'
  await ctx.send(link)

@client.command()
async def cat(ctx):
  link = 'https://api.thecatapi.com/v1/images/search'
  response = requests.get(link)
  response_json = json.loads(response.text)
  link = response_json[0]['url']
  await ctx.send(link)

@client.command()
async def dog(ctx):
  link = 'https://api.thedogapi.com/v1/images/search'
  response = requests.get(link)
  response_json = json.loads(response.text)
  link = response_json[0]['url']
  await ctx.send(link)  

@client.command()
async def howsimpami(ctx):
  simppercent = random.randint(1,100)
  await ctx.send('You are '+ str(simppercent) + '% simp :smirk:')

@client.command()
async def sfw(ctx):
    url = json.loads(requests.get('https://api.waifu.pics/sfw/' + str(random.choice(topicsfw))).text)["url"]
    embed=discord.Embed(description="here's your pic :smirk:")
    embed.set_image(url=url)
    await ctx.send(embed=embed)

@client.command()
async def nsfw(ctx):
  url = json.loads(requests.get('https://api.waifu.pics/nsfw/' + str(random.choice(topicnsfw))).text)["url"]
  embed=discord.Embed(description="We know what you are gonna do with this pic :smirk:")
  embed.set_image(url=url)
  if ctx.channel.is_nsfw():
    await ctx.send(embed=embed)
  else:
    await ctx.send("breh this is not an nsfw channel, you smol pp fellow")

client.run(os.getenv('TOKEN'))  



