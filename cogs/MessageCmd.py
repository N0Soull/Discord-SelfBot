import asyncio
import json
from colorama import Fore as F
from discord.ext import commands

"""NOTE this module was created by TherioJunior: https://gitlab.com/TherioJunior
        and just slightly modifed by yours truly"""

# this cog is only for the replacement of the embed
class MessageCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.load_replacements()

    def load_replacements(self):
        try:
            with open('./cfg/linkRules.json', 'r') as file:
                self.replacements = json.load(file)
        except FileNotFoundError:
            self.replacements = {}

    # on_message gets called when any message is sent into any channel
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author != self.bot.user:
            return

        # Twitter URLs can have a low embed replacement time because of the awesome changes that Elon made
        # resulting in not having to wait for the original embed to load anymore.
        # Other sites, however, have their own embeds which need to load pre-editing, otherwise, the edited URL will have the old embed.

        # link-replace loop
        for target, (replacement, sleep_time) in self.replacements.items():
            if target in message.content:
                new_text: str = message.content.replace(target, replacement)
                await asyncio.sleep(sleep_time)
                await message.edit(content=new_text)
                print(f"{F.LIGHTMAGENTA_EX}(*){F.LIGHTWHITE_EX} link edited, {target} replaced with {replacement}")
                break

    # on_message_edit gets called when the local user edits one of his own messages
    @commands.Cog.listener()
    async def on_message_edit(self, _, after):
        ctx = await self.bot.get_context(after)
        if ctx.command:
            await self.bot.process_commands(after)

async def setup(bot):
    await bot.add_cog(MessageCmd(bot))
