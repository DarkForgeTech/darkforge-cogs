from .gotmix import gotmix
from redbot.core import data_manager
from shutil import rmtree


def setup(bot):
    cog = gotmix(bot)
    bot.add_cog(cog)
