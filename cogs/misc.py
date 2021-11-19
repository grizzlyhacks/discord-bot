import discord
from discord.ext import commands

# You can change 'Misc' to anything.
class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['latency'])
    async def ping(self, ctx):
        await ctx.send(f'**Pong! ``{round(self.client.latency * 1000)}ms``**')

    @commands.command()
    async def say(self, ctx, *, message: str):
        """make the bot say something"""
        try:
            await ctx.message.delete()
        except Exception as e:
            print(e)
            pass
        await ctx.send(message)

    @commands.command()
    async def status(self, ctx, activity, *, status):
        """set the bot's status. the first argument must be one of:
           "playing", "streaming", "listening", or "watching"
        """
        activity = activity.lower()
        if activity == "playing":
            # Setting `Playing ` status
            await self.client.change_presence(activity=discord.Game(name=status))
        elif activity == "streaming":
            # Setting `Streaming ` status
            await self.client.change_presence(activity=discord.Streaming(
              name=status, url="https://github.com/grizzlyhacks/discord.py-cogs")
            )
        elif activity == "listening":
            # Setting `Listening ` status
            await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=status))
        elif activity == "watching":
            # Setting `Watching ` status
            await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
        else:
            await ctx.send("""
            usage: `status <activity> <status>`
            activity must be one of: `playing`, `streaming`, `listening`, or `watching`
            """)


def setup(client):
    client.add_cog(Misc(client))
# Remember based on which name you assigned your class for,
# It should be used at the end of the setup function right.
# eg:- client.add_cog(x(client)), client.add_cog(y(client)), client.add_cog(z(client))
