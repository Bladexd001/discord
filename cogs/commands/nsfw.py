############MODULES#############
import discord
import requests
import datetime
from discord.ext import commands
from utils.Tools import *
from core import Cog, Astroz, Context



class Nsfw(commands.Cog):
    def __init__(self, client):
        self.client = client





            
    @commands.group(name="Nsfw",invoke_without_command=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @blacklist_check()   
    @ignore_check()
    async def nsfw(self, ctx: commands.Context):
      if ctx.subcommand_passed is None:
          await ctx.send_help(ctx.command)
          ctx.command.reset_cooldown(ctx)
          
          
          
    @nsfw.command(name="4k")
    @blacklist_check()   
    @ignore_check()
    async def _4k(self, ctx):
      ok = requests.get("http://api.nekos.fun:8080/api/4k")
      data = ok.json()
      image = data["image"]
      if ctx.channel.is_nsfw() != True:
         await ctx.reply(embed=discord.Embed(description="Please Enable The NSFW Option From Channel Setting To Continue Forward:",color=0x01f5b6,timestamp=datetime.datetime.utcnow()).set_image(url="https://support.discord.com/hc/article_attachments/4580654542103/unnamed.png").set_thumbnail(url=ctx.author.display_avatar.url))
      else:
       embed = discord.Embed(color=0x01f5b6,timestamp=datetime.datetime.utcnow())
      embed.set_image(url=image)
      await ctx.send(embed=embed)

    @blacklist_check()   
    @ignore_check()
    @nsfw.command(name="pussy")
    async def _pussy(self, ctx):
      ok = requests.get("http://api.nekos.fun:8080/api/pussy")
      data = ok.json()
      image = data["image"]
      if ctx.channel.is_nsfw() != True:
         await ctx.reply(embed=discord.Embed(description="Please Enable The NSFW Option From Channel Setting To Continue Forward:",color=0x01f5b6,timestamp=datetime.datetime.utcnow()).set_image(url="https://support.discord.com/hc/article_attachments/4580654542103/unnamed.png").set_thumbnail(url=ctx.author.display_avatar.url))
      else:
       embed = discord.Embed(color=0x01f5b6,timestamp=datetime.datetime.utcnow())
      embed.set_image(url=image)
      await ctx.send(embed=embed)
      
      
      
    @blacklist_check()   
    @ignore_check()
    @nsfw.command(name="boobs")
    async def _boobs(self, ctx):
      ok = requests.get("http://api.nekos.fun:8080/api/boobs")
      data = ok.json()
      image = data["image"]
      if ctx.channel.is_nsfw() != True:
         await ctx.reply(embed=discord.Embed(description="Please Enable The NSFW Option From Channel Setting To Continue Forward:",color=0x01f5b6,timestamp=datetime.datetime.utcnow()).set_image(url="https://support.discord.com/hc/article_attachments/4580654542103/unnamed.png").set_thumbnail(url=ctx.author.display_avatar.url))
      else:
       embed = discord.Embed(color=0x01f5b6,timestamp=datetime.datetime.utcnow())
      embed.set_image(url=image)
      await ctx.send(embed=embed)
      
      
      
    @blacklist_check()   
    @ignore_check()
    @nsfw.command(name="lewd")
    async def _lewd(self, ctx):
      ok = requests.get("http://api.nekos.fun:8080/api/lewd")
      data = ok.json()
      image = data["image"]
      if ctx.channel.is_nsfw() != True:
         await ctx.reply(embed=discord.Embed(description="Please Enable The NSFW Option From Channel Setting To Continue Forward:",color=0x01f5b6,timestamp=datetime.datetime.utcnow()).set_image(url="https://support.discord.com/hc/article_attachments/4580654542103/unnamed.png").set_thumbnail(url=ctx.author.display_avatar.url))
      else:
       embed = discord.Embed(color=0x01f5b6,timestamp=datetime.datetime.utcnow())
      embed.set_image(url=image)
      await ctx.send(embed=embed)
      
      
    @blacklist_check()   
    @ignore_check()
    @nsfw.command(name="lesbian")
    async def _lesbian(self, ctx):
      ok = requests.get("http://api.nekos.fun:8080/api/lesbian")
      data = ok.json()
      image = data["image"]
      if ctx.channel.is_nsfw() != True:
         await ctx.reply(embed=discord.Embed(description="Please Enable The NSFW Option From Channel Setting To Continue Forward:",color=0x01f5b6,timestamp=datetime.datetime.utcnow()).set_image(url="https://support.discord.com/hc/article_attachments/4580654542103/unnamed.png").set_thumbnail(url=ctx.author.display_avatar.url))
      else:
       embed = discord.Embed(color=0x01f5b6,timestamp=datetime.datetime.utcnow())
      embed.set_image(url=image)
      await ctx.send(embed=embed)
      
    
    @blacklist_check()   
    @ignore_check()
    @nsfw.command(name="blowjob")
    async def _blowjob(self, ctx):
      ok = requests.get("http://api.nekos.fun:8080/api/blowjob")
      data = ok.json()
      image = data["image"]
      if ctx.channel.is_nsfw() != True:
         await ctx.reply(embed=discord.Embed(description="Please Enable The NSFW Option From Channel Setting To Continue Forward:",color=0x01f5b6,timestamp=datetime.datetime.utcnow()).set_image(url="https://support.discord.com/hc/article_attachments/4580654542103/unnamed.png").set_thumbnail(url=ctx.author.display_avatar.url))
      else:
       embed = discord.Embed(color=0x01f5b6,timestamp=datetime.datetime.utcnow())
      embed.set_image(url=image)
      await ctx.send(embed=embed)
      
    @blacklist_check()   
    @ignore_check()
    @nsfw.command(name="cum")
    async def _cum(self, ctx):
      ok = requests.get("http://api.nekos.fun:8080/api/cum")
      data = ok.json()
      image = data["image"]
      if ctx.channel.is_nsfw() != True:
         await ctx.reply(embed=discord.Embed(description="Please Enable The NSFW Option From Channel Setting To Continue Forward:",color=0x01f5b6,timestamp=datetime.datetime.utcnow()).set_image(url="https://support.discord.com/hc/article_attachments/4580654542103/unnamed.png").set_thumbnail(url=ctx.author.display_avatar.url))
      else:
       embed = discord.Embed(color=0x01f5b6,timestamp=datetime.datetime.utcnow())
      embed.set_image(url=image)
      await ctx.send(embed=embed)
      
      
    @blacklist_check()   
    @ignore_check()
    @nsfw.command(name="gasm")
    async def _gasm(self, ctx):
      ok = requests.get("http://api.nekos.fun:8080/api/gasm")
      data = ok.json()
      image = data["image"]
      if ctx.channel.is_nsfw() != True:
         await ctx.reply(embed=discord.Embed(description="Please Enable The NSFW Option From Channel Setting To Continue Forward:",color=0x01f5b6,timestamp=datetime.datetime.utcnow()).set_image(url="https://support.discord.com/hc/article_attachments/4580654542103/unnamed.png").set_thumbnail(url=ctx.author.display_avatar.url))
      else:
       embed = discord.Embed(color=0x01f5b6,timestamp=datetime.datetime.utcnow())
      embed.set_image(url=image)
      await ctx.send(embed=embed)
      
    @blacklist_check()   
    @ignore_check()
    @nsfw.command(name="hentai")
    async def _hentai(self, ctx):
      ok = requests.get("http://api.nekos.fun:8080/api/hentai")
      data = ok.json()
      image = data["image"]
      if ctx.channel.is_nsfw() != True:
         await ctx.reply(embed=discord.Embed(description="Please Enable The NSFW Option From Channel Setting To Continue Forward:",color=0x01f5b6,timestamp=datetime.datetime.utcnow()).set_image(url="https://support.discord.com/hc/article_attachments/4580654542103/unnamed.png").set_thumbnail(url=ctx.author.display_avatar.url))
      else:
       embed = discord.Embed(color=0x01f5b6,timestamp=datetime.datetime.utcnow())
      embed.set_image(url=image)
      await ctx.send(embed=embed)







