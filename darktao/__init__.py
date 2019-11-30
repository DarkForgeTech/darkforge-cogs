from .tao import darktao


def setup(bot):
    cog = darktao(bot)
    bot.add_cog(cog)