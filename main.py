import os
import discord

from discord.ext import commands

bot = commands.Bot(command_prefix='.')

TOKEN = ""

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# . is path folder -> lib/commands/thing_command.py 
# do not add extensions because they are perceived as /
base_path = 'lib.commands.'
bot.load_extension(base_path + "thing_command")
bot.load_extension(base_path + 'slap_command')
bot.load_extension(base_path + 'hug_command')

bot.run(TOKEN)