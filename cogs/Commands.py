import os
import sys
from discord.ext import commands
from colorama import Fore

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # test command, measures latence and just tests if the bot is even working
    @commands.command(name="ping", aliases=["test"], description="tests if the bot is working and test latency")
    async def command_test(self, ctx):
        msg = ctx.message
        latency = round(self.bot.latency * 1000)
        await msg.edit(content=f"```yaml\nThe bot's latency is {latency}ms```", delete_after=5)

    # shows help message
    @commands.command(name="help", description="sends help message")
    async def command_help(self, ctx):
        if self.bot.debug:
            print("COMMAND CALLED: \nhelp message called.")

        await ctx.reply(help_message)

    # reload cog modules
    @commands.command(name="reload", description="reloads selected cog module")
    async def reload_cog(self, ctx, *, cog: str):
        try:
            await self.bot.reload_extension(cog)
            await ctx.send(f"Reloaded extension `{cog}` successfully.")
        except Exception as e:
            await ctx.send(f"Failed to reload extension `{cog}`. {type(e).__name__}: {e}")

        if self.bot.debug:
            print(f"COMMAND CALLED: \nCOG {cog} reloaded")

    # loads new cog on the go
    @commands.command(name="load", description="loads new cog module")
    async def command_load_cog(self, ctx, *, cog: str):
        try:
            await self.bot.load_extension(cog)
            await ctx.reply(f"Loaded extension `{cog} successfully.")
        except Exception as e:
            await ctx.reply(f"Failed to load extension `{cog}`. {type(e).__name__}: {e}")
            
        if self.bot.debug:
            print(f"COMMAND CALLED: \nnew COG {cog} loaded")

    @commands.command(name="restart", description="restarts bot.py")
    async def command_restart(self, ctx):
        await ctx.message.delete()
        os.execv(sys.executable, ['python'] + ['./bot.py'])

    @commands.command(name="logout", description="Logs you out of the bot")
    async def command_logout(self, ctx):
        await ctx.message.delete()
        print(
            f"{Fore.GREEN}[+]{Fore.LIGHTWHITE_EX} Logged out of the account {Fore.LIGHTBLUE_EX}{self.bot.user}")
        await self.bot.close()

# custom help message
help_message: str = """
Commands format:
``command`` [shortcuts] - Explanation with extra notes

Available commands:
    Functionality:
        ``test`` [t] - Test if the bot is active (a basic ping pong command)
        ``help`` - Shows this message
        ``reload`` - reloads any cog
        ``load``- loads a new cog module on the go
        ``setprefix`` - lets the user define prefix
        ``debug`` [db] - toggles debug mode on and off
        ``reloadconfig`` [reloadcfg] - reloads the main config module(not working as of right now)

    Activity:
        ``ON`` [on] - Sets RPC to your default (can be customized in code)
        ``invisible`` [off] - Sets status to invisible (nothing special)
        ``work``[worki] - worki work RPC, just for fun (Do Not Disturb status)
        ``suffer``[evd] - listening to voices in my head RPC (idle status)

    Emotes:
        ``emote`` [e] - Automated emote integration without having Discord Nitro (works on mobile aswell)
        ``addemote``[addE] - adds a new emote to emotes.json file, you will need emote name its id and format 
        ``removeemote``[rmE] - removes emote entry from emotes.json file
        ``Find``[findEmote] - allowes you to find emote id/format and create your own shortcut

    List of emotes:
        <insert your emote shortcuts here>

    selfbot`s are against discord`s ToS but if you are seeing this message then you dont care or you know it allready so use this at you`r own risk...
"""

async def setup(bot):
    await bot.add_cog(Commands(bot))