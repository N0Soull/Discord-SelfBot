import asyncio
from discord.ext import commands


class MessageCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        """on_message gets called when any message is sent into any channel"""
        if message.author != self.bot.user:
            return

        # Twitter URLs can have a low embed replacement time, because elon's changes broke twitter.com/x.com embeds on Discord 
        # resulting in us not having to wait for the original embed to load anymore.
        # Other sites have their own embeds which need to load pre-editing, otherwise the edited URL will have the old embed.
        replacements: dict = {
            "://twitter.com": ("://vxtwitter.com", 1),
            "://x.com": ("://vxtwitter.com", 1),
            "discuss.whatever.social/r/": ("reddit.com/r/", 4),
            "piped.kavin.rocks": ("youtube.com", 4),
            "watch.whatever.social": ("youtube.com", 4),
            "piped.adminforge.de": ("youtube.com", 4)
        }

        for target, (replacement, sleep_time) in replacements.items():
            if target in message.content:
                new_text: str = message.content.replace(target, replacement)
                await asyncio.sleep(sleep_time)
                await message.edit(content=new_text)
                break

    @commands.Cog.listener()
    async def on_message_edit(self, _, after):
        """on_message_edit gets called when the local user who is running the bot edits one of his own messages"""
        ctx = await self.bot.get_context(after)
        if ctx.command:
            await self.bot.process_commands(after)


async def setup(bot):
    await bot.add_cog(MessageCmd(bot))