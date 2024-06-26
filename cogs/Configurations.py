import json
from colorama import Fore as F
from discord.ext import commands

# Defining a class for bot Configuration commands
class Configurations(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Loading configuration from file
    async def load_config(self):
        with open("./cfg/config.json", "r") as config_file:
            config = json.load(config_file)
        return config

    # Saving configuration to file
    async def save_config(self, config):
        with open("./cfg/config.json", "w") as config_file:
            json.dump(config, config_file, indent=4)

    ## Command to set a new prefix for bot commands
    @commands.command(name="setprefix", aliases=["setP"])
    async def command_set_prefix(self, ctx, prefix):
        config = await self.load_config()
        config["command_prefix"] = prefix
        await self.save_config(config)
        await ctx.reply(f"Command prefix set to: {prefix}")
        print(f"{F.LIGHTMAGENTA_EX}(*){F.LIGHTWHITE_EX} prefix set to {prefix}")

'''
dont know the usecase but i'll keep it here
    # debug mode ON/OFF
    @commands.command(name="debug", aliases=["DB"])
    async def command_debug(self, ctx, mode: bool):
        config = await self.load_config()
        config["debug"] = mode
        await self.save_config(config)
        await ctx.reply(f"Debug mode {'enabled' if mode else 'disabled'}.")

        if self.bot.debug:
            print(f"CONFIG CHANGE: \ndebug switched {mode}")
'''
# Setup function to add the Configurations cog to the bot
async def setup(bot):
    await bot.add_cog(Configurations(bot))