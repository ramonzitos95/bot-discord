import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents_message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)
my_secret = os.environ['DISCORD_TOKEN']


@bot.command()
async def inverse(ctx, message):
  await ctx.send(message[::-1])


bot.run(my_secret)
