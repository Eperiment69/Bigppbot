#import stuff
import os
import discord
from discord.ext import commands
import random
from replit import db
import requests
import json
from links import pissedoff, waifuu, topicsfw, topicnsfw
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
async def howsimpami(ctx):
  simppercent = random.randint(1,100)
  await ctx.send('You are '+ str(simppercent) + '% simp :smirk:')

@client.command()
async def howthotami(ctx):
  thotpercent = random.randint(1,100)
  await ctx.send('You are '+ str(thotpercent) + '% thot :peach:') 


@client.command()
async def toss(ctx):
  coin = random.randint(0,1)
  if coin == 0:
    await ctx.send("Heads")
  if coin == 1:
    await ctx.send('Tails')

@client.command()
async def rr(ctx):
  await ctx.send('You have started Russian Roulette')
  bullets = random.randint(1,6)
  if bullets == 6 or bullets == 3:
    await ctx.send("Bang! You died, Try again")
  else:
    await ctx.send('You survived smol pp boi')
    
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
async def pissoff(ctx):
  pissoff = pissedoff
  await ctx.send(random.choice(pissoff))  
  
@client.command()
async def waifu(ctx):
  waifu = waifuu
  await ctx.send(random.choice(waifu))
  
@client.command()
async def nudes(ctx):
  link = 'https://media0.giphy.com/media/Ju7l5y9osyymQ/giphy.gif?cid=ecf05e47elbtxq3txc1cmkeqv4vd1fd74i41xjy5f5fznuwf&rid=giphy.gif&ct=g'
  await ctx.send(link + '\n no nudes here, only rickroll')

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
  link = response_json[0]["url"]
  await ctx.send(link)
    
@client.command()
async def sfw(ctx):
    url = json.loads(requests.get('https://api.waifu.pics/sfw/' + str(random.choice(topicsfw))).text)['url']
    embed=discord.Embed(description="here's your pic :smile:")
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

@client.command()
async def hug(ctx):
  url = json.loads(requests.get('https://api.waifu.pics/sfw/hug').text)['url']
  await ctx.send(url)

@client.command()
async def kick(ctx):
  url = json.loads(requests.get('https://api.waifu.pics/sfw/kick').text)['url']
  await ctx.send(url)

@client.command()
async def pat(ctx):
  url = json.loads(requests.get('https://api.waifu.pics/sfw/pat').text)['url']
  await ctx.send(url) 

@client.command()
async def kill(ctx):
  url = json.loads(requests.get('https://api.waifu.pics/sfw/kill').text)['url']
  await ctx.send(url)

@client.command()
async def gif_help(ctx):
  help = '```You can use the given gif commands:\n $nudes,\n $pissoff,\n $waifu,\n $cat,\n $dog,\n $sfw,\n $hug,\n $kick,\n $pat,\n $kill\n and a very secret command ;)```'
  await ctx.send(help)
          
client.run(os.getenv('TOKEN'))  


