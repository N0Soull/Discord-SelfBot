import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

#debug mode BOOL
debug: bool = False

load_dotenv()
token = os.getenv('TOKEN')

#bot intialization
class Bot(commands.Bot):
    def __init__(self, command_prefix, self_bot):
        super().__init__(
            command_prefix=command_prefix,
            self_bot=self_bot
        )

        self.remove_command("help")
        self.initial_extensions = ["Emotes", "Status", "Commands"]
        self.debug = debug

    #extention load message
    async def setup_hook(self):
        for extension in self.initial_extensions:
            await self.load_extension(extension)
            print(f"Loaded extension {extension}")

    #on ready message
    async def on_ready(self):
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


#prefix can be changed to anything you want
client = Bot(command_prefix=">", self_bot=True)
client.run(token)