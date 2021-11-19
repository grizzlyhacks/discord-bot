import os
import settings
import discord
from discord.ext import commands

TOKEN = os.environ.get("BOT_TOKEN") or settings.token
PREFIX = os.environ.get("BOT_PREFIX") or settings.prefix

client = commands.Bot(command_prefix = PREFIX)
# client.remove_command("help")

# 'cogs' is the folder name
# 'fun', 'mod', and 'misc' are the file names
cogs = ['cogs.fun', 'cogs.mod', 'cogs.misc', 'cogs.events']

@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')

    for cog in cogs: # Looks for the cogs,
        client.load_extension(cog) # Loads the cogs.
    return

client.run(TOKEN)
