import discord
from discord.ext import commands
from settings_loader import prefix, token

client = commands.Bot(command_prefix = prefix)

# 'cogs' is the folder name
# 'fun', 'mod', and 'misc' are the file names
cogs = ['cogs.fun', 'cogs.mod', 'cogs.misc']

@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')

    for cog in cogs: # Looks for the cogs,
        client.load_extension(cog) # Loads the cogs.
    return

client.run(token)
