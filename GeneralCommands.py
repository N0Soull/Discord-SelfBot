from discord.ext import commands

help_message: str = """
Discord selfbot
Commands format:
``command`` [shortcuts] - Explanation (extra notes)

Available commands:
    Functionality:
        ``test`` [t] - Test if the bot is active
        ``help`` - Shows this message

    Activity:
        ``available`` [av] - Clear changed RPC (Resets status to online and activity to 'cyka''
        ``sleep`` - Sleep RPC
        ``school``[work] - School RPC
        ``homework`` [hw] - Homework RPC

    Emotes:
        ``emote`` [e] - Automated emote integration without having Discord Nitro

    List of emotes:
        `troll`, `trolla`, `crackcat`, `zzzcat`, `zzzcatconfused`, `zzzcathappy`, `5head`, `kekwdisco`, `sadangry`, `edits`, `fastsmh`, `catjamfast`, `bruh`, `sus`
"""


class GeneralCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="test", aliases=["t"])
    async def command_test(self, ctx):
        """command_test gets called when the user executes the command '>test' into any channel"""
        if self.bot.debug:
            print("command_test called.")

        await ctx.reply("Working.")

    @commands.command(name="help")
    async def command_help(self, ctx):
        """command_help gets called when the user executes the command '>help' into any channel"""
        if self.bot.debug:
            print("command_help called.")

        await ctx.reply(help_message)


async def setup(bot):
    await bot.add_cog(GeneralCommands(bot))
