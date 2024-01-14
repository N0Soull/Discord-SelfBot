from discord.ext import commands
from urllib.parse import urlparse, unquote


# Defining the emote dictionary
emotes = {
    'troll': ('781985209850789929', 'webp'),
    'trolla': ('838034298056474624', 'gif'),
    'crackcat': ('869556399116517447', 'webp'),
    'zzzcat': ('713860445307666504', 'gif'),
    'zzzcatconfused': ('808141260803407912', 'webp'),
    'zzzcathappy': ('800172683131617302', 'webp'),
    '5head': ('717371749607407758', 'webp'),
    'kekwdisco': ('772987436191318046', 'gif'),
    'sadangry': ('847566432140394567', 'webp'),
    'edits': ('843949099539234837', 'webp'),
    'fastsmh': ('723211652459266089', 'gif'),
    'catjamfast': ('843949652314816533', 'gif'),
    'bruh': ('850795625884680202', 'webp'),
    'sus': ('1084962295500775434', 'webp')
}

class EmoteCommands(commands.Cog):
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
    await bot.add_cog(EmoteCommands(bot))
