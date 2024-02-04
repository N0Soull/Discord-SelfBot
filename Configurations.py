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

    # sets new username and writes it to config
    # idc how to implement it as of rn so its just here rn for nothing
    # TODO think about usefull implementation
    @commands.command(name="setuser", aliases=["setUSR"])
    async def command_set_user(self, ctx, user_name):
        config = await self.load_config()
        config["user"] = user_name
        await self.save_config(config)
        await ctx.reply(f"User set to: {user_name}")

    # sets new prefix (if you dont like the default one)
    @commands.command(name="setprefix", aliases=["setP"])
    async def command_set_prefix(self, ctx, prefix):
        config = await self.load_config()
        config["command_prefix"] = prefix
        await self.save_config(config)
        await ctx.reply(f"Command prefix set to: {prefix}")

    # debug mode ON/OFF
    @commands.command(name="debug", aliases=["DB"])
    async def command_debug(self, ctx, mode: bool):
        config = await self.load_config()
        config["debug"] = mode
        await self.save_config(config)
        await ctx.reply(f"Debug mode {'enabled' if mode else 'disabled'}.")

    # allows to dynamicaly take changes to config
    # TODO fix this command, rn it just reloads the module instead of config 
    @commands.command(name="reloadconfig", aliases=["reloadcfg"])
    async def command_reload_config(self, ctx):
        try:
            await self.bot.unload_extension("cogs.Configurations")
            await self.bot.load_extension("cogs.Configurations")
            await ctx.reply("Config reloaded successfully.")
        except Exception as e:
            await ctx.reply(f"Failed to reload config: {e}")

async def setup(bot):
    await bot.add_cog(Configurations(bot))