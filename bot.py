import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='flower_chen_')

@bot.event
async def on_ready():
    print(">> bot is online <<")
    #channel = bot.get_channel(675004439697817634)
    #await channel.send('hello every1')

@bot.event
async def on_member_join(member):
    print(f'{member} join!')
    channel = bot.get_channel(675004439697817634)
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    print(f'{member} leave!')
    channel = bot.get_channel(675004439697817634)
    await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')


bot.run('Njc4MjExNzU0Mzk1Njk3MTc1.XkgQkg.F3nTjRIm_l2Y5RO2AJg8tt22fGs')