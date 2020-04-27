import discord
from discord.ext import commands
import time
import asyncio
import random
import os

PREFIX = '!'

client = commands.Bot(command_prefix = PREFIX)

@client.event
async def on_ready():
    print("Bot is online")
    await client.change_presence(status = discord.Status.dnd,activity=discord.Activity(type=discord.ActivityType.watching, name=" за сервером ODA"))

@client.command(pass_context = True)
async def hello(ctx):
    authormsg = ctx.message.author

    await ctx.send(f'Привет { authormsg.mention }!')



@client.command()
@commands.has_permissions(administrator = True)
async def say(ctx, arg):
    await ctx.channel.purge( limit = 1 )
    await ctx.send(arg)

@client.command()
@commands.has_permissions(administrator = True)
async def tests(ctx, arg):
    first = 100
    Varible = int (arg)
    Varible2 = Varible + first
    await ctx.send(Varible2)

@client.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def sayc(ctx):
    await ctx.message.delete()
    say_at_me = input("Введите сообщение через консоль: ")
    await ctx.send(say_at_me)

@client.command()
async def cf(ctx):
    a = random.randint(1, 2)
    if a == 1:
        await ctx.send('Вам выпал орёл')
    else:
        await ctx.send('Вам выпала решка')

@client.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def gc(ctx):
    await ctx.guild.edit(name="👈|Anima|👈")
    await asyncio.sleep(0.2)
    await ctx.guild.edit(name="👉|ДВСА|👉")
    await asyncio.sleep(0.2)
    await ctx.guild.edit(name="👍|ODA|👍")
    await asyncio.sleep(0.2)
    task = asyncio.create_task(gc(ctx))


colorr = [discord.Color.dark_orange(),discord.Color.orange(),discord.Color.dark_gold(),discord.Color.gold(),discord.Color.dark_magenta(),discord.Color.magenta(),discord.Color.red(),discord.Color.dark_red(),discord.Color.blue(),discord.Color.dark_blue(),discord.Color.teal(),discord.Color.dark_teal(),discord.Color.green(),discord.Color.dark_green(),discord.Color.purple(),discord.Color.dark_purple()] 
rainbowrolename = "Rainbow"
serverid = 693430308749443072

@client.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def rainbow(ctx, arg):
    args = str(arg)
    SERVER = 'test'
    if str(args) == str(SERVER):
        for role in client.get_guild(693430308749443072).roles: # радуга для сервера теста
            if str(role) == str(rainbowrolename):
                print(role)
                await role.edit(color=random.choice(colorr))
                print("detected role")
                await asyncio.sleep(2)
                client.loop.create_task(rainbow(ctx, arg))
    else:
        for role in client.get_guild(698831537889607720).roles: # радуга для ОДА (У меня не работает)
            if str(role) == str(rainbowrolename):
                print(role)
                await role.edit(color=random.choice(colorr))
                print("detected role")
                await asyncio.sleep(2)
                client.loop.create_task(rainbow(ctx))

@client.command()
async def casino(ctx):
    lng = str(input("Язык"))
    if lng == "rus":

        ageplone = int(input("Введите ваш возраст"))
        agepltwo = int(input("Введите ваш возраст"))
        if agepltwo >= 18 and ageplone >= 18:
            print("Вы подходите")
        else:
            print("Вы не подходите")
            exit(0)

        plone = str(input("Введите имя 1 игрока"))
        pltwo = str(input("Введите имя 2 игрока"))
        p = "yes"
        while p == "yes":
            a = randint(1, 6)
            print(plone, "выпало", a)
            time.sleep(3)
            b = randint(1, 6)
            print(pltwo, "выпало", b)

            if a > b:
                print("Победил", plone)
            elif a == b:
                print("Ничья")
            else:
                print("Победил", pltwo)
            p = str(input('хотите ли вы?'))

    else:

        ageplone = int(input("Enter your age"))
        agepltwo = int(input("Enter your age"))
        if agepltwo >= 18 and ageplone >= 18:
           print("You fit")
        else:
            print("You no fit")
            exit(0)

        plone = str(input("Введите имя 1 игрока"))
        pltwo = str(input("Введите имя 2 игрока"))
        p = "yes"
        while p == "yes":
            a = randint(1, 6)
            print(plone, "выпало", a)
            time.sleep(3)
            b = randint(1, 6)
            print(pltwo, "выпало", b)

            if a > b:
                print("Победил", plone)
            elif a == b:
                print("Ничья")
            else:
                print("Победил", pltwo)
            p = str(input('хотите ли вы?'))

token = os.environ.get('BOT TOKEN')
