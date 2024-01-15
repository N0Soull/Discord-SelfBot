from discord.ext import commands
from urllib.parse import urlparse, unquote


# Defining the emote dictionary
emotes = {
    'nicedick': ('877571237713436692', 'webp'),
}


# TODO url-parser is done, only emotes are fucked
class Emotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="emote", aliases=["e"])
    async def emote(self, ctx, *, emote_name: str):
        if emote_name in emotes:
            emote_id, ext = emotes[emote_name]
            emote_url = f"https://cdn.discordapp.com/emojis/{emote_id}.{ext}?size=44&quality=lossless"
            await ctx.message.edit(content=emote_url)
        else:
            await ctx.message.edit(content="Invalid emote name.")

    @commands.command(name="find")
    async def find(self, ctx, *, emote_url: str):
        parsed_url = urlparse(unquote(emote_url))
        emote_id = parsed_url.path.split('/')[-1].split('.')[0]
        file_ext = parsed_url.path.split('/')[-1].split('.')[1]
        reply = f"'': ('{emote_id}', '{file_ext}')"
        await ctx.reply(reply)


async def setup(bot):
    await bot.add_cog(Emotes(bot))
