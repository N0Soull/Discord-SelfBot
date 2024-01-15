import json
from discord.ext import commands

class Configurations(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # set user command to define name
    @commands.command(name="setuser", aliases=["stu"])
    async def command_set_user(self, ctx, user_name):
        with open("config.json", "r") as config_file:
            config = json.load(config_file)

        config["user"] = user_name

        with open("config.json", "w") as config_file:
            json.dump(config, config_file, indent=4)

        await ctx.reply(f"User set to: {user_name}")

    # setprefix command to define command prefix
    @commands.command(name="setprefix", aliases=["stp"])
    async def command_set_prefix(self, ctx, prefix):
        with open("config.json", "r") as config_file:
            config = json.load(config_file)

        config["command_prefix"] = prefix

        with open("config.json", "w") as config_file:
            json.dump(config, config_file, indent=4)

        await ctx.reply(f"Command prefix set to: {prefix}")

    # debug command to turn debug mode on/off
    @commands.command(name="debug", aliases=["db"])
    async def command_debug(self, ctx, mode: bool):
        with open("config.json", "r") as config_file:
            config = json.load(config_file)

        config["debug"] = mode

        with open("config.json", "w") as config_file:
            json.dump(config, config_file, indent=4)

        await ctx.reply(f"Debug mode {'enabled' if mode else 'disabled'}.")

async def setup(bot):
    await bot.add_cog(Configurations(bot))