import os
import discord
import json
import requests

from discord.ext import commands
from dotenv import load_dotenv

# todo fix load env
load_dotenv()

bot = commands.Bot(command_prefix='.')

# set the apikey and limit
apikey = ""
lmt = 1


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


# seperate commands
# New commands
@bot.command(name='slap')
async def slap(ctx, user: discord.Member):
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


@bot.command(name='hug')
async def slap(ctx, user: discord.Member):
    if isinstance(user, commands.MissingRequiredArgument):
        await ctx.send('Error: Musisz podać osobę do przytulenia')

    # Search
    search_term = "anime hug"

    # get random results using default locale of EN_US
    r = requests.get(
        "https://g.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

    if r.status_code == 200:
        gifs = json.loads(r.content)
        embed = discord.Embed(color=0xccfffe)
        embed.add_field(name="Sython", value=user.mention + " został przytulony", inline=False)
        embed.set_image(url=gifs['results'][0]['media'][0]['gif']['url'])

        await ctx.send(embed=embed)
    else:
        gifs = None
        await ctx.send('Error: Nie można wysłać gifa, przekroczono limit prób')


@bot.command(name='thing')
async def send_text(ctx):
    for x in range(6):
        await ctx.send('Julka ma chłopaka')


bot.run("")