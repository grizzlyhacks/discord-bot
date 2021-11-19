import discord
from discord.ext import commands

greetings = [
  "hi %member! :wave:",
  "%member's here, now this party can start"
]

class Listeners(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        channel = message.guild.system_channel
        if channel is not None:
            print(f"{message.created_at} {message.guild}#{message.channel} <{message.author}> {message.content}")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            greeting = random.choice(greetings)
            greeting = greeting.replace("%member", member.name)
            await channel.send(greeting)

def setup(client):
    client.add_cog(Listeners(client))
