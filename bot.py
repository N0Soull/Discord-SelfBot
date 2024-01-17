import discord
import os
import json
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')

# Default configuration values
default_config: dict = {
    "debug": False,
    "user": "N0Soul",
    "command_prefix": ">"
}

# Function to load configuration from a specified file path
def load_config(file_path: str) -> dict:
    if os.path.exists(file_path):
        with open(file_path, "r") as config_file:
            return json.load(config_file)
    else:
        print(f"'{file_path}' is not found. Using default configuration.")
        return default_config

# Primary configuration file path
primary_config_file_path: str = "./cfg/config.json"

# Loading the configuration
config: dict = load_config(primary_config_file_path)

# Extracting configuration values
debug: bool = config.get("debug", default_config["debug"])
cfg_user: str = config.get("user", default_config["user"])
cfg_prefix: str = config.get("command_prefix", default_config["command_prefix"])


#bot intialization
class Bot(commands.Bot):
    def __init__(self, command_prefix, self_bot):
        super().__init__(
            command_prefix=command_prefix,
            self_bot=self_bot
        )

        self.remove_command("help")
        self.initial_extensions = ["Emotes", "Status", "Commands", "Configurations"]
        self.debug = debug

        if cfg_user == "User":
            self.cfg_user = self.user
        else:
            self.cfg_user = cfg_user

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
client = Bot(command_prefix=cfg_prefix, self_bot=True)
client.run(token)