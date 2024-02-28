import json
from discord.ext import commands

class Configurations(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # loading config
    async def load_config(self):
        with open("./cfg/config.json", "r") as config_file:
            config = json.load(config_file)
        return config

    # saves config
    async def save_config(self, config):
        with open("./cfg/config.json", "w") as config_file:
            json.dump(config, config_file, indent=4)

    # sets new prefix (if you dont like the default one)
    @commands.command(name="setprefix", aliases=["setP"])
    async def command_set_prefix(self, ctx, prefix):
        config = await self.load_config()
        config["command_prefix"] = prefix
        await self.save_config(config)
        await ctx.reply(f"Command prefix set to: {prefix}")
        
        if self.bot.debug:
            print(f"CONFIG CHANGE: \nprefix changed to {prefix}")

    # debug mode ON/OFF
    @commands.command(name="debug", aliases=["DB"])
    async def command_debug(self, ctx, mode: bool):
        config = await self.load_config()
        config["debug"] = mode
        await self.save_config(config)
        await ctx.reply(f"Debug mode {'enabled' if mode else 'disabled'}.")

        if self.bot.debug:
            print(f"CONFIG CHANGE: \ndebug switched {mode}")
            
async def setup(bot):
    await bot.add_cog(Configurations(bot))