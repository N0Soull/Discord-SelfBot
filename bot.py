import discord
import os
import json
from discord.ext import commands
from dotenv import load_dotenv

# TODO think of a way to implement a logout command (as of right now it only works in a main module but act's like it doesnt exsist)

#please note that this damn god forbiden load .env function can only work with properly set up library´s
#if you try to do it otherwise and not like it says in README then it´s your fault and you can fuck with that on your own
#note aswell that i am not planning to fix it becouse it´s your own fault if you dont set up you´r enviroment right
load_dotenv()
token = os.getenv('TOKEN')

# Default configuration
default_config: dict = {
    "debug": False,
    "user": "Default User",
    "command_prefix": ">"
}

# Primary configuration file path
primary_config_file_path: str = "./cfg/config.json"

# Load the default configuration
config: dict = default_config

# Try to load the user-defined configuration
if os.path.exists(primary_config_file_path):
    with open(primary_config_file_path, "r") as config_file:
        user_config = json.load(config_file)
        config.update(user_config)
else:
    print(f"'{primary_config_file_path}' is not found. Using default configuration.")

# Extract configuration values
debug: bool = config.get("debug")
cfg_user: str = config.get("user")
cfg_prefix: str = config.get("command_prefix")


# bot intialization
class Bot(commands.Bot):
    def __init__(self, command_prefix, self_bot):
        super().__init__(
            command_prefix=command_prefix,
            self_bot=self_bot
        )
        # loads cog modules
        self.remove_command("help")
        self.initial_extensions = ["Emotes", "Status", "Commands", "Configurations", "MessageCmd"]
        self.debug = debug

        if cfg_user == "User":
            self.cfg_user = self.user
        else:
            self.cfg_user = cfg_user

    # extention load message
    async def setup_hook(self):
        for extension in self.initial_extensions:
            await self.load_extension(extension)
            print(f"Loaded extension {extension}")

    # on ready message
    async def on_ready(self):
        print(f"Logged in as: {self.user}")

        await self.change_presence(
            status=discord.Status.idle,
            activity=discord.Activity(
                type=discord.ActivityType.listening, #activity types: playing, watching, streaming, listening, custom, competing
                name="voices in my head"
            ),
            afk=True # AFK mode: ON/OFF better for discord to catch and force the notifications
        )

        if self.debug:
            print("Successfully changed presence")

# prefix can be changed to anything you want
client = Bot(command_prefix=cfg_prefix, self_bot=True)
client.run(token)