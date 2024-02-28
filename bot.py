import discord
import os
import fade
import json
from discord.ext import commands
from dotenv import load_dotenv
from colorama import Fore as F

# please note that this damn god forbidden load .env function can only work with properly set up libraries
# if you try to do it otherwise and not like it says in README then it´s your fault and you can fuck with that on your own
# note aswell that i am not planning to fix it becouse it´s your own fault if you dont set up you´r enviroment right
os.environ.clear()
load_dotenv()
token = os.getenv('TOKEN')

# Default configuration
default_config: dict = {
    "debug": False,
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
        self.cogs_folder = "cogs"
        self.debug = debug
        self.banner()


    # extension load message
    async def setup_hook(self):
        cog_files = [f[:-3] for f in os.listdir(self.cogs_folder) if f.endswith(".py")]

        for cog_file in cog_files:
            cog_path = f"{self.cogs_folder}.{cog_file}"
            try:
                await self.load_extension(cog_path)
                print(f"{F.GREEN}[+]{F.LIGHTWHITE_EX} Loaded {cog_file}")

            except Exception as e:
                print(f"{F.RED}[-]{F.LIGHTWHITE_EX} Failed to load {cog_file}.\n  Error: {F.RED}{e}{F.RESET}")
                exit()

    def banner(self):
     """Print a fancy banner."""
    print(fade.purpleblue("""
   _____             ____                   ____        __ 
  / ___/____  __  __/ / /__  __________    / __ )____  / /_
  \__ \/ __ \/ / / / / / _ \/ ___/ ___/   / __  / __ \/ __/
 ___/ / /_/ / /_/ / / /  __(__  |__  )   / /_/ / /_/ / /_  
/____/\____/\__,_/_/_/\___/____/____/   /_____/\____/\__/  
                              
           """))
            
    # on ready message
    async def on_ready(self):
        if self.debug:
            print(f"the current token is: {token}")

        # sets standart presense (status: idle activity: listenting)
        await self.change_presence(
            status=discord.Status.idle,
            activity=discord.Activity(
                type=discord.ActivityType.listening, #activity types: playing, watching, streaming, listening, custom, competing
                name="voices in my head"
            ),
            afk=True # AFK mode: ON/OFF for discord to better catch and force the notifications
        )

        if self.debug:
            print("PRESENSE CHANGED: \nDefeault presense")

# prefix can be changed to anything you want
client = Bot(command_prefix=cfg_prefix, self_bot=True)
client.run(token)