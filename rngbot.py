import logging
import discord
from discord.ext import commands

# Bot token
token = "MzY3MDMyMzA2ODU2MjMwOTIz.DL1qsQ.09KzvOqRtkCKGW0SbDWcJstOgrQ"

# Set up bot logs
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = commands.Bot(command_prefix='!rng', description='Renegades discord bot')


# Executed on bot login
@bot.event
async def on_ready():
    print('Logged in as ' + bot.user.name)


# Say command
@bot.command()
async def say(arg):
    """Say: Echoes text right back at ya."""
    await bot.say(arg)


bot.run(token)
