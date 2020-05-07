# ShrekBot

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print ("Ready to go")
    print ("I am running on ", bot.user.name)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("pong")
	
@bot.command(pass_context=True)
async def shreked(ctx):
	#victim_member = discord.utils.get(ctx.message.server.members, name=victim)
	await bot.create_channel(ctx.message.server, "The Shrek Zone", type=discord.ChannelType.voice)

bot.run("NDYwODkwNzc1NTg1MTYxMjE2.DhLV6A.D9-GoCS0LR-xhDEzpniYoKcsZ9A")
