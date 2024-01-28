import contextlib
from traceback import format_exception
import discord
from discord.ext import commands
import io
import textwrap
import datetime
import sys
from discord.ui import Button, View
import psutil
import time
import datetime
import platform
from utils.Tools import *
import os
import logging
from discord.ext import commands
import motor.motor_asyncio
from pymongo import MongoClient
from discord.ext.commands import BucketType, cooldown
import requests
import motor.motor_asyncio as mongodb
from typing import Optional
from utils import *
from utils import Paginator, DescriptionEmbedPaginator, FieldPagePaginator, TextPaginator 


import pathlib, shutil

def get_ram_usage():
    return int(psutil.virtual_memory().total - psutil.virtual_memory().available)


def get_ram_total():
    return int(psutil.virtual_memory().total)




start_time = time.time()





def datetime_to_seconds(thing: datetime.datetime):
    current_time = datetime.datetime.fromtimestamp(time.time())
    return round(round(time.time()) + (current_time - thing.replace(tzinfo=None)).total_seconds())
cluster = motor.motor_asyncio.AsyncIOMotorClient(       "mongodb+srv://Punitkumar69:7CC5i4DIQ7Rfwbb7@guardian.ormln1v.mongodb.net/?retryWrites=true&w=majority")

notedb = cluster["discord"]["note"]




class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.connection = mongodb.AsyncIOMotorClient(
          "mongodb+srv://Punitkumar69:7CC5i4DIQ7Rfwbb7@guardian.ormln1v.mongodb.net/?retryWrites=true&w=majority"
        )
        self.db = self.connection["Astroz"]["servers"]  



  

      
    @commands.group(name="banner")
    async def banner(self, ctx):
      if ctx.invoked_subcommand is None:
        await ctx.send_help(ctx.command)



    @banner.command(name="server")
    async def server(self, ctx):
      if not ctx.guild.banner:
        await ctx.reply("This server does not have a banner...")
      else:
        embed = discord.Embed(title=ctx.guild.name, color=0x01f5b6)
        embed.set_image(url=ctx.guild.banner)
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon.url if ctx.guild.icon else ctx.guild.default_icon.url)
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.reply(embed=embed)



    @banner.command(name="user")
    async def user(self, ctx, user: discord.Member=None):
      if user == None:
        user = ctx.author
      bid = await self.bot.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
      banner_id = bid["banner"]
      if banner_id:
        embed = discord.Embed(color=0x01f5b6)
        embed.set_author(name=f"{user}", icon_url=user.avatar.url if user.avatar else user.default_avatar.url)
        embed.set_image(url=f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024")
        await ctx.reply(embed=embed)
      else:
        await ctx.reply("{} does not have a banner...".format(user))


        
    @commands.hybrid_command(name="statistics",aliases=["st","stats"],usage="stats")
    @blacklist_check()   
    @ignore_check()
    async def stats(self, ctx):
        """Shows some usefull information about Astroz"""
        serverCount = len(self.bot.guilds)
        
        total_memory = psutil.virtual_memory().total >> 20
        used_memory = psutil.virtual_memory().used >> 20
        cpu_used = str(psutil.cpu_percent())
 
 
        total_members = sum(g.member_count for g in self.bot.guilds if g.member_count != None)
        cached_members = len(self.bot.users)
 
        b = Button(label='Invite Me', style=discord.ButtonStyle.link, url='https://discord.com/oauth2/authorize?client_id=1012627088232165376&permissions=2113268958&scope=bot')
        hacker = Button(label='Support Server', style=discord.ButtonStyle.link, url='https://discord.gg/D78YMq279a')
        #mohit = Button(label='Vote Me', style=discord.ButtonStyle.link, url='https://discord.com/oauth2/authorize?client_id=1021416292185546854&permissions=2113268958&scope=bot')
        view = View()
        view.add_item(b)
        view.add_item(hacker)
        #view.add_item(mohit)
 
        embed = discord.Embed(color=0x01f5b6,description="[Invite](https://discord.com/oauth2/authorize?client_id=1012627088232165376&permissions=2113268958&scope=bot) ● [Support Server](https://discord.gg/D78YMq279a)")
 
 
        embed.add_field(name='<a:discord:1009456425774362635> • **Servers**', value=f'```Total: {serverCount} Server```')
        embed.add_field(name='<:users:1009457592554225714> • **Users**', value=f'```Total: {total_members} Users```')
        embed.add_field(name="<:CPU:1009472944277307542> • **System**", value=f"```RAM: {used_memory}/{total_memory} MB\nCPU: {cpu_used}% used.```")
        embed.add_field(name="<:1349python:1009145861407785032> • **Python Version**", value=f"```{sys.version}```"),
        embed.add_field(name='<:1349python:1009145861407785032> • **Discord.py Version**', value=f'```{discord.__version__}```')
        embed.add_field(
            name="<a:botping:1009458753646637056> • **Ping**",
            value=f"```{round(self.bot.latency * 1000, 2)}ms```")
        hacker = await self.bot.fetch_user(143853929531179008)
        if hacker in ctx.guild.members:
            a = f'{hacker.mention}'
        else:
            a = f'{hacker}'
        luci = await self.bot.fetch_user(982132627836387379)
        if luci in ctx.guild.members:
            l = f'{luci.mention}'
        else:
            l = f'{luci}'

        hasan = await self.bot.fetch_user(301502732664307716)
        if hasan in ctx.guild.members:
            h = f'{hasan.mention}'
        else:
            h = f'{hasan}'
        embed.add_field(name='<a:Developer:1009460008204914829> • **Developers**', value=f"{a}\n{l}\n{h}")

        embed.set_author(name=f"{self.bot.user.name} Stats", icon_url=self.bot.user.display_avatar.url)
        embed.set_thumbnail(url=self.bot.user.display_avatar.url)
        embed.set_footer(text='Thanks For Using Astroz',icon_url= self.bot.user.display_avatar.url)
 
        await ctx.send(embed=embed, view=view)




    @commands.hybrid_command(name="invite",aliases=['inv'])
    @blacklist_check()   
    @ignore_check()
    async def invite(self, ctx: commands.Context):
        embed = discord.Embed( description = "> • [Click Here To Invite Astroz To Your Server](https://discord.com/oauth2/authorize?client_id=1012627088232165376&permissions=2113268958&scope=bot)\n> • [Click Here To Join My Support Server](https://discord.gg/D78YMq279a)\n> • [Click Here To Check Out Website Of Astroz](https://astroz.tk)", color=0x01f5b6, timestamp=ctx.message.created_at)
        embed.set_footer(icon_url=self.bot.user.display_avatar.url)
        embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
        await ctx.send(embed=embed)


    @commands.hybrid_command(name="uptime",aliases=['up'])
    @blacklist_check()   
    @ignore_check()
    async def uptime(self, ctx):
      uptime = datetime.datetime.utcnow() - start_time
      uptime = str(uptime).split(':')[0]
      await ctx.send(f"`Current Uptime:` "+''+uptime+'')

  
    @blacklist_check()   
    @ignore_check()
    @commands.hybrid_command(name="botinfo",aliases=['bi'], help="Get info about me!")
    async def botinfo(self, ctx: commands.Context):
        total, used, free = shutil.disk_usage("/")
        guilds = len(self.bot.guilds)
        users = sum(g.member_count for g in self.bot.guilds if g.member_count != None)
        p = pathlib.Path('./')
        button = Button(emoji="<:jk_inv:1051073323284561940>",label=f"{guilds} Guilds", style=discord.ButtonStyle.grey)
        button1 = Button(emoji="<:jk_support:1051073711463211068>",label=f"{users} Users", style=discord.ButtonStyle.grey)
        channel = len(set(self.bot.get_all_channels())) 
        embed = discord.Embed(
            description="An Advance Antinuke Bot Made To Protect Your Servers From Wizzers And Nukers",
            color=0x01f5b6,
            timestamp=datetime.datetime.utcnow()
        ).add_field(
            name="Stats:",
            value=f"""
```yaml\nGuilds: {len(self.bot.guilds)}
Users: {users}
Channels: {channel}
Commands: {len(set(self.bot.walk_commands()))}
Shards: {len(self.bot.shards)}
Python: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}
Uptime:{str(datetime.timedelta(seconds=int(round(time.time()-start_time))))}
Version: V2```""",
            inline=True
        ).add_field(
            name="Links:",
            value="""
- [Support](https://discord.gg/D78YMq279a)
- [Invite](https://discord.com/oauth2/authorize?client_id=1012627088232165376&permissions=2113268958&scope=bot)
- [Github](https://github.com/NotHerHacker)
            """,
            inline=True
        ).add_field(
            name="Storage:",
            value=f"""```yaml\nCPU:{round(psutil.cpu_percent())}%/100%\nRam:{int((psutil.virtual_memory().total - psutil.virtual_memory().available)
 / 1024 / 1024)}MB/{int((psutil.virtual_memory().total) / 1024 / 1024)}MB\nDisk: {used // (2 ** 30)}GB/{total // (2 ** 30)}GB\n```""",
            inline=True
        ).set_footer(text=self.bot.user.name, icon_url=self.bot.user.display_avatar.url
        ).set_author(name="Astroz Information`s", icon_url=self.bot.user.display_avatar.url
        ).set_thumbnail(url=self.bot.user.display_avatar.url)
        view = View()
        view.add_item(button)
        view.add_item(button1)
        await ctx.reply(embed=embed,view=view)


    @commands.hybrid_command(name="serverinfo",aliases=["sinfo","si"])
    @blacklist_check()   
    @ignore_check()
    async def serverinfo(self, ctx: commands.Context):
        nsfw_level = ''
        if ctx.guild.nsfw_level.name == 'default':
          nsfw_level = 'Default'
        if ctx.guild.nsfw_level.name == 'explicit':
          nsfw_level = 'Explicit'
        if ctx.guild.nsfw_level.name == 'safe':
          nsfw_level = 'Safe'
        if ctx.guild.nsfw_level.name == 'age_restricted':
          nsfw_level = 'Age Restricted'
        guild: discord.Guild = ctx.guild
        embed = discord.Embed(color=0x01f5b6
        ).set_author(
            name=f"{guild.name}'s Information",
            icon_url=guild.me.display_avatar.url if guild.icon is None else guild.icon.url
        ).set_footer(text=f"Requested By {ctx.author}",icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
        if guild.icon is not None:
            embed.set_thumbnail(url=guild.icon.url) 
            embed.timestamp = discord.utils.utcnow()
        embed.add_field(
            name="**__About__**",
            value=f"**Name : ** {guild.name}\n**ID :** {guild.id}\n**Owner <:Owner:1048556915963203684> :** {guild.owner} (<@{guild.owner_id}>)\n**Created At : **{guild.created_at.month}/{guild.created_at.day}/{guild.created_at.year}\n**Members :** {len(guild.members)}",
            inline=False
        )

        embed.add_field(
            name="**__Extras__**",
            value=f"""**Verification Level :** {str(guild.verification_level).title()}\n**AFK Channel :** {ctx.guild.afk_channel}\n**AFK Timeout :** {str(ctx.guild.afk_timeout / 60)}\n**System Channel :** {"None" if guild.system_channel is None else guild.system_channel.mention}\n**NSFW level :** {nsfw_level}\n**Explicit Content Filter :** {guild.explicit_content_filter.name}\n**Max Talk Bitrate :** {int(guild.bitrate_limit)} kbps""",
            inline=False
        ) 
        
        
        embed.add_field(
            name="**__Description__**",
            value=f"""{guild.description}""",
            inline=False
        )
        if guild.features:
            embed.add_field(
                name="**__Features__**",
                value='\n'.join([feature.replace('_', ' ').title() for feature in guild.features]),
                inline=False
            )
            
        embed.add_field(
            name="**__Members__**",
            value=f"""
Members : {len(guild.members)}
Humans : {len(list(filter(lambda m: not m.bot, guild.members)))}
Bots : {len(list(filter(lambda m: m.bot, guild.members)))}
            """,
            inline=False
        )
        
        embed.add_field(
            name="**__Channels__**",
            value=f"""
Categories : {len(guild.categories)}
Text Channels : {len(guild.text_channels)}
Voice Channels : {len(guild.voice_channels)}
Threads : {len(guild.threads)}
            """,
            inline=False
        )   
        
        embed.add_field(
            name="**__Emoji Info__**",
            value=f"Emojis : {len(guild.emojis)}\nStickers : {len(guild.stickers)}",
            inline=False
        )
        
        embed.add_field(
            name="**__Boost Status__**",
            value=f"Level : {guild.premium_tier} [<:jk_boost:1048568925648064602> {guild.premium_subscription_count} Boosts ]\nBooster Role : <@&{guild.premium_subscriber_role.id}>",
            inline=False
        )       
        embed.add_field(
            name=f"**__Server Roles [ {len(guild.roles)} ]__**",
            value="Too many roles to show here.",
            inline=False
        ) 
        
        if guild.banner is not None:
            embed.set_image(url=guild.banner.url)
        return await ctx.reply(embed=embed)
     
    @commands.hybrid_command(name="userinfo",aliases=["whois","ui"],usage="Userinfo [member]")
    @blacklist_check()   
    @ignore_check()
    async def userinfo(self, ctx: commands.Context, member: discord.Member = None):
      #
      if member == None:
          member = ctx.author
      if member == "":
          member = ctx.author
      bdgs = getbadges(member.id)
        
      badges = ""
      if member.public_flags.hypesquad:
          badges += "Hypesquad"
      elif member.public_flags.hypesquad_balance:
          badges += "<:HypeSquadBalance:1043905789615681556>"       
      elif member.public_flags.hypesquad_bravery:
          badges += "<:HYPERSQUADBRAVERY:1043904845859540992>"
      elif member.public_flags.hypesquad_brilliance:
          badges += "<:emoji_129:1043860600876433458>"
      if member.public_flags.early_supporter:
          badges += "<a:earlysup:1003952039807696937>"
      if member.public_flags.active_developer:
          badges += "<:active_dev:1040559350034473000>"        
      if member.public_flags.verified_bot_developer:
          badges += "<:BotDev:1043865866204364901>"
      if badges == "":
          badges = "None" 



      bannerUser = await self.bot.fetch_user(member.id)


      kp = ""
      if member.guild_permissions.kick_members:
          kp += "Kick Members, "
      if member.guild_permissions.ban_members:
          kp += "Ban Members, "
      if member.guild_permissions.administrator:
          kp += "Administrator, "
      if member.guild_permissions.manage_channels:
          kp += "Manage Channels, "
  #    if member.guild_permissions.manage_server:
  #        kp = "Manage Server"
      if member.guild_permissions.manage_messages:
          kp += "Manage Messages, "
      if member.guild_permissions.mention_everyone:
          kp += "Mention Everyone, "
      if member.guild_permissions.manage_nicknames:
          kp += "Manage Nicknames, "
      if member.guild_permissions.manage_roles:
          kp += "Manage Roles, "
      if member.guild_permissions.manage_webhooks:
          kp += "Manage Webhooks, "
      if member.guild_permissions.manage_emojis:
          kp += "Manage Emojis"

      if kp == "":
          kp = "None"
      


      if member == ctx.guild.owner:
          heck = "Server Owner"
      elif member.guild_permissions.administrator:
          heck = "Server Admin"     
      elif member.guild_permissions.ban_members or member.guild_permissions.kick_members:
          heck = "Server Moderator"
      else:
          heck = "Server Member"
############################
      if member.public_flags.early_supporter:
          badge = "<a:earlysup:1003952039807696937>"
      elif member.public_flags.active_developer:
          badge = "<:active_dev:1040559350034473000>"
        
      elif member.public_flags.verified_bot_developer:
          badge = "<:BotDev:1043865866204364901>"
      else:
          badge = ""  
      if badge is None:
          badge ="None"

      
      if member.bot:
          bot = "True"
      else:
          bot = "False" 
    
        ######
  #    if badges !=
        
      embed = discord.Embed(color = member.color)
      bannerUser = await self.bot.fetch_user(member.id)
      embed.add_field(name="__**General Information**__", value=f"**Name:** {member.name}#{member.discriminator}\n **Nickname:** {member.display_name}\n **ID**: {member.id}\n **Account Created:** <t:{int(member.created_at.timestamp())}:D>\n **Joined Server On:** <t:{int(member.joined_at.timestamp())}:D>\n **Highest Role:** {member.top_role.mention}\n **User Badges** : {badges}")
      r = (', '.join(role.mention for role in member.roles[1:][::-1]) if len(member.roles) > 1 else 'No Roles.') 
      embed.add_field(name="__**Roles:**__", value=r if len(r) <= 1024 else r[0:1006] + ' and more...',inline=False)
        
      embed.add_field(name="__**Key Permissions**__", value=", ".join([kp]))
      embed.add_field(name="__**Acknowledgements:**__", value=heck)
      if bdgs != []:
          embed.add_field(name="__Bot Badges:__", value=f"\n".join([bdgg for bdgg in bdgs]))
      embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar}")
      embed.timestamp = discord.utils.utcnow()
      embed.set_thumbnail(url=member.avatar)
      if not bannerUser.banner:
        pass
      else:
        embed.set_image(url=bannerUser.banner) 
      embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
      await ctx.send(embed=embed)


    @commands.hybrid_command(name="roleinfo",help="Shows you all information about a role.",usage="Roleinfo <role>")
    @blacklist_check()   
    @ignore_check()
    async def roleinfo(self, ctx: commands.Context, *, role: discord.Role):
        """Get information about a role"""
        content = discord.Embed(title=f"@{role.name} | #{role.id}")

        content.colour = role.color

        if isinstance(role.icon, discord.Asset):
            content.set_thumbnail(url=role.icon.url)
        elif isinstance(role.icon, str):
            content.title = f"{role.icon} @{role.name} | #{role.id}"

        content.add_field(name="Color", value=str(role.color).upper())
        content.add_field(name="Member count", value=len(role.members))
        content.add_field(name="Created at", value=role.created_at.strftime("%d/%m/%Y %H:%M"))
        content.add_field(name="Hoisted", value=str(role.hoist))
        content.add_field(name="Mentionable", value=role.mentionable)
        content.add_field(name="Mention", value=role.mention)
        if role.managed:
            if role.tags.is_bot_managed():
                manager = ctx.guild.get_member(role.tags.bot_id)
            elif role.tags.is_integration():
                manager = ctx.guild.get_member(role.tags.integration_id)
            elif role.tags.is_premium_subscriber():
                manager = "Server boosting"
            else:
                manager = "UNKNOWN"
            content.add_field(name="Managed by", value=manager)

        perms = []
        for perm, allow in iter(role.permissions):
            if allow:
                perms.append(f"`{perm.upper()}`")

        if perms:
            content.add_field(name="Allowed permissions", value=" ".join(perms), inline=False)

        await ctx.send(embed=content)



    @blacklist_check()   
    @ignore_check()
    @commands.command(name="status",
                      description="Shows users status",
                      usage="status <member>")
    async def status(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author

        status = member.status
        if status == discord.Status.offline:
            status_location = "Not Applicable"
        elif member.mobile_status != discord.Status.offline:
            status_location = "Mobile"
        elif member.web_status != discord.Status.offline:
            status_location = "Browser"
        elif member.desktop_status != discord.Status.offline:
            status_location = "Desktop"
        else:
            status_location = "Not Applicable"
        await ctx.send(embed=discord.Embed(title="**<a:zOR_lulladance:1002196227229761566> | status**",
                                           description="`%s`: `%s`" %
                                           (status_location, status),
                                           color=0x01f5b6))

    @commands.command(name="emoji",
                      help="Shows emoji syntax",
                      usage="emoji <emoji>")
    @blacklist_check()   
    @ignore_check()
    async def emoji(self, ctx, emoji: discord.Emoji):
        return await ctx.send(
            embed=discord.Embed(title="**<a:zOR_lulladance:1002196227229761566> | emoji**",
                                description="emoji: %s\nid: **`%s`**" %
                                (emoji, emoji.id),
                                color=0x01f5b6))

    @commands.command(name="user",
                      help="Shows user syntax",
                      usage="user [user]")
    @blacklist_check()   
    @ignore_check()
    async def user(self, ctx, user: discord.Member = None):
        return await ctx.send(
            embed=discord.Embed(title="user",
                                description="user: %s\nid: **`%s`**" %
                                (user.mention, user.id),
                                color=0x01f5b6))


    @commands.command(name="channel",
                      help="Shows channel syntax",
                      usage="channel <channel>")
    @blacklist_check()   
    @ignore_check()
    async def channel(self, ctx, channel: discord.TextChannel):
        return await ctx.send(
            embed=discord.Embed(title="channel",
                                description="channel: %s\nid: **`%s`**" %
                                (channel.mention, channel.id),
                                color=0x01f5b6))

    @commands.command(name="boostcount",
                      help="Shows boosts count",
                      usage="boosts",
                      aliases=["bc"])
    @blacklist_check()   
    @ignore_check()
    async def boosts(self, ctx):
        await ctx.send(
            embed=discord.Embed(title=f"Boosts Count Of {ctx.guild.name}",
                                description="**`%s`**" %
                                (ctx.guild.premium_subscription_count),
                                color=0x01f5b6))


    @commands.hybrid_group(name="list",invoke_without_command=True)
    @blacklist_check()   
    @ignore_check()
    async def __list_(self, ctx: commands.Context):
      if ctx.subcommand_passed is None:
          await ctx.send_help(ctx.command)
          ctx.command.reset_cooldown(ctx)
        

    @__list_.command(name="boosters", aliases=["boost", "booster"],usage="List boosters",help="ᗣ See a list of boosters in the server.")
    @blacklist_check()   
    @ignore_check()
    async def list_boost(self, ctx):
      guild = ctx.guild
      entries = [f"`[{no}]` | [{mem}](https://discord.com/users/{mem.id}) [{mem.mention}] - <t:{round(mem.premium_since.timestamp())}:R>" for no, mem in enumerate(guild.premium_subscribers, start=1)]
      paginator = Paginator(
        source=DescriptionEmbedPaginator(
          entries=entries,
          title=f"List of Boosters in {guild.name} - {len(guild.premium_subscribers)}",
          description="",
          per_page=10
        ),
        ctx=ctx
      )
      await paginator.paginate()

    
    @__list_.command(name="inrole", aliases=["inside-role"],help="ᗣ See a list of members that are in the specified role .")
    @blacklist_check()   
    @ignore_check()
    async def list_inrole(self, ctx, role: discord.Role):
      guild = ctx.guild
      entries = [f"`[{no}]` | [{mem}](https://discord.com/users/{mem.id}) [{mem.mention}] - <t:{int(mem.created_at.timestamp())}:D>" for no, mem in enumerate(role.members, start=1)]
      paginator = Paginator(
        source=DescriptionEmbedPaginator(
          entries=entries,
          title=f"List of Members in {role} - {len(role.members)}",
          description="",
          per_page=10
        ),
        ctx=ctx
      )
      await paginator.paginate()



    @__list_.command(name="emojis", aliases=["emoji"],help="Shows you all emojis in the server with ids")
    @blacklist_check()   
    @ignore_check()
    async def list_emojis(self, ctx):
      guild = ctx.guild
      entries = [f"`[{no}]` | {e} - `{e}`" for no, e in enumerate(ctx.guild.emojis, start=1)]
      paginator = Paginator(
        source=DescriptionEmbedPaginator(
          entries=entries,
          title=f"List of Emojis in {guild.name} - {len(ctx.guild.emojis)}",
          description="",
          per_page=10
        ),
        ctx=ctx
      )
      await paginator.paginate()


  
    @__list_.command(name="bots", aliases=["bot"],help="Get a list of All Bots in a server .")
    @blacklist_check()   
    @ignore_check()
    async def list_bots(self, ctx):
      guild = ctx.guild
      people = filter(lambda member: member.bot, ctx.guild.members)
      people = sorted(people, key=lambda member: member.joined_at)
      entries = [f"`[{no}]` | [{mem}](https://discord.com/users/{mem.id}) [{mem.mention}]" for no, mem in enumerate(people, start=1)]
      paginator = Paginator(
        source=DescriptionEmbedPaginator(
          entries=entries,
          title=f"Bots in {guild.name} - {len(people)}",
          description="",
          per_page=10
        ),
        ctx=ctx
      )
      await paginator.paginate()
      

    @__list_.command(name="admins", aliases=["admin"],help="Get a list of All Admins of a server .")
    @blacklist_check()   
    @ignore_check()
    async def list_admin(self, ctx):
      hackers = ([hacker for hacker in ctx.guild.members if hacker.guild_permissions.administrator])
      hackers = sorted(hackers, key=lambda hacker: hacker.joined_at)
      admins= len([hacker for hacker in ctx.guild.members if hacker.guild_permissions.administrator])
      guild = ctx.guild
      entries = [f"`[{no}]` | [{mem}](https://discord.com/users/{mem.id}) [{mem.mention}] - <t:{int(mem.created_at.timestamp())}:D>" for no, mem in enumerate(hackers, start=1)]
      paginator = Paginator(
        source=DescriptionEmbedPaginator(
          entries=entries,
          title=f"Admins in {guild.name} - {admins}",
          description="",
          per_page=10
        ),
        ctx=ctx
      )
      await paginator.paginate()

      
    @__list_.command(name="invoice", aliases=["invc"])
    @blacklist_check()   
    @ignore_check()
    async def listusers(self, ctx):
        if not ctx.author.voice:
            return await ctx.send("You are not connected to a voice channel")
        members = ctx.author.voice.channel.members
        entries = [f"`[{n}]` | {member} [{member.mention}]" for n, member in enumerate(members, start=1)]
        paginator = Paginator(
          source=DescriptionEmbedPaginator(
            entries=entries,
            description="",
            title=f"Voice List of {ctx.author.voice.channel.name} - {len(members)}",
            color=0x2f3136
          ),
          ctx=ctx
        )
        await paginator.paginate()


      
    @__list_.command(name="moderators", aliases=["mods"])
    @blacklist_check()   
    @ignore_check()
    async def list_mod(self, ctx):
      hackers = ([hacker for hacker in ctx.guild.members if hacker.guild_permissions.ban_members or hacker.guild_permissions.kick_members])
      hackers = sorted(hackers, key=lambda hacker: hacker.joined_at)
      admins= len([hacker for hacker in ctx.guild.members if hacker.guild_permissions.ban_members or hacker.guild_permissions.kick_members])
      guild = ctx.guild
      entries = [f"`[{no}]` | [{mem}](https://discord.com/users/{mem.id}) [{mem.mention}] - <t:{int(mem.created_at.timestamp())}:D>" for no, mem in enumerate(hackers, start=1)]
      paginator = Paginator(
        source=DescriptionEmbedPaginator(
          entries=entries,
          title=f"Mods in {guild.name} - {admins}",
          description="",
          per_page=10
        ),
        ctx=ctx
      )
      await paginator.paginate()

    @__list_.command(name="early", aliases=["sup"])
    @blacklist_check()   
    @ignore_check()
    async def list_early(self, ctx):
      hackers = ([hacker for hacker in ctx.guild.members if hacker.public_flags.early_supporter])
      hackers = sorted(hackers, key=lambda hacker: hacker.created_at)
      admins= len([hacker for hacker in ctx.guild.members if hacker.public_flags.early_supporter])
      guild = ctx.guild
      entries = [f"`[{no}]` | [{mem}](https://discord.com/users/{mem.id})  [{mem.mention}] - <t:{int(mem.created_at.timestamp())}:D>" for no, mem in enumerate(hackers, start=1)]
      paginator = Paginator(
        source=DescriptionEmbedPaginator(
          entries=entries,
          title=f"Early Id's in {guild.name} - {admins}",
          description="",
          per_page=10
        ),
        ctx=ctx
      )
      await paginator.paginate()



    @__list_.command(name="activedeveloper", aliases=["activedev"])
    @blacklist_check()   
    @ignore_check()
    async def list_activedeveloper(self, ctx):
      hackers = ([hacker for hacker in ctx.guild.members if hacker.public_flags.active_developer])
      hackers = sorted(hackers, key=lambda hacker: hacker.created_at)
      admins= len([hacker for hacker in ctx.guild.members if hacker.public_flags.active_developer])
      guild = ctx.guild
      entries = [f"`[{no}]` | [{mem}](https://discord.com/users/{mem.id}) [{mem.mention}] - <t:{int(mem.created_at.timestamp())}:D>" for no, mem in enumerate(hackers, start=1)]
      paginator = Paginator(
        source=DescriptionEmbedPaginator(
          entries=entries,
          title=f"Active Developer Id's in {guild.name} - {admins}",
          description="",
          per_page=10
        ),
        ctx=ctx
      )
      await paginator.paginate()

      

    @__list_.command(name="createpos")
    @blacklist_check()   
    @ignore_check()
    async def list_cpos(self, ctx):
      hackers = ([hacker for hacker in ctx.guild.members])
      hackers = sorted(hackers, key=lambda hacker: hacker.created_at)    
      admins= len([hacker for hacker in ctx.guild.members])
      guild = ctx.guild
      entries = [f"`[{no}]` | [{mem}](https://discord.com/users/{mem.id}) - <t:{int(mem.created_at.timestamp())}:D>" for no, mem in enumerate(hackers, start=1)]
      paginator = Paginator(
        source=DescriptionEmbedPaginator(
          entries=entries,
          title=f"Creation every id in {guild.name} - {admins}",
          description="",
          per_page=10
        ),
        ctx=ctx
      )
      await paginator.paginate()



    @__list_.command(name="joinpos")
    @blacklist_check()   
    @ignore_check()
    async def list_joinpos(self, ctx):
      hackers = ([hacker for hacker in ctx.guild.members])
      hackers = sorted(hackers, key=lambda hacker: hacker.joined_at)    
      admins= len([hacker for hacker in ctx.guild.members])
      guild = ctx.guild
      entries = [f"`[{no}]` | [{mem}](https://discord.com/users/{mem.id}) Joined At - <t:{int(mem.joined_at.timestamp())}:D>" for no, mem in enumerate(hackers, start=1)]
      paginator = Paginator(
        source=DescriptionEmbedPaginator(
          entries=entries,
          title=f"Join Position of every user in {guild.name} - {admins}",
          description="",
          per_page=10
        ),
        ctx=ctx
      )
      await paginator.paginate()






  
  
    @commands.hybrid_command(name="steal",
                  help="Adds a emoji",
                      usage="steal <emoji>",
                      aliases=["eadd"])
    @blacklist_check()   
    @ignore_check()

    @commands.has_permissions(manage_emojis=True)
    async def steal(self, ctx, emote):
        try:
            if emote[0] == '<':
                name = emote.split(':')[1]
                emoji_name = emote.split(':')[2][:-1]
                anim = emote.split(':')[0]
                if anim == '<a':
                    url = f'https://cdn.discordapp.com/emojis/{emoji_name}.gif'
                else:
                    url = f'https://cdn.discordapp.com/emojis/{emoji_name}.png'
                try:
                    response = requests.get(url)
                    img = response.content
                    emote = await ctx.guild.create_custom_emoji(name=name,
                                                                image=img)
                    return await ctx.send(
                        embed=discord.Embed(title="emoji-add",
                                            description="added \"**`%s`**\"!" %
                                            (emote),
                                            color=0x01f5b6))
                except Exception:
                    return await ctx.send(
                        embed=discord.Embed(title="emoji-add",
                                            description=f"failed to add emoji",
                                            color=0x01f5b6))
            else:
                return await ctx.send(
                    embed=discord.Embed(title="emoji-add",
                                        description=f"invalid emoji",
                                        color=0x01f5b6))
        except Exception:
            return await ctx.send(
                embed=discord.Embed(title="emoji-add",
                                    description=f"failed to add emoji",
                                    color=0x01f5b6))

    @commands.hybrid_command(name="removeemoji",help="Deletes the emoji from the server",usage="removeemoji <emoji>")
    @blacklist_check()   
    @ignore_check()
    @commands.has_permissions(manage_emojis=True)
    async def removeemoji(self, ctx, emoji: discord.Emoji):
        await emoji.delete()
        await ctx.send(f"**<a:black_astroz:1002204507985432666> emoji has been deleted.**")

    @commands.hybrid_command(name="unbanall",help="Unbans Everyone In The Guild!", aliases=['massunban'],usage="Unbanall")
    @blacklist_check()   
    @ignore_check()
    @commands.cooldown(1, 30, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only() 
    @commands.has_permissions(ban_members=True)
    async def unbanall(self, ctx):
        button = Button(label="Yes", style=discord.ButtonStyle.green, emoji="<:GreenTick:1018174649198202990>")
        button1 = Button(label="No", style=discord.ButtonStyle.red, emoji="<:error:1018174714750976030>")
        async def button_callback(interaction: discord.Interaction):
          a = 0
          if interaction.user == ctx.author:
            if interaction.guild.me.guild_permissions.ban_members:
              await interaction.response.edit_message(content=f"Unbanning All Banned Member(s)", embed=None, view=None)
              async for idk in interaction.guild.bans(limit=None):
                await interaction.guild.unban(user=idk.user, reason="Unbanall Command Executed By: {}".format(ctx.author))
                a += 1
              await interaction.channel.send(content=f"Successfully Unbanned {a} Member(s)")
            else:
              await interaction.response.edit_message(content="I am missing ban members permission.\ntry giving me permissions and retry", embed=None, view=None)
          else: 
            await interaction.response.send_message("This Is Not For You Dummy!", embed=None, view=None, ephemeral=True) 

        async def button1_callback(interaction: discord.Interaction): 
          if interaction.user == ctx.author: 
            await interaction.response.edit_message(content="Ok I will not unban anyone in this guild", embed=None, view=None)
          else:
            await interaction.response.send_message("This Is Not For You Dummy!", embed=None, view=None, ephemeral=True)
        embed = discord.Embed(title='Confirmation',
                          color=0x01f5b6,
                          description=f'**Are you sure you want to unban everyone in this guild?**')
        embed.set_footer(text="Made With 💖 By Eagle[.]#0831")
        
        view = View()
        button.callback = button_callback
        button1.callback = button1_callback
        view.add_item(button)
        view.add_item(button1)
        await ctx.reply(embed=embed, view=view, mention_author=False)






  


    @commands.command(name="joined-at",
                      help="Shows when a user joined",
                      usage="joined-at [user]")
    @blacklist_check()   
    @ignore_check()
    async def joined_at(self, ctx):
        joined = ctx.author.joined_at.strftime("%a, %d %b %Y %I:%M %p")
        await ctx.send(embed=discord.Embed(title="joined-at",
                                           description="**`%s`**" % (joined),
                                            color=0x01f5b6))






    @commands.command(name="github",usage="github [search]")
    @blacklist_check()   
    @ignore_check()
    async def github(self, ctx, *, search_query):
        json = requests.get(
            f"https://api.github.com/search/repositories?q={search_query}"
        ).json()

        if json["total_count"] == 0:
            await ctx.send("No matching repositories found")
        else:
            await ctx.send(
                f"First result for '{search_query}':\n{json['items'][0]['html_url']}")


    @commands.hybrid_command(name="vcinfo",help="get info about voice channel",usage="Vcinfo <VoiceChannel>")
    @blacklist_check()   
    @ignore_check()
    async def vcinfo(self, ctx: Context, vc: discord.VoiceChannel):
      e = discord.Embed(title='VC Information', color=0x01f5b6)
      e.add_field(name='VC name', value=vc.name, inline=False)
      e.add_field(name='VC ID', value=vc.id, inline=False)
      e.add_field(name='VC bitrate', value=vc.bitrate, inline=False)
      e.add_field(name='Mention', value=vc.mention, inline=False)
      e.add_field(name='Category name', value=vc.category.name, inline=False)
      await ctx.send(embed=e)




    @commands.hybrid_command(name="channelinfo",help="shows info about channel",aliases=['channeli', 'cinfo', 'ci'], pass_context=True, no_pm=True,usage="Channelinfo [channel]")
    @blacklist_check()   
    @ignore_check()
    async def channelinfo(self, ctx, *, channel: int = None):
        """Shows channel information"""
        if not channel:
            channel = ctx.message.channel
        else:
            channel = self.bot.get_channel(channel)
        data = discord.Embed()
        if hasattr(channel, 'mention'):
            data.description = "**Information about Channel:** " + channel.mention
        if hasattr(channel, 'changed_roles'):
            if len(channel.changed_roles) > 0:
                data.color = 0x01f5b6 if channel.changed_roles[0].permissions.read_messages else 0x01f5b6
        if isinstance(channel, discord.TextChannel): 
            _type = "Text"
        elif isinstance(channel, discord.VoiceChannel): 
            _type = "Voice"
        else: 
            _type = "Unknown"
        data.add_field(name="Type", value=_type)
        data.add_field(name="ID", value=channel.id, inline=False)
        if hasattr(channel, 'position'):
            data.add_field(name="Position", value=channel.position)
        if isinstance(channel, discord.VoiceChannel):
            if channel.user_limit != 0:
                data.add_field(name="User Number", value="{}/{}".format(len(channel.voice_members), channel.user_limit))
            else:
                data.add_field(name="User Number", value="{}".format(len(channel.voice_members)))
            userlist = [r.display_name for r in channel.members]
            if not userlist:
                userlist = "None"
            else:
                userlist = "\n".join(userlist)
            data.add_field(name="Users", value=userlist)
            data.add_field(name="Bitrate", value=channel.bitrate)
        elif isinstance(channel, discord.TextChannel):
            try:
                pins = await channel.pins()
                data.add_field(name="Pins", value=len(pins), inline=True)
            except discord.Forbidden:
                pass
            data.add_field(name="Members", value="%s"%len(channel.members))
            if channel.topic:
                data.add_field(name="Topic", value=channel.topic, inline=False)
            hidden = []
            allowed = []
            for role in channel.changed_roles:
                if role.permissions.read_messages is True:
                    if role.name != "@everyone":
                        allowed.append(role.mention)
                elif role.permissions.read_messages is False:
                    if role.name != "@everyone":
                        hidden.append(role.mention)
            if len(allowed) > 0: 
                data.add_field(name='Allowed Roles ({})'.format(len(allowed)), value=', '.join(allowed), inline=False)
            if len(hidden) > 0:
                data.add_field(name='Restricted Roles ({})'.format(len(hidden)), value=', '.join(hidden), inline=False)
        if channel.created_at:
            data.set_footer(text=("Created on {} ({} days ago)".format(channel.created_at.strftime("%d %b %Y %H:%M"), (ctx.message.created_at - channel.created_at).days)))
        await ctx.send(embed=data)



    @commands.command(name="note",help="Creates a note for you",usage="Note <message>")
    @cooldown(1, 10, BucketType.user)
    @blacklist_check()   
    @ignore_check()
    async def note(self, ctx, *, message):
        message = str(message)
        print(message)
        stats = await notedb.find_one({"id": ctx.author.id})
        if len(message) <= 50:
            #
            if stats is None:
                newuser = {"id": ctx.author.id, "note": message}
                await notedb.insert_one(newuser)
                await ctx.send("**Your note has been stored**")
                await ctx.message.delete()

            else:
                x = notedb.find({"id": ctx.author.id})
                z = 0
                async for i in x:
                    z += 1
                if z > 2:
                    await ctx.send("**You cannot add more than 3 notes**")
                else:
                    newuser = {"id": ctx.author.id, "note": message}
                    await notedb.insert_one(newuser)
                    await ctx.send("**Yout note has been stored**")
                    await ctx.message.delete()

        else:
            await ctx.send("**Message cannot be greater then 50 characters**")

    @commands.command(name="notes",help="Shows your note",usage="Notes")
    @blacklist_check()   
    @ignore_check()
    async def notes(self, ctx):
        stats = await notedb.find_one({"id": ctx.author.id})
        if stats is None:
            embed = discord.Embed(
                timestamp=ctx.message.created_at,
                title="Notes",
                description=f"{ctx.author.mention} has no notes",
                color=0x01f5b6,
            )
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(
                title="Notes", description=f"Here are your notes", color=0x01f5b6
            )
            x = notedb.find({"id": ctx.author.id})
            z = 1
            async for i in x:
                msg = i["note"]
                embed.add_field(name=f"Note {z}", value=f"{msg}", inline=False)
                z += 1
            await ctx.send(embed=embed)
          #  await ctx.send("**Please check your private messages to see your notes**")

    @commands.command(name="trashnotes",help="Delete the notes , it's a good practice",usage="Trashnotes")
    @blacklist_check()   
    @ignore_check()
    async def trashnotes(self, ctx):
        try:
            await notedb.delete_many({"id": ctx.author.id})
            await ctx.send("**Your notes have been deleted , thank you**")
        except:
            await ctx.send("**You have no record**")








    @commands.hybrid_command(name="badges", help="Check what premium badges a user have.", aliases=["badge","profile","pr"],usage="Badges [user]")
    @blacklist_check()   
    @ignore_check()
    async def _badges(self, ctx, user: Optional[discord.User] = None):
      hasan = await self.bot.fetch_user(301502732664307716)
      mem = user or ctx.author
      bdgs = getbadges(mem.id)
      badges = ""
      if mem.public_flags.hypesquad:
          badges += "Hypesquad\n"
      elif mem.public_flags.hypesquad_balance:
          badges += "<:HypeSquadBalance:1043905789615681556> *HypeSquad Balance*\n"
       
      elif mem.public_flags.hypesquad_bravery:
          badges += "<:HYPERSQUADBRAVERY:1043904845859540992> *HypeSquad Bravery*\n"
      elif mem.public_flags.hypesquad_brilliance:
          badges += "<:emoji_129:1043860600876433458> *Hypesquad Brilliance*\n"          
      if mem.public_flags.early_supporter:
          badges += "<a:earlysup:1003952039807696937> *Early Supporter*\n"        
      elif mem.public_flags.verified_bot_developer:
          badges += "<:activedev:1044968012932976750> *Verified Bot Developer*\n"
      elif mem.public_flags.active_developer:
          badges += "<:active_dev:1040559350034473000> *Active Developer*\n"
      if badges == "":
          badges = "None" 
      if bdgs == []:
        embed2 = discord.Embed(color=0x01f5b6)
        embed2.add_field(name="**User Badges:**", value=f"{badges}")
        embed2.add_field(name="**Bot Badges:**", value="<:jk_cut_stolen_emoji:1053893879105081344> NO BADGES")
        embed2.set_author(name=f"{mem}",icon_url=mem.avatar.url if mem.avatar else mem.default_avatar.url)
        embed2.set_thumbnail(url=mem.avatar.url if mem.avatar else mem.default_avatar.url)  
        await ctx.reply(embed=embed2, mention_author=False)
      else:
        embed = discord.Embed(color=0x01f5b6)
        embed.add_field(name="**User Badges:**", value=f"{badges}")
        embed.add_field(name="**Bot Badges:**", value="\n".join([bdg for bdg in bdgs]))
        embed.set_author(name=f"{mem}",icon_url=mem.avatar.url if mem.avatar else mem.default_avatar.url)
        embed.set_thumbnail(url=mem.avatar.url if mem.avatar else mem.default_avatar.url)
        await ctx.reply(embed=embed, mention_author=False)
        
        
        




    @commands.hybrid_command(name="ping",aliases=["latency"],usage="Checks the bot latency .")
    async def ping(self,ctx):
      embed = discord.Embed(title="Ping",description=f"```My Ping Is {int(self.bot.latency * 1000)} ms```",color=0x01f5b6) 
      embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
      embed.set_thumbnail(url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
      embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
      await ctx.reply(embed=embed) 