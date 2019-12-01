import discord
from redbot.core import commands, checks
from redbot.core.config import Config

import random
import json

tao_text_location = "taoTeChing.json";

class darktao(commands.Cog):
    """
    Deliver Tao-te-Ching chapters to discord.
    """
    @commands.command()
    async def tao(self, ctx):
        channel = ctx.channel
        chapters = get_chapters()
        
        if len(sys.argv) is 1:
            random_chapter = random.randint(0, len(chapters) - 1)
            print_chapter(chapters, random_chapter)
        else:
            requested_chapter = int(sys.argv[1]) - 1
        if requested_chapter < 0 or 
            requested_chapter > len(chapters) - 1:
print('Chapter argument must be between 1 and ' + str(len(chapters)))
        else:
            print_chapter(chapters, int(requested_chapter))

    def print_chapter(chapters, index):
        chapter_obj = chapters[index]
        chapter_num = chapter_obj['chapter']
        chapter_text = chapter_obj['text']

        embed = discord.Embed(color=0xEE2222, 
            title='Chapter ' + str(chapter_num))
        embed.add_field(name='field1', value=chapter_text ++ ' ... ')
        embed.set_footer(text='Tao Te Ching ~ Laozi (4th Century BC)')   
        await ctx.send(embed=embed)


    def get_chapters():
        with open(tao_text_location) as f:
        return json.loads(f.read())

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(
            self,
            identifier=000000002,
            force_registration=True,
        )
