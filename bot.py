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
bot.remove_command('help')

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


@bot.command()
async def help ():
	await bot.say("""f!help
     Zobrazí tuto zprávu

f!info
     Zobrazí info o tvůrci bota

f!request
     Pošle žádost o vylepšení na support server""")
	
@bot.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     

async def kick(ctx,user:discord.Member):

    if user.server_permissions.kick_members:
        await bot.say('**Na toto nemáš práva!**')
        return
    
    try:
        await bot.kick(user)
        await bot.say(user.name+' byl kicknut.')
        await bot.delete_message(ctx.message)

    except discord.Forbidden:
        await bot.say('Permission denied.')
        return
   
    

@bot.command(pass_context=True)  
@commands.has_permissions(ban_members=True) 

async def ban(ctx,user:discord.Member):

    if user.server_permissions.ban_members:
        await bot.say('**Nemáš Právo na ban**')
        return

    try:
        await bot.ban(user)
        await bot.say(user.name+' byl Zabanován.')

    except discord.Forbidden:

        await bot.say('Permission denied.')
        return
    except discord.HTTPException:
        await bot.say('Ban nebyl Úspěšný.')
        return		 

  

    


@bot.command(pass_context=True)
async def ping(ctx):
    t = await bot.say('Pong!')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
    await bot.edit_message(t, new_content=':ping_pong: Ping: {}ms'.format(int(ms)))
      


@bot.command(pass_context = True)
async def warn(ctx, *, member : discord.Member = None):
    if not ctx.message.author.server_permissions.administrator:
        return
 
    if not member:
        return await bot.say(ctx.message.author.mention +  " Označ Uživatele!")
    try:
        await bot.warn(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            return await bot.say("Dostal jsi Warn!")
 
    embed = discord.Embed(description = "%s Dostal jsi warn!"%member.name, color = 0xF00000)
    return await bot.say(embed = embed)






  



	

















    
     
   
        



  
 
 


  
  
     


    
     

bot.run(os.getenv("BOT_TOKEN"))
