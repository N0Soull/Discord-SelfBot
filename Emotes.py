import json
from discord.ext import commands
from urllib.parse import urlparse, unquote


# Defining the emote dictionary
'''`emote name`: (`emote id`, `emote format`),'''

# Load emotes from JSON file
def load_emotes():
    try:
        with open('./cfg/emotes.json', 'r') as file:
            data = file.read()
            return json.loads(data) if data else {}
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

# Save emotes to JSON file
def save_emotes(emotes):
    with open('./cfg/emotes.json', 'w') as file:
        json.dump(emotes, file)

class Emotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.emotes = load_emotes()

    # create and insert emote-link
    @commands.command(name="emote", aliases=["e"])
    async def emote(self, ctx, *, emote_name: str):
        if emote_name in self.emotes:
            emote_id, ext = self.emotes[emote_name]
            emote_url = f"https://cdn.discordapp.com/emojis/{emote_id}.{ext}?size=44&quality=lossless"
            await ctx.message.edit(content=emote_url)
        else:
            await ctx.message.edit(content="Invalid emote name.")

    # parse emote
    @commands.command(name="find", aliases=["parseEmote"])
    async def find(self, ctx, *, emote_url: str):
        parsed_url = urlparse(unquote(emote_url))
        emote_id = parsed_url.path.split('/')[-1].split('.')[0]
        file_ext = parsed_url.path.split('/')[-1].split('.')[1]
        reply = f"'': ('{emote_id}', '{file_ext}')"
        await ctx.reply(reply)

    # add emote
    @commands.command(name="addemote", aliases=["addE"])
    async def add_emote(self, ctx, emote_name: str, emote_id: str, ext: str):
        self.emotes[emote_name] = (emote_id, ext)
        save_emotes(self.emotes)
        await ctx.send(f"Emote {emote_name} added successfully.")

    # remove emote
    @commands.command(name="removeemote", aliases=["rmE"])
    async def remove_emote(self, ctx, emote_name: str):
        if emote_name in self.emotes:
            del self.emotes[emote_name]
            save_emotes(self.emotes)
            await ctx.send(f"Emote {emote_name} removed successfully.")
        else:
            await ctx.send("Emote not found.")

async def setup(bot):
    await bot.add_cog(Emotes(bot))