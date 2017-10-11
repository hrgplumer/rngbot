import discord
import logging
from discord.ext import commands

# Bot token
token = "MzY3MDMyMzA2ODU2MjMwOTIz.DL1qsQ.09KzvOqRtkCKGW0SbDWcJstOgrQ"

# Set up bot logs
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = commands.Bot(command_prefix='!', description='Renegades discord bot')


# Executed on bot login
@bot.event
async def on_ready():
    print('Logged in as ' + bot.user.name)


@bot.event
async def on_resumed():
    print('Session resumed')


@bot.event
async def on_member_join(member):
    # get general channel
    general = discord.utils.find(lambda c: c.name.upper() == 'GENERAL', member.server.channels)
    # send join message
    join_msg = member.mention + ' has joined this server.'
    await bot.send_message(general, join_msg)


@bot.event
async def on_member_remove(member):
    pass


@bot.event
async def on_message(message):
    pass


# Say command
@bot.command()
async def say(arg):
    """Say: Echoes text right back at ya."""
    await bot.say(arg)


# How to change game:
# await client.change_presence(game=discord.Game(name='my game'))
bot.run(token)
