import os
import sys
import discord
from discord.ext import commands
from colorama import Fore as F

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # test command, measures latence and just tests if the bot is even working
    @commands.command(name="ping", aliases=["test"], description="tests if the bot is working and test latency")
    async def command_test(self, ctx):
        msg = ctx.message
        latency = round(self.bot.latency * 1000)
        await msg.edit(content=f"```yaml\nThe bot's latency is {latency}ms```", delete_after=5)
        print(f"{F.LIGHTMAGENTA_EX}(*){F.LIGHTWHITE_EX} bots latency is {latency}ms")

    # shows help message
    @commands.command(name="help", description="sends help message")
    async def command_help(self, ctx):
        await ctx.reply(help_message)
        print(f"{F.LIGHTMAGENTA_EX}(*){F.LIGHTWHITE_EX} help message sent")

    # reload cog modules
    @commands.command(name="reload", description="reloads selected cog module")
    async def reload_cog(self, ctx, *, cog: str):
        try:
            await self.bot.reload_extension(cog)
            await ctx.send(f"Reloaded extension `{cog}` successfully.")
            print(f"{F.GREEN}[+]{F.LIGHTWHITE_EX} reloaded {cog}")
        except Exception as e:
            await ctx.send(f"Failed to reload extension `{cog}`. {type(e).__name__}: {e}")
            print(f"{F.RED}[-]{F.LIGHTWHITE_EX} Failed to load {cog}.\n  Error: {F.RED}{e}{F.RESET}")

    # loads new cog on the go
    @commands.command(name="load", description="loads new cog module")
    async def command_load_cog(self, ctx, *, cog: str):
        try:
            await self.bot.load_extension(cog)
            await ctx.reply(f"Loaded extension `{cog} successfully.")
            print(f"{F.GREEN}[+]{F.LIGHTWHITE_EX} Loaded {cog}")
        except Exception as e:
            await ctx.reply(f"Failed to load extension `{cog}`. {type(e).__name__}: {e}")
            print(f"{F.RED}[-]{F.LIGHTWHITE_EX} Failed to load {cog}.\n  Error: {F.RED}{e}{F.RESET}")

    @commands.command(name="restart", description="restarts bot.py")
    async def command_restart(self, ctx):
        await ctx.message.delete()
        print(f"{F.GREEN}[+]{F.LIGHTWHITE_EX} restarting the bot")
        os.execv(sys.executable, ['python'] + ['./bot.py'])

    @commands.command(name="logout", description="Logs you out of the bot")
    async def command_logout(self, ctx):
        await self.bot.change_presence(
            activity=None,
            status=discord.Status.invisible
            )
        await ctx.message.delete()
        print(f"{F.GREEN}[+]{F.LIGHTWHITE_EX} Logged out of the account {F.LIGHTBLUE_EX}{self.bot.user}")
        await self.bot.close()

    #just for fun command
    @commands.command(name="github", description="send my github just for fun")
    async def command_github(self, ctx):
        msg = ctx.message
        await msg.edit(content="https://github.com/N0Soull")
        print(f"{F.LIGHTMAGENTA_EX}(*){F.LIGHTWHITE_EX} github link sent")

# custom help message
help_message: str = """
Commands format:
``command`` [alternative shortcuts] - Explanation with extra notes

Available commands:
    Functionality:
        ``Ping`` [test] - Test if the bot is active (a basic ping pong command)
        ``help`` - Shows this message
        ``reload`` - reloads any cog defined
        ``load``- loads a new cog module on the go
        ``setprefix`` - lets the user define prefix
        ``restart`` - Restarts the entire bot
        ``logout`` - logs the bot out
        ``github`` - sends my github link (just for fun idk why rly)

    Activity:
        ``ON`` [on] - Sets RPC to your default (can be customized in code)
        ``invisible`` [off] - Sets status to invisible (nothing special)
        ``work`` [worki] - Worki work RPC, just for fun (Do Not Disturb status)
        ``suffer`` [evd] - Listening to voices in my head RPC (idle status)
        ``rpc`` - Accepts arguments such as watching, listening etc. and a custom status message to that
        ``status`` - Sets your status without changing the rpc

    Emotes:
        ``emote`` [e] - Automated emote integration without having Discord Nitro (works on mobile as well)
        ``addemote`` [addE] - Adds a new emote to emotes.json file, you will need emote name its id and format
        ``removeemote`` [rmE] - Removes emote entry from emotes.json file
        ``Find`` [findEmote] - Allows you to find emote id/format and create your own shortcut
        ``emotelist`` - Lists all the emote names saved in the emotes.json file

    List of already preloaded emotes:
        ``>e`` hehe, fcku, gtfo, damn, sadt, tfuw, hmm, aware

    Additional features:
        Automatic embed replacement for Twitter/x and automatic link replacement for sites such as piped, whatever social, adminforge, and etc...
        "This idea was taken from TherioJunior"

Self-bots are against Discord's ToS but if you are seeing this message then you don't care or you know it already so use this at your own risk blah blah blah...
"""

async def setup(bot):
    await bot.add_cog(Commands(bot))