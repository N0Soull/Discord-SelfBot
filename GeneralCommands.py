from discord.ext import commands

class GeneralCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #test command, similar to ping-pong
    @commands.command(name="test", aliases=["t"])
    async def command_test(self, ctx):
        if self.bot.debug:
            print("command_test called.")

        await ctx.reply("Working.")

    #shows help message
    @commands.command(name="help")
    async def command_help(self, ctx):
        if self.bot.debug:
            print("command_help called.")

        await ctx.reply(help_message)

help_message: str = """
Commands format:
``command`` [shortcuts] - Explanation (extra notes)

Available commands:
    Functionality:
        ``test`` [t] - Test if the bot is active
        ``help`` - Shows this message

    Activity:
        ``ON`` [on] - Cleares RPC (Resets status to "sleep" and activity to 'Playing with the shotgun trigger''
        ``invisible`` [off] - Sleep RPC plus custom message
        ``work``[worki] - worki work RPC, just for fun

    Emotes:
        ``emote`` - Automated emote integration without having Discord Nitro

    List of emotes:
        still wokring on that
"""

async def setup(bot):
    await bot.add_cog(GeneralCommands(bot))
