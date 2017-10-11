import discord


def get_channel(name, server):
    """
    Get a discord channel handle.
    :param name: The name of the channel. Case does not matter.
    :param server: The discord server object
    :return: The channel object with the given name in the given server.
    """
    return discord.utils.find(lambda c: c.name.upper() == name.upper(), server.channels)

