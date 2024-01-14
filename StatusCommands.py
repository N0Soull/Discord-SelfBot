import discord
from discord.ext import commands


class StatusCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="available", aliases=["av"])
    async def command_available(self, ctx):
        """command_available gets called when the user executes the command '>available' or '>av' into any channel"""
        if self.bot.debug:
            print("command_available called.")

        await self.bot.change_presence(
            status=discord.Status.do_not_disturb,
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="cyka"
            ),
            afk=True
        )

        await ctx.message.delete()

    @commands.command(name="sleep")
    async def command_sleep(self, ctx):
        """command_sleep gets called when the user executes the command '>sleep' into any channel"""
        if self.bot.debug:
            print("command_sleep called.")

        await self.bot.change_presence(
            status=discord.Status.do_not_disturb,
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="Cyka"
            ),
            afk=False
        )

        await ctx.message.delete()

    @commands.command(name="school", aliases=["work"])
    async def command_school(self, ctx):
        """command_school gets called when the user executes the command '>school' or '>work' into any channel"""
        if self.bot.debug:
            print("command_school called.")

        await self.bot.change_presence(
            status=discord.Status.do_not_disturb,
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="Cyka"
            ),
            afk=True
        )

        await ctx.message.delete()

    @commands.command(name="homework", aliases=["hw"])
    async def command_homework(self, ctx, *, is_afk: str = "no"):
        """command_homework gets called when the user executes the command '>homework' or '>hw' into any channel"""
        if self.bot.debug:
            print("command_homework called.")

        if is_afk == "yes":
            is_afk = True
        else:
            is_afk = False

        await self.bot.change_presence(
            status=discord.Status.do_not_disturb,
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="cyka"
            ),
            afk=is_afk
        )

        await ctx.message.delete()


async def setup(bot):
    await bot.add_cog(StatusCommands(bot))
