import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

import asyncio
import platform
import colorsys
import random
import os 
import time





bot=commands.Bot(command_prefix='f!')

@bot.event
async def on_ready():
	print('The bot is ready!')
	print(bot.user.name)
	print(bot.user.id)
	
@bot.command()
async def info():
	await bot.say('Tohoto bota udělal Majitel MegaCraftu/Syn#1308')
	
@bot.command()
async def hosting():
	await bot.say('****Tento Command Se Dodělává!****')
	
@bot.command()
async def request():
	await bot.say('****__Děkujeme za Request!__****')
	

bot.run(os.getenv("BOT_TOKEN"))




















    
     
   
        



  
 
 


  
  
     


    
     

