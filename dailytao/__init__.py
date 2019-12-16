from .dailytao import dailytao


def setup(bot):
    cog = dailytao(bot)
    bot.add_cog(cog)