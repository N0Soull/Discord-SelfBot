import json
from discord.ext import commands
from colorama import Fore as F
from urllib.parse import urlparse, unquote


# Defining the emote dictionary
'''`emote name`: (`emote id`, `emote format`),'''
# this was moved to an external file emotes.json

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
            emote_url = f"https://cdn.discordapp.com/emojis/{emote_id}.{ext}?size=44&quality=lossless" # deconstructed emote link for the replacement
            await ctx.message.edit(content=emote_url)
            print(f"{F.LIGHTMAGENTA_EX}(*){F.LIGHTWHITE_EX} emote {emote_name} sent")
        else:
            await ctx.message.delete()
            print(f"{F.RED}[-]{F.LIGHTWHITE_EX} Invalid Emote name")


    # parse emote
    @commands.command(name="Find", aliases=["ParseEmote"])
    async def find(self, ctx, *, emote_url: str):

        parsed_url = urlparse(unquote(emote_url))
        emote_id = parsed_url.path.split('/')[-1].split('.')[0]
        file_ext = parsed_url.path.split('/')[-1].split('.')[1]
        reply = f"'': ('{emote_id}', '{file_ext}')"

        await ctx.reply(reply)

        print(f"{F.LIGHTMAGENTA_EX}(*){F.LIGHTWHITE_EX} new emote found")

    # add emote
    @commands.command(name="AddEmote", aliases=["addE"])
    async def add_emote(self, ctx, emote_name: str, emote_id: str, ext: str):
        self.emotes[emote_name] = (emote_id, ext)

        save_emotes(self.emotes)
        await ctx.send(f"Emote {emote_name} added successfully.")

        print(f"{F.LIGHTMAGENTA_EX}(*){F.LIGHTWHITE_EX} emote {emote_name} added")

    # remove emote
    @commands.command(name="RemoveEmote", aliases=["rmE"])
    async def remove_emote(self, ctx, emote_name: str):
        if emote_name in self.emotes:
            del self.emotes[emote_name]
            save_emotes(self.emotes)
            await ctx.send(f"Emote {emote_name} removed successfully.")
            print(f"{F.LIGHTMAGENTA_EX}(*){F.LIGHTWHITE_EX} emote {emote_name} removed")
        else:
            await ctx.send("Emote not found.")
            print(f"{F.RED}[-]{F.LIGHTWHITE_EX} Failed to delete {emote_name}.")

    @commands.command(name='emotelist', description="sends a list with all emote names which are saven in emotes.json file")
    async def list_emotes(self, ctx):
        with open('./cfg/emotes.json', 'r') as file:
            emotes_data = json.load(file)

        emote_names = list(emotes_data.keys())
        # native discord emoji link
        base_link = "https://cdn.discordapp.com/emojis/"
        full_links = []

        # parses the emotes saved in file and creates a link with parsed data, also inserts the values into new formated list
        for emote_name in emote_names:
            if emote_name in self.emotes:
                emote_id, ext = self.emotes[emote_name]
                emote_url = f"{base_link}{emote_id}.{ext}?size=44&quality=lossless"
                formatted_line = f"<{emote_url}> {''.join(c for c in emote_name if c != ':')}:{ext}"
                full_links.append(formatted_line)

        # Concatenate the lines with '\n' and add prefix and suffix to preserve monospace font
        joined_lines = '\n'.join(full_links)
        output = f"**Emotes:**\n``{joined_lines}``"

        await ctx.message.edit(output)
        print(f"{F.LIGHTMAGENTA_EX}(*){F.LIGHTWHITE_EX} emote list command used")

async def setup(bot):
    await bot.add_cog(Emotes(bot))