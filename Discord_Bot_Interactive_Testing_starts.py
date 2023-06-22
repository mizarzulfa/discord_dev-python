import discord
from discord.ext import commands
from auth.privateToken import myToken

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

bot.run(myToken())
