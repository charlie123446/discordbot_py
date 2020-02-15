import discord
from discord.ext import commands
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix=jdata['command_prefix'])

@bot.event
async def on_ready():
    print(">> bot is online <<")
    #channel = bot.get_channel(675004439697817634)
    #await channel.send('hello every1')

@bot.event
async def on_member_join(member):
    print(f'{member} join!')
    channel = bot.get_channel(int(jdata['test_channel']))
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    print(f'{member} leave!')
    channel = bot.get_channel(int(jdata['test_channel']))
    await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

bot.run(jdata['token'])