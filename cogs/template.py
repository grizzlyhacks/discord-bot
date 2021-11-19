import discord
from discord.ext import commands

# You can change 'Moderation' to anything.
class Template(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Ban command:
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member} has been banned.')
    # Ban error:
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            # You can customize what is said by the bot in the f strings:
            await ctx.send(f'{(ctx.message.author.mention)} User is not defined.')
        elif isinstance(error, commands.errors.MemberNotFound):
            await ctx.send(f'Member not found in this server')
        elif isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'i cannot ban :slight_frown:')
        else:
            await ctx.send(f'Error: {type(error)}: {error}')

def setup(client):
    client.add_cog(Moderation(client))
