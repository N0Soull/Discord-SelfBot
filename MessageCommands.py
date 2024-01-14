import asyncio
from discord.ext import commands


class MessageCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        """on_message gets called when any message is sent into any channel"""
        if message.author != self.bot.user:
            return

        targets_twitter = ["://twitter.com", "://x.com"]
        for target in targets_twitter:
            if target in message.content:
                new_text = message.content.replace(target, "://vxtwitter.com")
                await asyncio.sleep(4)  # Sleep for a bit to render twitter's embed first.
                await message.edit(content=new_text)
                break

        if "discuss.whatever.social/r/" in message.content:
            new_text = message.content.replace("discuss.whatever.social", "reddit.com")
            await asyncio.sleep(4)  # Sleep for a bit to render reddit's embed first
            await message.edit(content=new_text)

        targets = ["piped.kavin.rocks", "watch.whatever.social", "piped.adminforge.de"]
        for target in targets:
            if target in message.content:
                new_text = message.content.replace(target, "youtube.com")
                await asyncio.sleep(4)  # Sleep for a bit to render target's embed first
                await message.edit(content=new_text)
                break  # Break the loop after editing the message to avoid multiple edits

        await self.bot.process_commands(message)

    @commands.Cog.listener()
    async def on_message_edit(self, _, after):
        """on_message_edit gets called when the local user who is running the bot edits one of his own messages"""
        ctx = await self.bot.get_context(after)
        if not ctx.command:
            await self.bot.process_commands(after)


async def setup(bot):
    await bot.add_cog(MessageCommands(bot))
