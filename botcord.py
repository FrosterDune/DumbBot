import asyncio

import nextcord
import copypasty
import Derp
import private
import lists
import kvadra
from nextcord.ext import commands, tasks
from nextcord.ext.commands import has_permissions, CommandNotFound
from random import choice
from typing import Optional

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
descriptions = copypasty.Description()
copypasta = copypasty.Copypasta()
derpy = Derp.Commands()
random_derp = Derp.Random()
channelid = private.ChannelIDrequest.bot_image_posting()
token = private.token.token()
trainlist = lists.Command()
kvadr = kvadra.Commands()

#events
@bot.event
async def on_ready():
    print("I'm ready")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.message.delete()
        await ctx.send(error)

#Basic custom commands
@bot.slash_command(description="Shows bot latency")
async def ping(ctx):
    await ctx.send(f"Bot Speed - {round(bot.latency * 1000)}ms", ephemeral=True)

@bot.slash_command(description="You know what is this (nextcord)")
async def chalice(ctx):
    embed = nextcord.Embed(title="I, EvaX", description=copypasta.chalice())
    embed.set_thumbnail("https://pbs.twimg.com/media/Ejh9-w8WsAAwQCi.jpg")
    await ctx.send(embed=embed)

@bot.slash_command(description=descriptions.zyzzdes())
async def zyzz(ctx: nextcord.Interaction):
    await ctx.response.defer()
    await ctx.followup.send("**We're All Gonna Make It Brah 💪**", file=nextcord.File('zyzz.mp4'))

@bot.slash_command(description="najde vlak který jezdí na trati 270 (pouze Os/Sp/R)", default_member_permissions=8)
async def train(ctx, input: int):
    embed = nextcord.Embed(description=trainlist.vypis(input=input))
    await ctx.send(embed=embed, ephemeral=True)

@bot.slash_command(description="kvadratická rovnice protože proč kurva ne")
async def kvadra(ctx, a: float, b: float, c:float):
    embed = nextcord.Embed(description=kvadr.vypis(a=a, b=b, c=c))
    await ctx.send(embed=embed, ephemeral=True)

@bot.slash_command(description="Make string more retarded")
async def retard(ctx, message:str):
    retarder = "".join(choice((str.upper, str.lower))(char) for char in message)
    await ctx.send(retarder)

@bot.slash_command(description="reply test with link")
async def tvojemama(ctx: nextcord.Interaction, message_link: Optional[str] = nextcord.SlashOption(required=False)):
    await ctx.response.defer()
    await ctx.followup.send(file=nextcord.File('tvojemama.mp4'))
    if message_link is not None:
        await ctx.channel.send(f"od {ctx.user.mention} na zprávu: {message_link}")
    else:
        await ctx.channel.send(f"od {ctx.user.mention}")

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

@bot.command(name="msg")
@has_permissions(manage_messages=True)
async def sendmsg(ctx, *, message: str):
    await ctx.send(message)
    await ctx.message.delete()

#Commands for start or stop loop events
@bot.slash_command(description="start 1. loop (random art from ARTISTS list)", default_member_permissions=8)
async def startloop1(ctx):
    send_random_artfromartist.start()
    await ctx.send("successful", ephemeral=True)

@bot.slash_command(description="start 2. loop (random art)", default_member_permissions=8)
async def startloop2(ctx):
    send_random_art.start()
    await ctx.send("successful", ephemeral=True)

@bot.slash_command(description="stopping loop1 (art from ARTISTS list)", default_member_permissions=8)
async def stoploop1(ctx):
    send_random_artfromartist.stop()
    print("loop1 stopped")
    await ctx.send("successful", ephemeral=True)

@bot.slash_command(description="stopping loop2 (random art)", default_member_permissions=8)
async def stoploop2(ctx):
    send_random_art.stop()
    print("loop2 stopped")
    await ctx.send("successful", ephemeral=True)

#Loop events
@tasks.loop(seconds=10)
async def send_random_artfromartist():
    message_channel = bot.get_channel(channelid)
    await message_channel.send(random_derp.randomimageartistslist())

@send_random_artfromartist.before_loop
async def before():
    await bot.wait_until_ready()
    print("loop1 has started")

@tasks.loop(seconds=5)
async def send_random_art():
    message_channel = bot.get_channel(channelid)
    await message_channel.send(random_derp.randomimage(upvotes=350))

@send_random_art.before_loop
async def before():
    await bot.wait_until_ready()
    print("loop2 has started")


bot.run(token)