import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord import Guild, app_commands
import asyncio
import random

intents = discord.Intents.all()

#load .env, needed for bot token securitry, ids and so on
load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='>', self_bot=True, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


#client run, launches the bot
bot.run(TOKEN)