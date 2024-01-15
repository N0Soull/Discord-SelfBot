import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

debug: bool = False

load_dotenv()
token = os.getenv('TOKEN')

class Bot(commands.Bot):
    def __init__(self, command_prefix, self_bot):
        super().__init__(
            command_prefix=command_prefix,
            self_bot=self_bot
        )

        self.remove_command("help")
        self.initial_extensions = ["Emotes", "Status", "Commands"]
        self.debug = debug

    async def setup_hook(self):
        for extension in self.initial_extensions:
            await self.load_extension(extension)
            print(f"Loaded extension {extension}")

    async def on_ready(self):
        """on_ready event"""
        print(f"Logged in as: {self.user}")

        await self.change_presence(
            status=discord.Status.idle,
            activity=discord.Activity(
                type=discord.ActivityType.playing,
                name="with the shotgun trigger"
            ),
            afk=True
        )

        if self.debug:
            print("Successfully changed presence")

    # TODO Fix this command, as of right now, it acts like it doesn't exist
    @commands.command(name="reload")
    async def reload_cog(self, ctx, *, cog: str):
        try:
            await self.bot.reload_extension(cog)
            await ctx.send(f"Reloaded extension `{cog}` successfully.")
        except Exception as e:
            await ctx.send(f"Failed to reload extension `{cog}`. {type(e).__name__}: {e}")


client = Bot(command_prefix=">", self_bot=True)
client.run(token)