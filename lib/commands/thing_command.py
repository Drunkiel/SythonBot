import discord
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def thing(self, ctx):
        for x in range(6):
            await ctx.send('Julka ma chłopaka')

def setup(bot):
    bot.add_cog(MyCog(bot))