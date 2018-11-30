import discord
from discord.ext import commands
import asyncio

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
	
bot.run('NTE3NzUyNTU3NTQ0OTMxMzMw.DuGyiw.7jpxF_VH3-32vKknQ4Nkzy6DbF4')





















    
     
   
        



  
 
 


  
  
     


    
     

