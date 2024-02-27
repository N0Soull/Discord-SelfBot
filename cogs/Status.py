import discord
from discord.ext import commands


class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Status: idle activity: playing
    @commands.command(name="Available", aliases=["on"])
    async def command_available(self, ctx):
        if self.bot.debug:
            print("STATUS CHANGE CALLED: \nstatus set to Available")

        await self.bot.change_presence(
            status=discord.Status.idle,
            activity=discord.Activity(
                type=discord.ActivityType.playing,
                name="with N0Soul's sanity"
            ),
            afk=False
        )

        if ctx.message:
            await ctx.message.delete()

    # Status: invisible Activity: watching (is not shown)
    @commands.command(name="invisible", aliases=["off"])
    async def command_sleep(self, ctx):
        if self.bot.debug:
            print("STATUS CHANGE CALLED: \nstatus set to Invisible")

        await self.bot.change_presence(
            status=discord.Status.invisible,
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="some bullshit"
            ),
            afk=False
        )

        if ctx.message:
            await ctx.message.delete()

    # status dnd activity: watching
    @commands.command(name="Work", aliases=["worki"])
    async def command_school(self, ctx):
        if self.bot.debug:
            print("STATUS CHANGE CALLED: \nstatus set to Work")

        await self.bot.change_presence(
            status=discord.Status.do_not_disturb,
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="N0Soul go insane"
            ),
            afk=False
        )
        
        if ctx.message:
            await ctx.message.delete()

    # status: idle activity: listening
    @commands.command(name="suffer", aliases=["evd"])
    async def command_suffering(self, ctx):
        if self.bot.debug:
            print("STATUS CHANGE CALLED: \nstatus set to Suffer")

        await self.bot.change_presence(
            status=discord.Status.idle,
            activity=discord.Activity(
                type=discord.ActivityType.listening,
                name="voices in my head"
            ),
            afk=False
        )

        if ctx.message:
            await ctx.message.delete()

async def setup(bot):
    await bot.add_cog(Status(bot))