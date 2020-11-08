# pip install discord.py

import discord
from discord.ext import commands
from discord.ext import tasks

from datetime import datetime

TOKEN = ""

# without this bot cant get all info about users
intents = discord.Intents().all()
bot = commands.Bot(command_prefix='.', help_command=None, description="This is a Helper Bot", intents=intents)


# channels ids
BOT_TEXT_CHANNEL_ID = 00000


# command examples

@bot.command()
async def help(context):
    await context.send("Custom help command")

@bot.command()
async def hello(ctx):
    await ctx.send('hello! {0}'.format(ctx.author))

@bot.command()
async def echo(ctx):
    await ctx.send(ctx.message)


@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Lorem Ipsum asdasd", timestamp=datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")

    await ctx.send(embed=embed)



@bot.command()
async def get_user_by_info(ctx, user):

    nicks = {}
    names = {}
    discriminators = {}
    for index, member in enumerate(ctx.guild.members):
        nicks.update({member.nick:index})
        names.update({member.name:index})
        discriminators.update({member.discriminator:index})

    selected_user = None
    if(user in nicks):
        print(ctx.guild.members[nicks[user]])
        selected_user = ctx.guild.members[nicks[user]]
        
    elif(user in names):
        print(ctx.guild.members[names[user]])
        selected_user = ctx.guild.members[names[user]]
        
    elif(user in discriminators):
        print(ctx.guild.members[discriminators[user]])
        selected_user = ctx.guild.members[discriminators[user]]
        


@bot.command()
async def text_me(ctx):
    BOT_TEXT_CHANNEL = bot.get_channel(BOT_TEXT_CHANNEL_ID)
    await BOT_TEXT_CHANNEL.send("test")


# event examples

@bot.event
async def on_ready():
    # # Setting `Playing ` status
    # await bot.change_presence(activity=discord.Game(name="a game"))
    # # Setting `Streaming ` status
    # await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))
    # # Setting `Listening ` status
    # await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))
    # # Setting `Watching ` status
    # await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))

    # await bot.change_presence(status=discord.Status.idle)
    # await bot.change_presence(status=discord.Status.offline)
    await bot.change_presence(status=discord.Status.online)
    print("bot is active")


@bot.listen()
async def on_message(message): 
    if(message.author == bot.user):
        return

    # don't respond with the word "bot" or you will call the on_message event recursively
    if("bot" in message.content.lower()):
        await message.channel.send("hi")
        await bot.process_commands(message)


# better way
# message_responses
message_responses_exact = {"a":"a"}
message_responses_in = {"bbb":"bbb"}
@bot.listen()
async def on_message(message):

    if(message.author == bot.user):
        return

    for m in message_responses_exact:
        if(m == message.content.lower()):
            await message.channel.send(message_responses_exact[m])
            await bot.process_commands(message)
            return

    for m in message_responses_in:
        if(m in message.content.lower()):
            await message.channel.send(message_responses_in[m])
            await bot.process_commands(message)
            return


bot.run(TOKEN)