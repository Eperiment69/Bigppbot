#!/usr/bin/env python
#import stuff

import os
import json
import nextcord
from nextcord.ext import commands
import random
secrets = json.load(open('secrets.json'))
import requests
from jikanpy import Jikan
from links import pissedoff, waifuu, topicsfw, topicnsfw
# import interactions
description = "A bot, with big pp"
intents = nextcord.Intents.all()
client = commands.Bot(command_prefix=commands.when_mentioned_or('`'), description=description, intents=intents)
jikan = Jikan()

sad_words = [' sad ',' unhappy ',' depressed ', ' wanna die ', ' want to die ', ' sed ', ' bored ',' lifeless ']
discouragments = [
  'haha, sucks to be you',
  'Hope you give up',
  'You are worth nothing lmao',
  'You are an accident',
  'Never Gonna Give You Up'
]

#functions 
def get_quote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + "    - ryan"
  return(quote)

class Deck:
    def __init__(self):
      self.deck = []
      self.suits = ['♥', '♦', '♣', '♠']
      for suit in self.suits: # generate all 52 cards
        for i in range(2, 11):
          self.deck.append(str(i) + suit)
        self.deck.append('J' + suit)
        self.deck.append('Q' + suit)
        self.deck.append('K' + suit)
        self.deck.append('A' + suit)
        self.deck.append('a' + suit)
    
    def deal(self, player): # deal card to player, remove from deck and return
      playerCard=random.choice(self.deck)
      player.append(playerCard)
      self.deck.remove(playerCard)
      return
    
    def calScore(self, playerdeck): # calculate score
      playerScore = 0
      for card in playerdeck:
        if card[0] == 'J' or card[:-1] == 'Q' or card[0] == 'K' or card[-1] == 10:
          playerScore += 10
        elif card[0] == 'A':
          playerScore += 11
        elif card[0] == 'a':
          playerScore += 1
        else:
          playerScore += int(card[0])
      return(playerScore)

def get_meme(self): # Get a meme from reddit
      meme = json.loads(requests.get("https://meme-api.herokuapp.com/gimme").text) # GET meme from api
      embed = nextcord.Embed(title=meme["title"]) # create embed
      embed.set_footer(text="u/" + meme["author"] + " - r/" + meme["subreddit"])
      embed.set_image(url=meme["url"])
      return embed # return meme with embed containing meme


@client.event
async def on_ready():
  print('You have a big pp {0.user} '.format(client))
@client.event
async def on_message(message):
      if message.author == client.user:
          return
      if len(message.content) > 30:
          return
      elif any(word in message.content for word in sad_words):
          if random.random() < 0.4:
            await message.channel.send(random.choice(discouragments))
      await client.process_commands(message)

#commands
@client.command()
async def howbigpp(ctx):
    await ctx.send("U big pp man")

@client.command()
async def inspireusryan(ctx):
    quote = get_quote()
    await ctx.send(quote)

@client.command()
async def meme(ctx):
      meme = json.loads(requests.get("https://meme-api.herokuapp.com/gimme").text) # GET meme from api
      embed = nextcord.Embed(title=meme["title"]) # create embed
      embed.set_footer(text="u/" + meme["author"] + " - r/" + meme["subreddit"])
      embed.set_image(url=meme["url"])
      await ctx.send(embed=embed)

@client.command()
async def sauce(ctx):
  gayperc = random.randint(1,100)
  await ctx.send("Open sauce baby, send pr :3\nhttps://github.com/Eperiment69/Bigppbot/")  
      
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
    embed=nextcord.Embed(description="here's your pic :smile:")
    embed.set_image(url=url)
    await ctx.send(embed=embed)

@client.command()
async def nsfw(ctx):
  url = json.loads(requests.get('https://api.waifu.pics/nsfw/' + str(random.choice(topicnsfw))).text)["url"]
  embed=nextcord.Embed(description="We know what you are gonna do with this pic :smirk:")
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
async def anime(ctx, *anime):
  try:
    output = jikan.search('anime', anime, parameters={'limit': 1})
    embed = nextcord.Embed(title = output['results'][0]['title'], description = output['results'][0]['synopsis'])
    embed.add_field(name = 'Score: ', value = output['results'][0]['score'])
    embed.add_field(name = 'Eps', value = output['results'][0]['episodes'])
    embed.set_image(url=output['results'][0]['image_url'])
    embed.add_field(name = 'Rated: ', value = output['results'][0]['rated'])
    embed.add_field(name = 'Date: ', value = output['results'][0]['start_date'] + ' - ' + output['results'][0]['end_date'])
    await ctx.send(embed=embed)
  except:
    await ctx.send("Not found")

@client.command()
async def gif_help(ctx):
  help = '```You can use the given gif commands:\n $nudes,\n $pissoff,\n $waifu,\n $cat,\n $dog,\n $sfw,\n $hug,\n $kick,\n $pat,\n $kill\n and a very secret command ;)```'
  await ctx.send(help)

@client.command()
async def bj(ctx):
  embed = nextcord.Embed(title='Black Jack', description='You have started Black Jack!')
  
  playercards = []
  dealercards = []
  deck = Deck()
  embed.add_field(name='Generating', value='Shuffling your cards!')
  await ctx.send(embed=embed)
  deck.deal(playercards)
  deck.deal(dealercards)
  embed = nextcord.Embed(title="Black Jack", description="Player cards: " + str(playercards) + "\ndealer cards: " + str(dealercards))
  embed.add_field(name='Black Jack',  value="Player score: " + str(deck.calScore(playercards)) + "\ndealer cards: " + str(deck.calScore(dealercards)))
  embed.add_field(inline=False, name='Black Jack', value="***HIT*** or ***STAND***")
  await ctx.send(embed=embed)

  def check(m):
   return m.author == ctx.author and m.channel == ctx.channel and \
        m.content.lower() in ["hit", "stand"]

  msg = await client.wait_for('message', check=check)

  if msg.content.lower() == "hit":
        embed.add_field(name='Generating', value='Shuffling your cards!')
        await ctx.send(embed=embed)
        deck.deal(playercards)
        deck.deal(dealercards)
        embed = nextcord.Embed(title="Black Jack", description="Player cards: " + str(playercards) + "\ndealer cards: " + str(dealercards))
        embed.add_field(name='Black Jack',  value="Player score: " + str(deck.calScore(playercards)) + "\ndealer cards: " + str(deck.calScore(dealercards)))
        embed.add_field(inline=False, name='Black Jack', value="***HIT*** or ***STAND***")
        await ctx.send(embed=embed)
  else:
    await ctx.send("invalid input")
    
    playerScore=deck.calScore(playercards)
    dealerScore=deck.calScore(dealercards)
    if dealerScore > 21:
      await ctx.send("Dealer busts! You win!")
    elif playerScore > 21:
      await ctx.send("You bust! Dealer wins!")
    elif playerScore > dealerScore and playerScore == 21:
      await ctx.send("You win!")
    elif playerScore > dealerScore and dealerScore == 21:
      await ctx.send("Dealer wins!")
    else:
      return
    deck.deal(playercards)
    deck.deal(dealercards)
    await ctx.send("player cards: " + str(playercards) + "\ndealer cards: " + str(dealercards))
    await ctx.send("player score: " + str(deck.calScore(playercards)) + "\ndealer cards: " + str(deck.calScore(dealercards)))

  msg = await client.wait_for('message', check=check)
  

  
  
client.run(secrets['TOKEN'])   
