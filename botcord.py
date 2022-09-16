import nextcord
import copypasty
import Derp
import private
from nextcord.ext import commands, tasks
from nextcord.ext.commands import command, has_permissions, bot_has_permissions, Cog, cog
from better_profanity import profanity
from math import sqrt
import datetime

bot = commands.Bot()
descriptions = copypasty.Description()
copypasta = copypasty.Copypasta()
derpy = Derp.Commands()
random_derp = Derp.Random()
channelid = private.ChannelIDrequest()
token = private.token()

@bot.event
async def on_ready():
    print("I'm ready")

#Loop events
@tasks.loop(seconds=15)
async def send_random_artfromartist():
    message_channel = bot.get_channel(channelid.bot_image_posting())
    await message_channel.send(random_derp.randomimageartistslist())

@send_random_artfromartist.before_loop
async def before():
    await bot.wait_until_ready()
    print("waiting finished loop1")

@tasks.loop(seconds=15)
async def send_random_art():
    message_channel = bot.get_channel(channelid.bot_image_posting())
    await message_channel.send(random_derp.randomimage(upvotes=350))

@send_random_art.before_loop
async def before():
    await bot.wait_until_ready()
    print("finished waiting loop2")

#Basic custom commands
@bot.slash_command(description="You know what is this (nextcord)")
async def chalice(ctx):
    embed = nextcord.Embed(title="I, EvaX", description=copypasta.chalice())
    embed.set_thumbnail("https://pbs.twimg.com/media/Ejh9-w8WsAAwQCi.jpg")
    await ctx.send(embed=embed)

@bot.slash_command(description=descriptions.zyzzdes())
async def zyzz(ctx):
    await ctx.channel.send("**We're All Gonna Make It Brah 💪**", file=nextcord.File('zyzz.mp4'))

@bot.slash_command(description="kvadratická rovnice protože proč kurva ne")
async def kvadra(ctx, a: float, b: float, c:float):
    try:
        D = b**2-4*a*c
        x1 = (-b+sqrt(D))/(2*a)
        x2 = (-b-sqrt(D))/(2*a)
        await ctx.send(f"x1 = {x1}\nx2 = {x2}", ephemeral=True)
    except(ValueError):
        await ctx.send("nelze vypočítat, rovnice nemá řešení, try me bitch again", ephemeral=True)

#DerPyBooru commands
@bot.slash_command(description="post random art from Light")
async def light(ctx, upvotes: int):
    await ctx.send(derpy.light(upvotes=upvotes))
@bot.slash_command(description="post a random art from Coco")
async def coco(ctx):
    await ctx.send(derpy.coco())
@bot.slash_command(description="post a random art from Dyo")
async def dyo(ctx, upvotes: int):
    await ctx.send(derpy.dyo(upvotes=upvotes))
@bot.slash_command(description="post a random art from Quint")
async def quint(ctx):
    await ctx.send(derpy.quint())
@bot.slash_command(description="post a random image from Ginny")
async def ginny(ctx):
    await ctx.send(derpy.ginny())

@bot.slash_command(description="post a random image from Derpi")
async def randomderp(ctx, upvotes: int):
    await ctx.send(random_derp.randomimage(upvotes=upvotes))

@bot.slash_command(description=descriptions.randomderpartists())
async def randomderpartists(ctx):
    await ctx.send(random_derp.randomimageartistslist())

#Server manipulation for admins
@bot.slash_command(description="clear messages above", default_member_permissions=8)
@has_permissions(manage_messages=True)
async def clear(ctx, limit: int):
    if 0 < limit <=10:
        await ctx.channel.purge(limit=limit)
        await ctx.send("cleaning was successful", ephemeral=True)
    else:
        await ctx.send("I can delete only 10 messages at once", ephemeral=True)

@bot.slash_command(description="send message through bot", default_member_permissions=8, force_global=False)
@has_permissions(manage_messages=True)
async def sendmsg(ctx, message: str):
    await ctx.send(message)

#Commands for start or stop loop events
@bot.slash_command(description="start 1. loop", default_member_permissions=8)
async def startloop1(ctx):
    send_random_artfromartist.start()
    await ctx.send("successful", ephemeral=True)

@bot.slash_command(description="start 2. loop", default_member_permissions=8)
async def startloop2(ctx):
    send_random_art.start()
    await ctx.send("successful", ephemeral=True)

@bot.slash_command(description="stopping loop1", default_member_permissions=8)
async def stoploop1(ctx):
    send_random_artfromartist.stop()
    await ctx.send("successful", ephemeral=True)

@bot.slash_command(description="stopping loop2", default_member_permissions=8)
async def stoploop2(ctx):
    send_random_art.stop()
    await ctx.send("successful", ephemeral=True)


bot.run(token.token())
