#import stuff
import os
import discord
from discord.ext import commands
import random
from replit import db
import requests
import json
# import interactions
description = " Macky, smol pp "
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
  'You are worth nothing lmao'
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
  await ctx.send("You are " + str(gayperc) + '% gay')

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
    print(rand1 and rand2)
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
  hug = ['https://media0.giphy.com/media/l8ooOxhcItowwLPuZn/giphy.gif?cid=ecf05e47mi97mmlb52g2bxt31izuo825cinr2tpge26yi17b&rid=giphy.gif&ct=g', 'https://media2.giphy.com/media/4No2q4ROPXO7T6NWhS/giphy.gif?cid=ecf05e47mi97mmlb52g2bxt31izuo825cinr2tpge26yi17b&rid=giphy.gif&ct=g', 'https://media4.giphy.com/media/U4LhzzpfTP7NZ4UlmH/giphy.gif?cid=ecf05e47mi97mmlb52g2bxt31izuo825cinr2tpge26yi17b&rid=giphy.gif&ct=g', 'https://media2.giphy.com/media/ZBQhoZC0nqknSviPqT/giphy.gif?cid=ecf05e47mi97mmlb52g2bxt31izuo825cinr2tpge26yi17b&rid=giphy.gif&ct=g'] 
  await ctx.send(random.choice(hug))

@client.command()
async def pissoff(ctx):
  pissoff = ['https://media0.giphy.com/media/4WF4YilkoC7sjzG3TY/giphy.gif?cid=ecf05e47ay6qhakebn5ymu5s8cbkqyyixnivnmr1e6nrlyig&rid=giphy.gif&ct=g', 'https://media4.giphy.com/media/13sY5MBe3khsly/giphy.gif?cid=ecf05e47iq1eiwuo34nihcswb9pzoemf7af0lyufvmney3ec&rid=giphy.gif&ct=g', 'https://tenor.com/view/i-think-i-found-something-look-adam-dimarco-randall-carpio-the-order-i-discovered-something-gif-18043211', 'https://media1.giphy.com/media/uYOgd0l1uRVbq/giphy.gif?cid=ecf05e47f57wwzqcthwlgdlo1uhep9tilfanq4jfwrk01phf&rid=giphy.gif&ct=g']
  await ctx.send(random.choice(pissoff))    
    

client.run(os.getenv('TOKEN'))
