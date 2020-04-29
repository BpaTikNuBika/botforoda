import discord
from discord.ext import commands
import time
import asyncio
import random
import os
from random import randint
import shutil
from os import system
import youtube_dl
from discord.ext import commands
from discord.utils import get

PREFIX = 'am!'

client = commands.Bot(command_prefix = PREFIX)
client.remove_command('help')
# on ready
@client.event
async def on_ready():
    print("Bot is online")
    await client.change_presence(status = discord.Status.dnd,activity=discord.Activity(type=discord.ActivityType.watching, name=" за сервером ODA"))
#hello
@client.command(pass_context = True)
async def hello(ctx):
    authormsg = ctx.message.author

    await ctx.send(f'Привет { authormsg.mention }!')
#clear
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )
async def clear( ctx, amount = 100 ):
    await ctx.channel.purge( limit = amount )
#kick
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )
async def kick( ctx, member: discord.Member, *, reason = None ):
    await ctx.channel.purge( limit = 1 )

    await member.kick( reason = reason )
    await ctx.send( f'User kicked { member.mention }' )
#ban
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )
async def ban( ctx, member: discord.Member, *, reason = None ):
    await ctx.channel.purge( limit = 1 )

    await member.kick( reason = reason )
    await ctx.send( f'User banned { member.mention }' )
#say
@client.command()
@commands.has_permissions(administrator = True)
async def say(ctx, arg):
    await ctx.channel.purge( limit = 1 )
    await ctx.send(arg)
#test
@client.command()
@commands.has_permissions(administrator = True)
async def tests(ctx, arg):
    first = 100
    Varible = int (arg)
    Varible2 = Varible + first
    await ctx.send(Varible2)
#sayc
@client.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def sayc(ctx):
    await ctx.message.delete()
    say_at_me = input("Введите сообщение через консоль: ")
    await ctx.send(say_at_me)
#coinflip
@client.command()
async def cf(ctx):
    a = random.randint(1, 2)
    if a == 1:
        await ctx.send('Вам выпал орёл')
    else:
        await ctx.send('Вам выпала решка')
#guild name
@client.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def gc(ctx):
    await ctx.guild.edit(name="👈|Anima|👈")
    await asyncio.sleep(0.5)
    await ctx.guild.edit(name="👉|ДВСА|👉")
    await asyncio.sleep(0.5)
    await ctx.guild.edit(name="👍|ODA|👍")
    await asyncio.sleep(0.5)
    task = asyncio.create_task(gc(ctx))


colorr = [discord.Color.dark_orange(),discord.Color.orange(),discord.Color.dark_gold(),discord.Color.gold(),discord.Color.dark_magenta(),discord.Color.magenta(),discord.Color.red(),discord.Color.dark_red(),discord.Color.blue(),discord.Color.dark_blue(),discord.Color.teal(),discord.Color.dark_teal(),discord.Color.green(),discord.Color.dark_green(),discord.Color.purple(),discord.Color.dark_purple()] 
rainbowrolename = "Rainbow"
serverid = 693430308749443072
#rainbow
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
                await asyncio.sleep(0.1)
                client.loop.create_task(rainbow(ctx, arg))
    else:
        for role in client.get_guild(698831537889607720).roles: # радуга для ОДА 
            if str(role) == str(rainbowrolename):
                print(role)
                await role.edit(color=random.choice(colorr))
                print("detected role")
                await asyncio.sleep(0.1)
                client.loop.create_task(rainbow(ctx, arg))
#casino
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

@client.command(pass_context=True, aliases=['j', 'joi'])
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"The bot has connected to {channel}\n")

    await ctx.send(f"Подключенно к {channel}")


@client.command(pass_context=True, aliases=['l', 'lea'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"The bot has left {channel}")
        await ctx.send(f"Оклченно от {channel}")
    else:
        print("Bot was told to leave voice channel, but was not in one")
        await ctx.send("Я нахожусь не в голосовом канале")

@client.command(pass_context=True, aliases=['v', 'vol'])
async def volume(ctx, arg):
    VOLUME3 = 0.07
    VOLUME1 = int (arg)
    await ctx.send(VOLUME1)
    VOLUME2 = VOLUME1 - 30 
    VOLUME3 = VOLUME2 / 1000
    await ctx.send(VOLUME3)
    print("Volume set:", VOLUME3)

@client.command(pass_context=True, aliases=['p', 'pla'])
async def play(ctx, url: str):

    def check_queue():
        Queue_infile = os.path.isdir("./Queue")
        if Queue_infile is True:
            DIR = os.path.abspath(os.path.realpath("Queue"))
            length = len(os.listdir(DIR))
            still_q = length - 1
            try:
                first_file = os.listdir(DIR)[0]
            except:
                print("No more queued song(s)\n")
                queues.clear()
                return
            main_location = os.path.dirname(os.path.realpath(__file__))
            song_path = os.path.abspath(os.path.realpath("Queue") + "\\" + first_file)
            if length != 0:
                print("Song done, playing next queued\n")
                print(f"Songs still in queue: {still_q}")
                song_there = os.path.isfile("song.mp3")
                if song_there:
                    os.remove("song.mp3")
                shutil.move(song_path, main_location)
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file, 'song.mp3')

                voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = VOLUME3

            else:
                queues.clear()
                return

        else:
            queues.clear()
            print("No songs were queued before the ending of the last song\n")



    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            queues.clear()
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("ОШИБКА")
        return


    Queue_infile = os.path.isdir("./Queue")
    try:
        Queue_folder = "./Queue"
        if Queue_infile is True:
            print("Removed old Queue Folder")
            shutil.rmtree(Queue_folder)
    except:
        print("No old Queue folder")

    await ctx.send("Подождите")

    voice = get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading audio now\n")
            ydl.download([url])
    except:
        print("FALLBACK: youtube-dl does not support this URL, using Spotify (This is normal if Spotify URL)")
        c_path = os.path.dirname(os.path.realpath(__file__))
        system("spotdl -f " + '"' + c_path + '"' + " -s " + url)

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = VOLUME

    nname = name.rsplit("-", 2)
    await ctx.send(f"Играет: {nname[0]}")
    print("playing\n")


@client.command(pass_context=True, aliases=['pa', 'pau'])
async def pause(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Music paused")
        voice.pause()
        await ctx.send("Музыка била поставленна на паузу")
    else:
        print("Music not playing failed pause")
        await ctx.send("Музыка не играет не удалось поставить на паузу")


@client.command(pass_context=True, aliases=['r', 'res'])
async def resume(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        print("Resumed music")
        voice.resume()
        await ctx.send("Музыка продолжает играть")
    else:
        print("Music is not paused")
        await ctx.send("Музыка не на паузе")


@client.command(pass_context=True, aliases=['st', 'sto'])
async def stop(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    queues.clear()

    queue_infile = os.path.isdir("./Queue")
    if queue_infile is True:
        shutil.rmtree("./Queue")

    if voice and voice.is_playing():
        print("Music stopped")
        voice.stop()
        await ctx.send("Музыка остановлена")
        os.remove("song.mp3")
    else:
        print("No music playing failed to stop")
        await ctx.send("Музыка не играет не удалось остановить")
        os.remove("song.mp3")


queues = {}

@client.command(pass_context=True, aliases=['sa', 'sad'])
async def sadd(ctx, url: str):
    Queue_infile = os.path.isdir("./Queue")
    if Queue_infile is False:
        os.mkdir("Queue")
    DIR = os.path.abspath(os.path.realpath("Queue"))
    q_num = len(os.listdir(DIR))
    q_num += 1
    add_queue = True
    while add_queue:
        if q_num in queues:
            q_num += 1
        else:
            add_queue = False
            queues[q_num] = q_num

    queue_path = os.path.abspath(os.path.realpath("Queue") + f"\song{q_num}.%(ext)s")

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'outtmpl': queue_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading audio now\n")
            ydl.download([url])
    except:
        print("FALLBACK: youtube-dl does not support this URL, using Spotify (This is normal if Spotify URL)")
        q_path = os.path.abspath(os.path.realpath("Queue"))
        system(f"spotdl -ff song{q_num} -f " + '"' + q_path + '"' + " -s " + url)


    await ctx.send("Додаю песню #" + str(q_num) + " к очереди")

    print("Song added to queue\n")


@client.command(pass_context=True, aliases=['s', 'skp'])
async def skip(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Playing Next Song")
        voice.stop()
        await ctx.send("Следущая песня")
    else:
        print("No music playing")
        await ctx.send("Музыка не играет")

@client.command(pass_context=True) #Я тут коечто изменил 
async def help(ctx):
    colors = [discord.Color.dark_orange(),discord.Color.orange(),discord.Color.dark_gold(),discord.Color.gold(),discord.Color.dark_magenta(),discord.Color.magenta(),discord.Color.red(),discord.Color.dark_red(),discord.Color.blue(),discord.Color.dark_blue(),discord.Color.teal(),discord.Color.dark_teal(),discord.Color.green(),discord.Color.dark_green(),discord.Color.purple(),discord.Color.dark_purple()]
    embed = discord.Embed(
        colour=random.choice(colors),
        title="Мои комманды!",
        description="Мой префикс {}".format(PREFIX) )

    embed.set_author(name='Мой Разаработчик "⌠𝓐⌡ῼр̷а̷н̷д̷о̷м̷̷ч̷и̷к̷ῼ"', icon_url='https://cdn.discordapp.com/avatars/451306546123767808/94ba37a999f838511292e162cd29b064.png?size=128')
    embed.add_field(name="{}help".format(PREFIX), value="Вызывает эту страницу", inline=False)
    embed.add_field(name="{}kick".format(PREFIX), value="Кикает указанного профиля", inline=False)
    embed.add_field(name="{}Ban".format(PREFIX), value="Банит указанного профиля", inline=False)
    embed.add_field(name="{}clear".format(PREFIX), value="Чистка сообщений", inline=False)
    embed.add_field(name="{}say".format(PREFIX), value="Вы можете отправить сообщение от именни бота!", inline=False)
    embed.add_field(name="{}scyc".format(PREFIX), value="Только для администратора, вы можете сказать от имени бота через КОНСОЛЬ!", inline=False)
    embed.add_field(name="{}hello".format(PREFIX), value="Скажите привет боту :)", inline=False)
    embed.add_field(name="{}rainbow".format(PREFIX), value="Включает радужную роль ( Для администраторов )", inline=False)
    embed.add_field(name="{}casino".format(PREFIX), value="Казино (пока что не работает)", inline=False)
    embed.add_field(name="{}cf".format(PREFIX), value="Под бросить монету", inline=False)
    embed.add_field(name="{}gc".format(PREFIX), value="Анимированое название гильдии", inline=False)
    embed.add_field(name="{}join".format(PREFIX), value="Присойденить бота к вам в канал(j или joi)", inline=False)
    embed.add_field(name="{}leave".format(PREFIX), value="Заставить бота отключитса от вашего канала(l или lea)", inline=False)
    embed.add_field(name="{}skip".format(PREFIX), value="Следуйщая песня в очереди(s или skp)", inline=False)
    embed.add_field(name="{}pause".format(PREFIX), value="Поставить на паузу песню котороя сечяс играет(p или pau)", inline=False)
    embed.add_field(name="{}play".format(PREFIX), value="Включить песню по url(p или pla)", inline=False)
    embed.add_field(name="{}sadd".format(PREFIX), value="Добавить песню в очередь(s или sad)", inline=False)
    embed.add_field(name="{}resume".format(PREFIX), value="Продолжает проигровать песню котороя стоит на паузе(r или res)", inline=False)
    embed.add_field(name="{}stop".format(PREFIX), value="Останавливает песню котороя щяс играет(st или sto)", inline=False)
    embed.add_field(name="{}volume".format(PREFIX), value="Тестовая функция изменнения громкости(v или vol)", inline=False)
    await ctx.send(embed=embed)

client.run('NzAwNjE4NDM3ODQzNDg0Njg0.XqgX2w.5vf8BT1N454zu-UIKijAs2kh0P4')
token = os.environ.get('BOT_TOKEN')
client.run(str(token))
