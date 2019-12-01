import random
import json
import discord
from redbot.core import commands, checks
from redbot.core.config import Config

tao_text_location = "taoTeChing.json";
with open(tao_text_location) as f:
    chapters = json.loads(f.read()

class darktao(commands.Cog):
    """
    Deliver Tao-te-Ching chapters to discord.
    """

    @commands.command()
    async def tao(self, ctx):
        random_chapter = random.randint(0, len(chapters) - 1)
        print_chapter(chapters, random_chapter)

    async def print_chapter(chapters, index):
        chapter_obj = chapters[index]
        chapter_num = chapter_obj['chapter']
        chapter_text = chapter_obj['text']

        await ctx.maybe_send_embed(chapter_text)

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(
            self,
            identifier=123456789,
            force_registration=True,
        )
