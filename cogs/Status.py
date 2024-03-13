import discord
from colorama import Fore as F
from discord.ext import commands
from typing import Optional


class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Status: idle activity: playing
    @commands.command(name="Available", aliases=["on"])
    async def command_available(self, ctx):
        print(f"{F.LIGHTMAGENTA_EX}(*){F.LIGHTWHITE_EX} rpc set to pre-defined one: {F.LIGHTGREEN_EX}available")

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
        print(f"{F.LIGHTMAGENTA_EX}(*){F.LIGHTWHITE_EX} rpc set to pre-defined one: {F.BLUE}invisible")

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
    @commands.command(name="work", aliases=["workiwork"])
    async def command_school(self, ctx):
        print(f"{F.LIGHTMAGENTA_EX}(*){F.LIGHTWHITE_EX} rpc set to pre-defined one: {F.LIGHTRED_EX}work")

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
        print(f"{F.LIGHTMAGENTA_EX}(*){F.LIGHTWHITE_EX} rpc set to pre-defined one: {F.LIGHTMAGENTA_EX}Suffer")

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

    # sets status
    @commands.command(name="status", description="allows you to just change the status")
    async def command_status(self, ctx, status):
        msg = ctx.message

        if status == "online":
            await self.bot.change_presence(status=discord.Status.online)
            await msg.edit(content="```yaml\nChanged status to online.```", delete_after=5)
            print(f"{F.LIGHTMAGENTA_EX}(*){F.LIGHTWHITE_EX} status set to {F.LIGHTGREEN_EX}{status}")
        elif status == "offline":
            await self.bot.change_presence(status=discord.Status.invisible)
            await msg.edit(content="```yaml\nChanged status to offline```", delete_after=5)
            print(f"{F.LIGHTMAGENTA_EX}(*){F.LIGHTWHITE_EX} status set to {F.LIGHTBLACK_EX}{status}")
        elif status == "idle":
            await self.bot.change_presence(status=discord.Status.idle)
            await msg.edit(content="```yaml\nChanged status to idle.```", delete_after=5)
            print(f"{F.LIGHTMAGENTA_EX}(*){F.LIGHTWHITE_EX} status set to {F.LIGHTYELLOW_EX}{status}")
        elif status == "dnd":
            await self.bot.change_presence(status=discord.Status.dnd)
            await msg.edit(content="```yaml\nChanged status to do not disturb.```", delete_after=5)
            print(f"{F.LIGHTMAGENTA_EX}(*){F.LIGHTWHITE_EX} status set to {F.LIGHTRED_EX}{status}")
        elif status == "none":
            await self.bot.change_presence(status=None)
            await msg.edit(content="```yaml\nChanged status to none.```", delete_after=5)
            print(f"{F.LIGHTMAGENTA_EX}(*){F.LIGHTWHITE_EX} status set to {status}")

    # sets custom rpc wiht your own activity
    @commands.command(name="rpc", aliases=["RPC"], description="allowes to set custom rpc")
    async def command_rpc(self, ctx, rpc : str, *, cstm: Optional [str]):
        msg = ctx.message

        if rpc == "listening":
            await self.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening,
                name=cstm,),
            status=self.bot.status)

            await msg.edit(content=f"```yaml\n+ Set your listening rpc to {cstm}```", delete_after=5)
            print(f"{F.LIGHTMAGENTA_EX}(*){F.LIGHTWHITE_EX} RPC set to {F.LIGHTCYAN_EX}{rpc}{F.LIGHTWHITE_EX} with a custom message '{F.LIGHTBLUE_EX}{cstm}{F.LIGHTWHITE_EX}'")
        elif rpc == "watching":
            await self.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name=cstm),
            status=self.bot.status)
        
            await msg.edit(content=f"```yaml\n+ Set your watching rpc to {cstm}```", delete_after=5)
            print(f"{F.LIGHTMAGENTA_EX}(*){F.LIGHTWHITE_EX} RPC set to {F.LIGHTCYAN_EX}{rpc}{F.LIGHTWHITE_EX} with a custom message '{F.LIGHTBLUE_EX}{cstm}{F.LIGHTWHITE_EX}'")
        elif rpc == "playing":
            await self.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.playing,
                name=cstm),
            status=self.bot.status)
            
            await msg.edit(content=f"```yaml\n+ Set your playing rpc to {cstm}```", delete_after=5)
            print(f"{F.LIGHTMAGENTA_EX}(*){F.LIGHTWHITE_EX} RPC set to {F.LIGHTCYAN_EX}{rpc}{F.LIGHTWHITE_EX} with a custom message '{F.LIGHTBLUE_EX}{cstm}{F.LIGHTWHITE_EX}'")
        elif rpc == "stop":
            await ctx.message.delete()
            await self.bot.change_presence(
            activity=None,
            status=self.bot.status)

            await msg.edit(content="```yaml\n Set your rpc to none```", delete_after=5)
            print(f"{F.LIGHTMAGENTA_EX}(*){F.LIGHTWHITE_EX} RPC set to {F.LIGHTCYAN_EX}{rpc}")

async def setup(bot):
    await bot.add_cog(Status(bot))