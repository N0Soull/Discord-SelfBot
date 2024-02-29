import asyncio
from colorama import Fore as F
from discord.ext import commands

"""NOTE this module was created by TherioJunior: https://gitlab.com/TherioJunior"""

# this cog is only for the replacement of the embed
class MessageCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # on_message gets called when any message is sent into any channel
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author != self.bot.user:
            return

        # Twitter URLs can have a low embed replacement time becouse of the awesome changes that elon made
        # resulting in not having to wait for the original embed to load anymore.
        # Other sites however have their own embeds which need to load pre-editing, otherwise the edited URL will have the old embed.

        """":original.link": (":replace.link", embed level)"""
        replacements: dict = {
            "://twitter.com": ("://vxtwitter.com", 1),
            "://x.com": ("://vxtwitter.com", 1),
            "piped.kavin.rocks": ("youtube.com", 4),
            "watch.whatever.social": ("youtube.com", 4),
            "piped.adminforge.de": ("youtube.com", 4),
        }
        
        # link-replace loop
        for target, (replacement, sleep_time) in replacements.items():
            if target in message.content:
                new_text: str = message.content.replace(target, replacement)
                await asyncio.sleep(sleep_time)
                await message.edit(content=new_text)
                print(f"{F.LIGHTMAGENTA_EX}(*){F.LIGHTWHITE_EX} link edited, replaced with {replacement}")
                break

    # on_message_edit gets called when the local user edits one of his own messages
    @commands.Cog.listener()
    async def on_message_edit(self, _, after):
        ctx = await self.bot.get_context(after)
        if ctx.command:
            await self.bot.process_commands(after)

async def setup(bot):
    await bot.add_cog(MessageCmd(bot))