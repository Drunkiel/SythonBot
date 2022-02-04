import discord
from discord.ext import commands
import requests
import json

# set the apikey and limit
apikey = ""
lmt = 1

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def slap(self, ctx, user: discord.Member):
        if isinstance(user, commands.MissingRequiredArgument):
            await ctx.send('Error: Musisz podać osobę do pobicia')

        # Search
        search_term = "anime slap"

        # get random results using default locale of EN_US
        r = requests.get(
            "https://g.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

        if r.status_code == 200:
            gifs = json.loads(r.content)
            embed = discord.Embed(color=0xccfffe)
            embed.add_field(name="Sython", value=user.mention + " dostał z liścia", inline=False)
            embed.set_image(url=gifs['results'][0]['media'][0]['gif']['url'])

            await ctx.send(embed=embed)
        else:
            gifs = None
            await ctx.send('Error: Nie można wysłać gifa, przekroczono limit prób')

def setup(bot):
    bot.add_cog(MyCog(bot))