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
  hug = ['https://media0.giphy.com/media/l8ooOxhcItowwLPuZn/giphy.gif?cid=ecf05e47mi97mmlb52g2bxt31izuo825cinr2tpge26yi17b&rid=giphy.gif&ct=g', 'https://media2.giphy.com/media/4No2q4ROPXO7T6NWhS/giphy.gif?cid=ecf05e47mi97mmlb52g2bxt31izuo825cinr2tpge26yi17b&rid=giphy.gif&ct=g', 'https://media4.giphy.com/media/U4LhzzpfTP7NZ4UlmH/giphy.gif?cid=ecf05e47mi97mmlb52g2bxt31izuo825cinr2tpge26yi17b&rid=giphy.gif&ct=g', 'https://media2.giphy.com/media/ZBQhoZC0nqknSviPqT/giphy.gif?cid=ecf05e47mi97mmlb52g2bxt31izuo825cinr2tpge26yi17b&rid=giphy.gif&ct=g', 'https://media3.giphy.com/media/chyZacnjg8q0XMp8my/giphy.gif?cid=ecf05e47i55xjwhawhfoq4yhezhf4s7zk6ihm4eddzleznir&rid=giphy.gif&ct=g', 'https://media2.giphy.com/media/TiDgr2Zas5gZdoFJxR/giphy.gif?cid=ecf05e47gcvn45933e63ca95foapsx7z5h6m3301fclmdclf&rid=giphy.gif&ct=g', 'https://media2.giphy.com/media/NhjPhBQIIxdxm/giphy.gif?cid=790b7611ce653ccce81b60c01505dcb1ca4870bcf4dee63a&rid=giphy.gif&ct=g'] 
  await ctx.send(random.choice(hug))

@client.command()
async def pissoff(ctx):
  pissoff = ['https://media0.giphy.com/media/4WF4YilkoC7sjzG3TY/giphy.gif?cid=ecf05e47ay6qhakebn5ymu5s8cbkqyyixnivnmr1e6nrlyig&rid=giphy.gif&ct=g', 'https://media4.giphy.com/media/13sY5MBe3khsly/giphy.gif?cid=ecf05e47iq1eiwuo34nihcswb9pzoemf7af0lyufvmney3ec&rid=giphy.gif&ct=g', 'https://tenor.com/view/i-think-i-found-something-look-adam-dimarco-randall-carpio-the-order-i-discovered-something-gif-18043211', 'https://media1.giphy.com/media/uYOgd0l1uRVbq/giphy.gif?cid=ecf05e47f57wwzqcthwlgdlo1uhep9tilfanq4jfwrk01phf&rid=giphy.gif&ct=g', 'https://media0.giphy.com/media/QGzPdYCcBbbZm/giphy.gif?cid=ecf05e47pp88oj6knidhs9velp74dxbfb4d9kn26503rv6lf&rid=giphy.gif&ct=g', 'https://media0.giphy.com/media/x1kS7NRIcIigU/giphy.gifps://www.google.com/search?q=traps&iflsig=ALs-wAMAAAAAYV3VMJ_xVAI7i6FbVVjma0Ghw9f8XBuG?cid=ecf05e47oxfa5uvqzkwrsntc8fhomjzduagfsbv6r6v9kekm&rid=giphy.gif&ct=g', 'https://media2.giphy.com/media/XHr6LfW6SmFa0/giphy.gif?cid=ecf05e47pz9a4ania3bphryyxqcvf3jzm5j87bg08o8qu6wf&rid=giphy.gif&ct=g']
  await ctx.send(random.choice(pissoff))  
  
@client.command()
async def waifu(ctx):
  waifu = ['https://media3.giphy.com/media/sMeN0FzG7lsw8/giphy.gif?cid=ecf05e478m1b1bcp0ti6hd2xqqefq9jv0n2tzdu5jzspzkay&rid=giphy.gif&ct=g', 'https://media4.giphy.com/media/LML5ldpTKLPelFtBfY/giphy.gif?cid=ecf05e47jkynm5zvpscrlh47iafp2m25rbd80ubglsf87uz2&rid=giphy.gif&ct=g', 'https://media0.giphy.com/media/10YWqUivkQPeeJWD3u/giphy.gif?cid=ecf05e47brubnww16fff9x8azlzbuukr4lf5pj6rztuimlut&rid=giphy.gif&ct=g', 'https://media0.giphy.com/media/du1u1eYSXp0wo/giphy.gif?cid=ecf05e47wo9un68r4kgy8vxk25k2bytsdkv78xvdibmhyuxq&rid=giphy.gif&ct=g', 'https://media0.giphy.com/media/cxPtMDHG8Ljry/giphy.gif?cid=ecf05e47zntncg3nfwg7hx0lyc2ct9m2mlcxpf0fomyw4rfh&rid=giphy.gif&ct=g', 'https://media3.giphy.com/media/hZfBs4E6tCTc19njbD/giphy.gif?cid=ecf05e47xuk5a7xqrr8mu1qwiandty9jdvkeaq0arkjawp00&rid=giphy.gif&ct=g', 'https://media3.giphy.com/media/5os6xBZJEobuE3Wnmj/giphy.gif?cid=ecf05e47ive8dr3uye3o5vfhriv1iktn5m28tfrtiqcz4dvx&rid=giphy.gif&ct=g', 'https://media4.giphy.com/media/xF2i5FhIo3Igeuzt5t/giphy.gif?cid=ecf05e47x1j3rai599c59tvxm0tssydrafauzslg2iga48hc&rid=giphy.gif&ct=g', 'https://media3.giphy.com/media/gSGNyzkKeKFBS/giphy.gif?cid=ecf05e47pmvjqow3efzmr1owpm7i049kuo9b72xyl31lyv8c&rid=giphy.gif&ct=g', 'https://media1.giphy.com/media/Qcrmc6dbGyLMQ/giphy.gif?cid=ecf05e47l15fd653nxhpz1r5emiabrdk30p8qoxbqtsjix0z&rid=giphy.gif&ct=g']
  await ctx.send(random.choice(waifu))

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

client.run(os.getenv('TOKEN'))
