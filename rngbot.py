"""
Renegades Discord Bot

author: John Connor
date: October 2017
"""

import discord
import logging
from discord.ext import commands
import helpers
import rngbot_config

"""
This bot requires Manage Server, Manage Message permissions
"""

# Read config values from file
config_file_name = 'botconfig.json'
config_values = rngbot_config.read_config_file(config_file_name)

# Bot token
token = config_values.token

# Set up bot logs
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# bot init
bot = commands.Bot(command_prefix=config_values.command_prefix, description='Renegades discord bot')


@bot.event
async def on_ready():
    """
    Event executed on bot login to discord
    """
    print('Logged in as ' + bot.user.name)


@bot.event
async def on_resumed():
    """
    Event executed if the bot loses connection and is able to reconnect
    """
    print('Session resumed')


@bot.event
async def on_member_join(member):
    """
    New member join event
    :param member: A Member object representing the user that joined.
    """
    # Find the general channel object
    general = helpers.get_channel(config_values.general_channel_name, member.server)
    # send join message to general
    join_msg = member.mention + config_values.join_msg
    await bot.send_message(general, join_msg)


@bot.event
async def on_member_remove(member):
    """
    Member leaves server event
    :param member: A Member object representing the user that left.
    """
    # Find the general channel object
    general = helpers.get_channel(config_values.general_channel_name, member.server)
    # send leave message to general
    leave_msg = member.name + config_values.leave_msg
    await bot.send_message(general, leave_msg)


# @bot.event
# async def on_message(message):
#     """
#     Message sent event. This is fired for every message sent in this server
#     :param message: A Message object containing the message info.
#     """
#     pass  # do nothing


@bot.command()
async def say(arg):
    """Say: Echoes text back. Text with spaces must be surrounded by quotes.
    :param arg: The text to repeat back.
    """
    await bot.say(arg)


@bot.command(pass_context=True)
async def clear(context, num_messages: int):
    """
    Clear: Deletes the last x messages.
    :param context: Bot context
    :param num_messages: The number of messages to delete.
    :return: Nothing
    """
    if num_messages > 10:
        await bot.say('Limit is 10 messages.')
        return
    if num_messages is None or num_messages <= 0:
        await bot.say('Tell me how many messages to clear.')
        return

    # Check user has proper permissions here
    if not context.message.author.server_permissions.manage_messages:
        await bot.say('You don''t have permission to do this.')
        return

    try:
        await bot.purge_from(context.message.channel, limit=num_messages)
    except discord.Forbidden:
        await bot.say('You don''t have permission to do this.')
        return
    except discord.HTTPException:
        await bot.say('Something went wrong.')
        return


# How to change game:
# await bot.change_presence(game=discord.Game(name='my game'))

# Start the bot
bot.run(token)
