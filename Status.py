import discord
from discord.ext import commands


class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #standart status and RPC
    @commands.command(name="Available", aliases=["on"])
    async def command_available(self, ctx):
        if self.bot.debug:
            print("command_available called.")

        await self.bot.change_presence(
            status=discord.Status.idle,
            activity=discord.Activity(
                type=discord.ActivityType.playing,
                name="with the shotgun trigger"
            ),
            afk=False
        )

        if ctx.message:
            await ctx.message.delete()

        if self.debug:
            print("Successfully changed presence")

    #sets status to invisible plus custom RPC
    @commands.command(name="invisible", aliases=["off"])
    async def command_sleep(self, ctx):
        if self.bot.debug:
            print("command_sleep called.")

        await self.bot.change_presence(
            status=discord.Status.invisible,
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="marks mom"
            ),
            afk=False
        )

        if ctx.message:
            await ctx.message.delete()

        if self.debug:
            print("Successfully changed presence")

    #sets status to Do not Discturb plus custom RPC
    @commands.command(name="Work", aliases=["worki"])
    async def command_school(self, ctx):
        if self.bot.debug:
            print("command_school called.")

        await self.bot.change_presence(
            status=discord.Status.do_not_disturb,
            activity=discord.Activity(
                type=discord.ActivityType.playing,
                name="with my sanity"
            ),
            afk=False
        )
        
        if ctx.message:
            await ctx.message.delete()
            
        if self.debug:
            print("Successfully changed presence")

async def setup(bot):
    await bot.add_cog(Status(bot))