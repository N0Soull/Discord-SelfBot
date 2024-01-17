from discord.ext import commands

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #test command, similar to ping-pong
    @commands.command(name="test", aliases=["t"])
    async def command_test(self, ctx):
        if self.bot.debug:
            print("Test_called.")

        await ctx.reply("Working.")

    #shows help message
    @commands.command(name="help")
    async def command_help(self, ctx):
        if self.bot.debug:
            print("command_help called.")

        await ctx.reply(help_message)

    #reload cog modules
    @commands.command(name="reload")
    async def reload_cog(self, ctx, *, cog: str):
        try:
            await self.bot.reload_extension(cog)
            await ctx.send(f"Reloaded extension `{cog}` successfully.")
        except Exception as e:
            await ctx.send(f"Failed to reload extension `{cog}`. {type(e).__name__}: {e}")

    #loads new cog on the go
    @commands.command(name="load")
    async def command_load_cog(self, ctx, *, cog: str):
        try:
            await self.bot.load_extension(cog)
            await ctx.reply(f"Loaded extension `{cog} successfully.")
        except Exception as e:
            await ctx.reply(f"Failed to load extension `{cog}`. {type(e).__name__}: {e}")

#defining custom help message
help_message: str = """
Commands format:
``command`` [shortcuts] - Explanation with extra notes

Available commands:
    Functionality:
        ``test`` [t] - Test if the bot is active (a basic ping pong command)
        ``help`` - Shows this message
        ``reload`` - reloads any cog
        ``load``- loads a new cog module on the go
        ``setuser``[stu] - sets the username in config file
        ``setprefix``[stp] - lets the user define prefix
        ``debug`` [db] - toggles debug mode on and off

    Activity:
        ``ON`` [on] - Sets RPC to your default (can be customized in code)
        ``invisible`` [off] - Sets status to invisible (nothing special)
        ``work``[worki] - worki work RPC, just for fun (Do Not Disturb status)
        ``suffer``[evd] - listening to voices in my head RPC (idle status)

    Emotes:
        ``emote`` [e] - Automated emote integration without having Discord Nitro (works on mobile aswell)
        ``addemote``[addE] - adds a new emote to emotes.json file
        ``removeemote``[rmE] - removes emote entry from emotes.json file

    List of emotes:
        <insert your emote shortcuts here>

        USE THIS SELFBOT AT YOUR OWN RISK, IT IS AGAINST DISCORD'S ToS!
"""

async def setup(bot):
    await bot.add_cog(Commands(bot))