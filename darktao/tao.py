import random
import json
import discord
from redbot.core import commands, checks
from redbot.core.config import Config

tao_text_location = "taoTeChing.json";

class darktao(commands.Cog):
    """
    Deliver Tao-te-Ching chapters to discord.
    """
    @commands.command()
    async def tao(self, ctx):
        chapters = get_chapters()
        random_chapter = random.randint(0, len(chapters) - 1)
        print_chapter(chapters, random_chapter)

    def print_chapter(chapters, index):
        chapter_obj = chapters[index]
        chapter_num = chapter_obj['chapter']
        chapter_text = chapter_obj['text']

        await ctx.maybe_send_embed(chapter_text)

    def get_chapters():
        with open(tao_text_location) as f:
        	return json.loads(f.read())

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(
            self,
            identifier=000000001,
            force_registration=True,
        )
