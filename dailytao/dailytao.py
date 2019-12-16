import json
import random
import discord
from redbot.core import commands, checks
from redbot.core.config import Config


class dailytao(commands.Cog):
    """
    Delivers Tao te Ching to Channel
    """
    @commands.command()
    async def tao(self, ctx):

        tao_text_location = "/home/ec2-user/forge/cogs/darkforge-cogs/dailytao/taoteching.json";
        with open(tao_text_location) as f:
            chapters = json.loads(f.read())
                    
        index = random.randint(0, len(chapters) - 1)
        chapter_obj = chapters[index]
        chapter_num = chapter_obj['chapter']
        chapter_text = chapter_obj['text']
        embed = discord.Embed(color=0x000000, title='Tao te Ching')
        embed.add_field(name=' chapter ', value=chapter_num)
        embed.add_field(name=' —————— ', value=chapter_text)
        embed.set_footer(text='Lao Tzu / Laozi (4th-6th Century BC)')   
                     
        await ctx.send(embed=embed)

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(
            self,
            identifier=112353211,
            force_registration=True,
        )
