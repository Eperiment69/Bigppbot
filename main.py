import os
import discord
import requests
import json
import random
from replit import db


client = discord.Client()


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

def update_discouragement(discouraging_message):
  if discouragments in db.keys():
    pass



@client.event
async def on_ready():
  print('You have a big pp {0.user} '.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  msg = message.content

  if msg.startswith('$howbigpp'):
    await message.channel.send('U big pp man')

  
  if msg.startswith('$howppnitesh'):
    await message.channel.send('nitesh big pp, like very big, like this big 8=====================D')


  if msg.startswith('$inspireusryan'):
    quote = get_quote()
    await message.channel.send(quote)

  if msg.startswith('$howgayami'):
    await message.channel.send('U very gay man')

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice
    (discouragments))

client.run(os.getenv('TOKEN'))
