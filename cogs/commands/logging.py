import discord
from discord.ext import commands
import datetime
from typing import Union
from utils.Tools import *






class Logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    guild_channels = Union[
        discord.TextChannel, discord.VoiceChannel, discord.CategoryChannel
    ]



    @commands.group(name="logall", invoke_without_command=True)
    @blacklist_check()   
    @ignore_check()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _logging(self, ctx):
      if ctx.subcommand_passed is None:
          await ctx.send_help(ctx.command)
          ctx.command.reset_cooldown(ctx)   

            
    @_logging.command(name="disable")
    @blacklist_check()   
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _disable(self, ctx, channel: discord.TextChannel):
        data = loggingDB(ctx.guild.id)
        chh = data["logging"]["channel"]
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            if len(chh) == 0:
                hacker = discord.Embed(color=0x01f5b6,description=f"<a:error:1002226340516331571> | This server dont have any logall channel setupped yet .", timestamp=ctx.message.created_at)
                hacker.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
                await ctx.send(embed=hacker)
            else:
                if str(channel.id) not in chh:
                    hacker1 = discord.Embed(color=0x01f5b6,description=f"<a:error:1002226340516331571> | This channel is not in the logall channels list .", timestamp=ctx.message.created_at)
                    hacker1.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
                    await ctx.send(embed=hacker1)
                else:
                    chh.remove(str(channel.id))
                    updateDB(ctx.guild.id, data)
                    hacker3 = discord.Embed(color=0x01f5b6,description=f"<:GreenTick:1029990379623292938> | Successfully removed {channel.mention} from logall channel list .", timestamp=ctx.message.created_at)
                    hacker3.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")    
                    await ctx.send(embed=hacker3)
        else:
          hacker5 = discord.Embed(description="""```diff
 - You must have Administrator permission. - Your top role should be above my top role. 
```""",color=0x01f5b6)
          hacker5.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
          
          await ctx.send(embed=hacker5)          
          
    @_logging.command(name="enable", help="Enables all the log in the given channel .")
    @blacklist_check()   
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _logging_enable(self, ctx, channel: discord.TextChannel):
        data = loggingDB(ctx.guild.id)
        chh = data["logging"]["channel"]
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            if len(chh) == 3:
                hacker = discord.Embed(color=0x01f5b6,description=f"<a:error:1002226340516331571> | You have reached maximum channel limit for logging channel which is one .", timestamp=ctx.message.created_at)
                hacker.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
                await ctx.send(embed=hacker)
            else:
                if str(channel.id) in chh:
                    hacker1 = discord.Embed(color=0x01f5b6,description=f"<a:error:1002226340516331571> | This channel is already in the logging channels list .", timestamp=ctx.message.created_at)
                    hacker1.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
                    await ctx.send(embed=hacker1)
                else:
                    chh.append(str(channel.id))
                    updatelog(ctx.guild.id, data)
                    hacker4 = discord.Embed(color=0x01f5b6,description=f"<:GreenTick:1029990379623292938> | Successfully added {channel.mention} to logging channel list .", timestamp=ctx.message.created_at)
                    hacker4.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")                     
                    await ctx.send(embed=hacker4)
        else:
          hacker5 = discord.Embed(description="""```diff
 - You must have Administrator permission. - Your top role should be above my top role. 
```""",color=0x01f5b6)
          hacker5.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
          
          await ctx.send(embed=hacker5)    


    @commands.command(name="msglogs")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _msglog(self, ctx, channel: discord.TextChannel):
        data = loggingDB(ctx.guild.id)
        chh = data["logging"]["msglog"]
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            if len(chh) == 3:
                hacker = discord.Embed(color=0x01f5b6,description=f"<a:error:1002226340516331571> | You have reached maximum channel limit for messagelogs channel which is three .", timestamp=ctx.message.created_at)
                hacker.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
                await ctx.send(embed=hacker)
            else:
                if str(channel.id) in chh:
                    hacker1 = discord.Embed(color=0x01f5b6,description=f"<a:error:1002226340516331571> | This channel is already in the message logging channels list .", timestamp=ctx.message.created_at)
                    hacker1.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
                    await ctx.send(embed=hacker1)
                else:
                    chh.append(str(channel.id))
                    updatelog(ctx.guild.id, data)
                    hacker4 = discord.Embed(color=0x01f5b6,description=f"<:GreenTick:1029990379623292938> | Successfully added {channel.mention} to message logging channel list .", timestamp=ctx.message.created_at)
                    hacker4.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")                     
                    await ctx.send(embed=hacker4)
        else:
          hacker5 = discord.Embed(description="""```diff
 - You must have Administrator permission. - Your top role should be above my top role. 
```""",color=0x01f5b6)
          hacker5.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
          
          await ctx.send(embed=hacker5) 


    @commands.command(name="memberlogs")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _memberlogs(self, ctx, channel: discord.TextChannel):
        data = loggingDB(ctx.guild.id)
        chh = data["logging"]["memberlog"]
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            if len(chh) == 3:
                hacker = discord.Embed(color=0x01f5b6,description=f"<a:error:1002226340516331571> | You have reached maximum channel limit for memberlogs channel which is three .", timestamp=ctx.message.created_at)
                hacker.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
                await ctx.send(embed=hacker)
            else:
                if str(channel.id) in chh:
                    hacker1 = discord.Embed(color=0x01f5b6,description=f"<a:error:1002226340516331571> | This channel is already in the memberlogs channels list .", timestamp=ctx.message.created_at)
                    hacker1.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
                    await ctx.send(embed=hacker1)
                else:
                    chh.append(str(channel.id))
                    updatelog(ctx.guild.id, data)
                    hacker4 = discord.Embed(color=0x01f5b6,description=f"<:GreenTick:1029990379623292938> | Successfully added {channel.mention} to memberlogs channel list .", timestamp=ctx.message.created_at)
                    hacker4.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")                     
                    await ctx.send(embed=hacker4)
        else:
          hacker5 = discord.Embed(description="""```diff
 - You must have Administrator permission. - Your top role should be above my top role. 
```""",color=0x01f5b6)
          hacker5.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
          
          await ctx.send(embed=hacker5) 



    @commands.command(name="serverlogs")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _serverlogs(self, ctx, channel: discord.TextChannel):
        data = loggingDB(ctx.guild.id)
        chh = data["logging"]["serverlog"]
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            if len(chh) == 3:
                hacker = discord.Embed(color=0x01f5b6,description=f"<a:error:1002226340516331571> | You have reached maximum channel limit for serverlogs channel which is three .", timestamp=ctx.message.created_at)
                hacker.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
                await ctx.send(embed=hacker)
            else:
                if str(channel.id) in chh:
                    hacker1 = discord.Embed(color=0x01f5b6,description=f"<a:error:1002226340516331571> | This channel is already in the serverlogs channels list .", timestamp=ctx.message.created_at)
                    hacker1.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
                    await ctx.send(embed=hacker1)
                else:
                    chh.append(str(channel.id))
                    updatelog(ctx.guild.id, data)
                    hacker4 = discord.Embed(color=0x01f5b6,description=f"<:GreenTick:1029990379623292938> | Successfully added {channel.mention} to serverlogs channel list .", timestamp=ctx.message.created_at)
                    hacker4.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")                     
                    await ctx.send(embed=hacker4)
        else:
          hacker5 = discord.Embed(description="""```diff
 - You must have Administrator permission. - Your top role should be above my top role. 
```""",color=0x01f5b6)
          hacker5.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
          
          await ctx.send(embed=hacker5) 

    @commands.command(name="rolelogs")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _rolelogs(self, ctx, channel: discord.TextChannel):
        data = loggingDB(ctx.guild.id)
        chh = data["logging"]["rolelog"]
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            if len(chh) == 3:
                hacker = discord.Embed(color=0x01f5b6,description=f"<a:error:1002226340516331571> | You have reached maximum channel limit for rolelogs channel which is three .", timestamp=ctx.message.created_at)
                hacker.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
                await ctx.send(embed=hacker)
            else:
                if str(channel.id) in chh:
                    hacker1 = discord.Embed(color=0x01f5b6,description=f"<a:error:1002226340516331571> | This channel is already in the rolelogs channels list .", timestamp=ctx.message.created_at)
                    hacker1.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
                    await ctx.send(embed=hacker1)
                else:
                    chh.append(str(channel.id))
                    updatelog(ctx.guild.id, data)
                    hacker4 = discord.Embed(color=0x01f5b6,description=f"<:GreenTick:1029990379623292938> | Successfully added {channel.mention} to rolelogs channel list .", timestamp=ctx.message.created_at)
                    hacker4.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")                     
                    await ctx.send(embed=hacker4)
        else:
          hacker5 = discord.Embed(description="""```diff
 - You must have Administrator permission. - Your top role should be above my top role. 
```""",color=0x01f5b6)
          hacker5.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
          
          await ctx.send(embed=hacker5)     


    @commands.command(name="channellogs")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _channellogs(self, ctx, channel: discord.TextChannel):
        data = loggingDB(ctx.guild.id)
        chh = data["logging"]["channellog"]
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            if len(chh) == 3:
                hacker = discord.Embed(color=0x01f5b6,description=f"<a:error:1002226340516331571> | You have reached maximum channel limit for channellogs channel which is three .", timestamp=ctx.message.created_at)
                hacker.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
                await ctx.send(embed=hacker)
            else:
                if str(channel.id) in chh:
                    hacker1 = discord.Embed(color=0x01f5b6,description=f"<a:error:1002226340516331571> | This channel is already in the channellogs channels list .", timestamp=ctx.message.created_at)
                    hacker1.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
                    await ctx.send(embed=hacker1)
                else:
                    chh.append(str(channel.id))
                    updatelog(ctx.guild.id, data)
                    hacker4 = discord.Embed(color=0x01f5b6,description=f"<:GreenTick:1029990379623292938> | Successfully added {channel.mention} to channellogs channel list .", timestamp=ctx.message.created_at)
                    hacker4.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")                     
                    await ctx.send(embed=hacker4)
        else:
          hacker5 = discord.Embed(description="""```diff
 - You must have Administrator permission. - Your top role should be above my top role. 
```""",color=0x01f5b6)
          hacker5.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")          
          await ctx.send(embed=hacker5) 


    @commands.command(name="voicelogs")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _voicelogs(self, ctx, channel: discord.TextChannel):
        data = loggingDB(ctx.guild.id)
        chh = data["logging"]["voicelog"]
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            if len(chh) == 3:
                hacker = discord.Embed(color=0x01f5b6,description=f"<a:error:1002226340516331571> | You have reached maximum channel limit for voicelogs channel which is three .", timestamp=ctx.message.created_at)
                hacker.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
                await ctx.send(embed=hacker)
            else:
                if str(channel.id) in chh:
                    hacker1 = discord.Embed(color=0x01f5b6,description=f"<a:error:1002226340516331571> | This channel is already in the voicelogs channels list .", timestamp=ctx.message.created_at)
                    hacker1.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
                    await ctx.send(embed=hacker1)
                else:
                    chh.append(str(channel.id))
                    updatelog(ctx.guild.id, data)
                    hacker4 = discord.Embed(color=0x01f5b6,description=f"<:GreenTick:1029990379623292938> | Successfully added {channel.mention} to voicelogs channel list .", timestamp=ctx.message.created_at)
                    hacker4.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")                     
                    await ctx.send(embed=hacker4)
        else:
          hacker5 = discord.Embed(description="""```diff
 - You must have Administrator permission. - Your top role should be above my top role. 
```""",color=0x01f5b6)
          hacker5.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
          
          await ctx.send(embed=hacker5) 

            
    @commands.Cog.listener(name="on_guild_channel_delete")  
    async def logs_channel_delete(self, channel: guild_channels):
        data = loggingDB(channel.guild.id)
        chnl = list(data["logging"]["channel"])
        hacker = list(data["logging"]["channellog"])
        logall =  data["logging"]["logall"]
        async for log in channel.guild.audit_logs(
            action=discord.AuditLogAction.channel_delete, limit=1
        ):
            user = f"**Deleted By:** `{log.user}`\n"
        hacker = discord.Embed(title=f"{channel.type} Channel Deleted",description=f"{channel.type} Channel {channel.name} Deleted By {log.user}", color=0x01f5b6)
        hacker.set_author(name=f"{log.user}", icon_url=log.user.display_avatar.url)
        hacker.add_field(name="Name",
                    value=f"{channel.name}",
                    inline=False)
        hacker.add_field(name="Category",
                    value=f"{channel.category}",
                    inline=False)
        hacker.add_field(name="Position",
                    value=f"{channel.position}",
                    inline=False)
        hacker.set_thumbnail( url=log.user.display_avatar.url)
        hacker.set_footer(text="DELETED", icon_url=self.bot.user.display_avatar.url)
        hacker.timestamp = discord.utils.utcnow()
        for chh in chnl:
            ch = self.bot.get_channel(int(chh))
            await ch.send(embed=hacker)






    

    @commands.Cog.listener(name="on_guild_channel_create") 
    async def logs_channel_create(self, channel: guild_channels):
        data = loggingDB(channel.guild.id)
        chnl = list(data["logging"]["channel"])
        hacker = list(data["logging"]["channellog"])
        logall =  data["logging"]["logall"]
        async for log in channel.guild.audit_logs(
            action=discord.AuditLogAction.channel_create, limit=1
        ):       
         hacker = discord.Embed(title=f"{channel.type} Created By {log.user}",description=f"""{channel.type} Channel {channel.mention} Created By {log.user}""", color=0x01f5b6)
        hacker.add_field(name="Name",
                    value=f"{channel.name}",
                    inline=False)
        hacker.add_field(name="Category",
                    value=f"{channel.category}",
                    inline=False)
        hacker.add_field(name="Mention",
                    value=f"{channel.mention}",
                    inline=False)
        hacker.add_field(name="Position",
                    value=f"{channel.position}",
                    inline=False)
        hacker.add_field(name="Channel Type",
                    value=f"{channel.name}",
                    inline=False)

        hacker.set_author(name=log.user, icon_url=log.user.display_avatar.url)
        hacker.set_thumbnail( url=log.user.display_avatar.url)
        hacker.set_footer(text="CREATED", icon_url=self.bot.user.display_avatar.url)
        hacker.timestamp = discord.utils.utcnow()
        for chh in chnl:
            ch = self.bot.get_channel(int(chh))
            await ch.send(embed=hacker)

                



    @commands.Cog.listener(name="on_guild_update")
    async def logs_guild_update(self, before: discord.Guild, after: discord.Guild):
        data = loggingDB(after.guild.id)
        chnl = list(data["logging"]["channel"])
        hacker = list(data["logging"]["serverlog"])
        logall =  data["logging"]["logall"]
        async for log in after.audit_logs(
            limit=1, action=discord.AuditLogAction.guild_update
        ):
            user = f"**Updated By:** `{log.user}`"
        if before.icon != after.icon:
            if not after.icon:
                msg = {"title": "Server Icon Removed | Log", "description": user}
            else:
                msg = {
                    "title": "Server Icon Updated | Log",
                    "description": user,
                    "thumbnail": f"{self.bot.try_asset(after.icon)}",
                }
        elif before.banner != after.banner:
            if not after.banner:
                msg = {"title": "Server Banner Removed | Log", "description": user}
            else:
                msg = {
                    "title": "Server Banner Updated | Log",
                    "description": user,
                    "thumbnail": f"{self.bot.try_asset(after.banner)}",
                }
        elif before.name != after.name:
            msg = {
                "title": "Server Name Updated | Log",
                "description": f"**Before:** `{before.name}`\n**After:** `{after.name}`\n{user}",
            }
        elif before.owner != after.owner:
            msg = {
                "title": "Server Owner Updated | Log",
                "description": f"**Before:** `{before.owner}`\n**After:** `{after.owner}`",
            }
        if msg:
            hacker = discord.Embed(color=0x01f5b6,
                title=msg.get("title"),
                description=msg.get("description")
            )
            hacker.set_author(name=log.user, icon_url=log.user.display_avatar.url)
            hacker.set_thumbnail( url=log.user.display_avatar.url)
            hacker.set_footer(text="UPDATED", icon_url=self.bot.user.display_avatar.url)
            hacker.timestamp = discord.utils.utcnow()
            for chh in chnl:
                ch = self.bot.get_channel(int(chh))
            await ch.send(embed=hacker)
          
            
            
            
    @commands.Cog.listener(name="on_member_join")  
    async def logs_member_join(self, member: discord.Member):
        data = loggingDB(member.guild.id)
        chnl = list(data["logging"]["channel"])
        hacker = list(data["logging"]["memberlog"])
        logall =  data["logging"]["logall"]
        if member.bot:
            check_bot = "Bot"
        else:
            check_bot = "Member"
        hacker = discord.Embed(title=f"A {check_bot} joined the server", color=0x01f5b6)
        hacker.add_field(name="Username",
                    value=f"{member.name}",
                    inline=False)
        hacker.add_field(name="Id",
                    value=f"{member.id}",
                    inline=False)
        hacker.add_field(name="Account created at",
                    value=f"<t:{int(member.created_at.timestamp())}:F>",
                    inline=False)
        hacker.add_field(name="Joined at",
                    value=f"<t:{int(member.joined_at.timestamp())}:F>",
                    inline=False)
        if member.bot:
          async for log in member.guild.audit_logs(
              limit=1, action=discord.AuditLogAction.bot_add
          ):
           hacker.add_field(name="Added by", value=log.user)
        else:
            pass
        hacker.set_author(name=member, icon_url=member.avatar.url if member.avatar else member.default_avatar.url)
        hacker.set_thumbnail( url=member.avatar.url if member.avatar else member.default_avatar.url)
        hacker.set_footer(text="JOINED", icon_url=self.bot.user.display_avatar.url)
        hacker.timestamp = discord.utils.utcnow()
        for chh in chnl:
            ch = self.bot.get_channel(int(chh))
            await ch.send(embed=hacker)

        
    @commands.Cog.listener(name="on_member_remove")  
    async def logs_member_remove(self, member: discord.Member):
        data = loggingDB(member.guild.id)
        chnl = list(data["logging"]["channel"])
        hacker = list(data["logging"]["memberlog"])
        logall =  data["logging"]["logall"]
        async for log in member.guild.audit_logs(
            limit=1, action=discord.AuditLogAction.ban
        ):
         hacker = discord.Embed(title="A member left the server", color=0x01f5b6)
        hacker.add_field(name="Username",
                    value=f"{member.name}",
                    inline=False)
        hacker.add_field(name="Id",
                    value=f"{member.id}",
                    inline=False)
        hacker.add_field(name="Account created at",
                    value=f"<t:{int(member.created_at.timestamp())}:F>",
                    inline=False)
        hacker.set_author(name=member, icon_url=member.avatar.url if member.avatar else member.default_avatar.url)
        hacker.set_thumbnail( url=member.avatar.url if member.avatar else member.default_avatar.url)
        hacker.set_footer(text="LEFT", icon_url=self.bot.user.display_avatar.url)
        hacker.timestamp = discord.utils.utcnow()
        for chh in chnl:
            ch = self.bot.get_channel(int(chh))
            await ch.send(embed=hacker)

        
        
        
        
        
        


    @commands.Cog.listener(name="on_member_update")  
    async def logs_member_update(self, before: discord.Member, after: discord.Member):
        data = loggingDB(before.guild.id)
        chnl = list(data["logging"]["channel"])
        hacker = list(data["logging"]["memberlog"])
        logall =  data["logging"]["logall"]
        msg = None
        if before.guild_avatar != after.guild_avatar:
            if not after.guild_avatar:
                msg = {
                    "title": "Member Server Avatar Removed | Log",
                    "description": f"**User:** {after}",
                    "thumbnail": self.bot.try_asset(
                        after.display_avatar, after.default_avatar
                    ),
                }
            else:
                msg = {
                    "title": "Member Server Avatar Updated | Log",
                    "description": f"**User:** {after}",
                    "thumbnail": self.bot.try_asset(
                        after.guild_avatar, after.display_avatar
                    ),
                }
        elif before.nick != after.nick:
            time = self.bot.time(
                datetime.datetime.utcnow() - datetime.timedelta(seconds=2)
            )
            async for log in after.guild.audit_logs(
                limit=1, action=discord.AuditLogAction.member_update
            ):
                if log.created_at > time and log.user != log.target:
                    user = f"\n**Updated By:** `{log.user}`"
                else:
                    user = ""
            user = "" if not user else user
            if not after.nick:
                msg = {
                    "title": "Member Server Nickname Removed | Log",
                    "description": f"**User:** `{after}`{user}",
                }
            else:
                msg = {
                    "title": "Member Server Nickname Updated | Log",
                    "description": f"**User:** `{after}`\n**Nick Before:** `{before.nick}`\n**Nick After:** `{after.nick}`{user}",
                }
        elif before.roles != after.roles:
            time = discord.utils.utcnow()
            async for log in after.guild.audit_logs(
                limit=1, action=discord.AuditLogAction.member_role_update
            ):
                if log.created_at > time:
                    user = f"\n**Updated By :** {log.user}"
                else:
                    user = ""
            user = "" if not user else user
            added = set(after.roles) - set(before.roles)
            removed = set(before.roles) - set(after.roles)
            add = False
            if added:
                added = f"**Added :** {', '.join([r.mention for r in added])}\n"
                add = True
            else:
                added = ""
            if removed:
                removed = f"**Removed :** {', '.join([r.mention for r in removed])}"
                add = True
            else:
                removed = ""
            if add:
                member = f"**Member :** {after}\n"
                msg = {
                    "title": "Member Roles Updated | Log",
                    "description": f"{member}{user}\n{added}{removed}",
                }
        if msg:
            embed = discord.Embed(color=0x01f5b6,
                title=msg.get("title"),
                description=msg.get("description")
            )
            embed.set_author(name=after, icon_url=after.avatar.url if after.avatar else after.default_avatar.url)
            embed.set_thumbnail( url=after.avatar.url if after.avatar else after.default_avatar.url)
            embed.set_footer(text="UPDATED", icon_url=self.bot.user.display_avatar.url)
            embed.timestamp = discord.utils.utcnow()        
            for chh in chnl:
                ch = self.bot.get_channel(int(chh))
            await ch.send(embed=embed)           

                  
                  
            
            
    @commands.Cog.listener(name="on_member_ban")
    async def logs_member_ban(self, guild: discord.Guild, member: discord.User):
        data = loggingDB(guild.id)
        chnl = list(data["logging"]["channel"])
        logall =  data["logging"]["logall"]
        async for log in guild.audit_logs(limit=1, action=discord.AuditLogAction.ban):
            if log.user.id == self.bot.user.id:
                return
            user = f"**Banned By:** `{log.user}`\n"
            reason = (
                f"**Reason:** ```\n{'Unspecified' if not log.reason else log.reason}```"
            )
        name = f"**Member:** `{member}`\n"
        embed = discord.Embed(color=0x01f5b6,
            title="Member Banned | Log",
            description=f"{name}{user}{reason}",
        )
        for chh in chnl:
            ch = self.bot.get_channel(int(chh))
            await ch.send(embed=embed)

        
        
        
        
    @commands.Cog.listener(name="on_member_unban")
    async def logs_member_unban(self, guild: discord.Guild, member: discord.User):
        data = loggingDB(guild.id)
        chnl = list(data["logging"]["channel"])
        logall =  data["logging"]["logall"]
    
        async for log in guild.audit_logs(limit=1, action=discord.AuditLogAction.unban):
            if log.user.id == self.bot.user.id:
                return
            user = f"**Unbanned By:** `{log.user}`\n"
            reason = (
                f"**Reason:** ```\n{'Unspecified' if not log.reason else log.reason}```"
            )
        name = f"**Member:** `{member}`\n"
        embed = discord.Embed(color=0x01f5b6,
            title="Member Unbanned | Log",
            description=f"{name}{user}{reason}"
        )
        for chh in chnl:
            ch = self.bot.get_channel(int(chh))
            await ch.send(embed=embed)

        
        
        
        
    @commands.Cog.listener(name="on_message_edit")
    async def logs_message_edit(self, before: discord.Message, after: discord.Message):
        if before.author.bot:
            return
        data = loggingDB(before.guild.id)
        chnl = list(data["logging"]["channel"])
        hacker = list(data["logging"]["msglog"])
        logall =  data["logging"]["logall"]
        embed = discord.Embed(color=0x01f5b6,description=f":scroll: Message sent by {before.author.mention} edited [jump to message]({after.jump_url})"
        )
        embed.add_field(name="Before",
                    value=f"```{before.content}```",
                    inline=False)
        embed.add_field(name="After",
                    value=f"```{after.content}```",
                    inline=False)
        
        embed.set_author(name=before.author, icon_url=before.author.avatar.url if before.author.avatar else before.author.default_avatar.url)
        embed.set_thumbnail( url=before.author.avatar.url if before.author.avatar else before.author.default_avatar.url)
        embed.set_footer(text="EDITED", icon_url=self.bot.user.display_avatar.url)
        embed.timestamp = discord.utils.utcnow()
        for chh in chnl:
            ch = self.bot.get_channel(int(chh))
            await ch.send(embed=hacker)


            
        

    @commands.Cog.listener(name="on_message_delete")
    async def logs_message_delete(self, msg: discord.Message):
        if msg.author.bot:
            return
        data = loggingDB(msg.guild.id)
        chnl = list(data["logging"]["channel"])
        hacker = list(data["logging"]["msglog"])
        logall =  data["logging"]["logall"]
        time = discord.utils.utcnow()
        async for log in msg.guild.audit_logs(
            limit=1, action=discord.AuditLogAction.message_delete
        ):
            if log.created_at > time and log.target == msg.author:
                deleted_by = f"**Deleted By :** {log.user}\n"
            else:
                deleted_by = ""
        content = f"**Content ** : ```\n{msg.content}```" if msg.content != "" else ""
        if msg.attachments:
            attachments = f"**Attachments :** {', '.join([f'`{a.filename}`' for a in msg.attachments])}\n"
        else:
            attachments = ""
        if msg.stickers:
            stickers = (
                f"**Stickers :** {', '.join([f'`{s.name}`' for s in msg.stickers])}"
            )
        else:
            stickers = ""
        time_sent = (
            f"**Message Sent :** {discord.utils.format_dt(msg.created_at, style='R')}\n"
        )
        hacker = discord.Embed(color=0x01f5b6, description=f":put_litter_in_its_place: Message sent by {msg.author} deleted in <#{msg.channel.id}>\n\n{content}{attachments}{stickers}")
        hacker.set_thumbnail( url=msg.author.avatar.url if msg.author.avatar else msg.author.default_avatar.url)
        hacker.set_footer(text="DELETED", icon_url=self.bot.user.display_avatar.url)
        hacker.timestamp = discord.utils.utcnow()
        hacker.set_author(name=msg.author, icon_url=msg.author.avatar.url if msg.author.avatar else msg.author.default_avatar.url)
        for chh in chnl:
            ch = self.bot.get_channel(int(chh))
            await ch.send(embed=hacker)
      
        
    @commands.Cog.listener(name="on_guild_role_delete")
    async def logs_guild_role_delete(self, role: discord.Role):
        data = loggingDB(role.guild.id)
        chnl = list(data["logging"]["channel"])
        hacker = list(data["logging"]["rolelog"])
        logall =  data["logging"]["logall"]
        async for log in role.guild.audit_logs(
            action=discord.AuditLogAction.role_delete, limit=1
        ):
            user = f"**Deleted By:** `{log.user}`\n"
        hacker = discord.Embed(color=0x01f5b6,title=f"Role {role.name} Deleted By {log.user}")
        hacker.add_field(name="Name",
                    value=f"{role.name}",
                    inline=False)
        hacker.add_field(name="Colour",
                    value=f"{role.colour}",
                    inline=False)
        hacker.add_field(name="Position",
                    value=f"{role.position}",
                    inline=False)
        hacker.add_field(name="Hoisted",
                    value=str(role.hoist),
                    inline=False)
        hacker.add_field(name="Mentionable",
                    value=role.mentionable,
                    inline=False)
        hacker.add_field(name="Members",
                    value=f"{len(role.members)}",
                    inline=False)
        hacker.set_thumbnail( url=log.user.avatar.url if log.user.avatar else log.user.default_avatar.url)
        hacker.set_footer(text="DELETED", icon_url=self.bot.user.display_avatar.url)
        hacker.timestamp = discord.utils.utcnow()
        hacker.set_author(name=log.user, icon_url=log.user.avatar.url if log.user.avatar else log.user.default_avatar.url)
        for chh in chnl:
            ch = self.bot.get_channel(int(chh))
            await ch.send(embed=hacker)

        
    @commands.Cog.listener(name="on_guild_role_create")
    async def logs_guild_role_create(self, role: discord.Role):
        data = loggingDB(role.guild.id)
        chnl = list(data["logging"]["channel"])
        hacker = list(data["logging"]["rolelog"])
        logall =  data["logging"]["logall"]
        async for log in role.guild.audit_logs(
            action=discord.AuditLogAction.role_create, limit=1
        ):
            user = f"**Created By:** {log.user}"

        hacker = discord.Embed(color=0x01f5b6, description=f"Role {role.mention} Created By {log.user}")
        hacker.add_field(name="Name",
                    value=f"{role.name}",
                    inline=False)
        hacker.add_field(name="Colour",
                    value=f"{role.colour}",
                    inline=False)
        hacker.add_field(name="Hoisted",
                    value=str(role.hoist),
                    inline=False)
        hacker.add_field(name="Mentionable",
                    value=role.mentionable,
                    inline=False)
        hacker.add_field(name="Position",
                    value=f"{role.position}",
                    inline=False)
        hacker.set_thumbnail( url=log.user.avatar.url if log.user.avatar else log.user.default_avatar.url)
        hacker.set_footer(text="CREATED", icon_url=self.bot.user.display_avatar.url)
        hacker.timestamp = discord.utils.utcnow()
        hacker.set_author(name=log.user, icon_url=log.user.avatar.url if log.user.avatar else log.user.default_avatar.url)
        perms = []
        for perm, allow in iter(role.permissions):
            if allow:
                perms.append(f"`{perm.upper()}` ,")
        if perms:

            hacker.add_field( name="Permissions",value=" ".join(perms))
            for chh in chnl:
                ch = self.bot.get_channel(int(chh))
            await ch.send(embed=hacker)
 
        
        
        
    @commands.Cog.listener(name="on_guild_role_update")
    async def logs_guild_role_update(self, before: discord.Role, after: discord.Role):
        data = loggingDB(before.guild.id)
        chnl = list(data["logging"]["channel"])
        hacker = list(data["logging"]["rolelog"])
        logall =  data["logging"]["logall"]
        async for log in before.guild.audit_logs(
            action=discord.AuditLogAction.role_update, limit=1
        ):
            user = f"**Updated By :** {log.user}\n"
        msg = None
        if before.colour != after.colour:
            changed = f"**Before :** {before.colour}\n**After :** {after.colour}\n"
            msg = {
                "title": "Role Name Updated | Log",
                "description": f"{changed}{user}",
            }
        elif before.hoist != after.hoist:
            changed = (
                f"**Before :** {'Hoisted' if before.hoist else 'Not Hoisted'}\n"
                f"**After :** {'Hoisted' if after.hoist else 'Not Hoisted'}\n"
            )
            msg = {
                "title": "Role Hoist Updated | Log",
                "description": f"{changed}{user}",
            }
        elif before.icon != after.icon:
            msg = {
                "title": f"Role Icon {'Removed' if not after.icon else 'Updated'} | Log",
                "description": f"{user}",
                "thumbnail": f"{self.bot.try_asset(after.icon)}",
            }
        elif before.mentionable != after.mentionable:
            changed = (
                f"**Before :** {'Not Mentionable' if not before.mentionable else 'Mentionable'}\n"
                f"**After :** {'Not Mentionable' if not after.mentionable else '`Mentionable'}\n"
            )
            msg = {
                "title": "Role Mentionable State Updated | Log",
                "description": f"{changed}{user}",
            }
        elif before.name != after.name:
            changed = f"**Before :** {before.name}\n**After :** {after.name}\n"
            msg = {
                "title": "Role Name Updated | Log",
                "description": f"{changed}{user}",
            }
        elif before.permissions != after.permissions:
            b_enabled = [
                str(name).replace("guild", "server").replace("_", " ").title()
                for name, value in set(before.permissions)
                if value is True
            ]
            b_disabled = [
                str(name).replace("guild", "server").replace("_", " ").title()
                for name, value in set(before.permissions)
                if value is False
            ]
            a_enabled = [
                str(name).replace("guild", "server").replace("_", " ").title()
                for name, value in set(after.permissions)
                if value is True
            ]
            a_disabled = [
                str(name).replace("guild", "server").replace("_", " ").title()
                for name, value in set(after.permissions)
                if value is False
            ]
            added = ""
            if b_enabled != a_enabled:
                added = set(a_enabled) - set(b_enabled)
                if added:
                    added = f"**Added :** {', '.join(added)}\n"
                else:
                    added = ""
            removed = ""
            if a_disabled != b_disabled:
                removed = set(a_disabled) - set(b_disabled)
                if removed:
                    removed = f"**Removed :** {', '.join(removed)}\n"
                else:
                    removed = ""
            msg = {
                "title": "Role Permissions Updated | Log",
                "description": added + removed,
            }
        if msg:
            hacker = discord.Embed(color=0x01f5b6,
                title=msg.get("title"),
                description=msg.get("description")
            )
            hacker.set_thumbnail( url=log.user.avatar.url if log.user.avatar else log.user.default_avatar.url)
            hacker.set_footer(text="UPDATED", icon_url=log.user.avatar.url if log.user.avatar else log.user.default_avatar.url)
            hacker.timestamp = discord.utils.utcnow()
            hacker.set_author(name=log.user, icon_url=log.user.avatar.url if log.user.avatar else log.user.default_avatar.url)
            for chh in chnl:
                ch = self.bot.get_channel(int(chh))
            await ch.send(embed=hacker)
 
        
    
    
    
    
    
    @commands.Cog.listener(name="on_voice_state_update")
    async def logs_voice_state_update(
        self,
        member: discord.Member,
        before: discord.VoiceState,
        after: discord.VoiceState,
    ):
        msg = None
        data = loggingDB(member.guild.id)
        chnl = list(data["logging"]["channel"])
        hacker = list(data["logging"]["voicelog"])
        logall =  data["logging"]["logall"]
        if before.channel and after.channel and before.channel != after.channel:
            msg = {
                "title": "Member Moved Voice Channel",
                "description": f"**Member :** {member} \n**Old Channel :** {before.channel.mention}\n"
                f"**New Channel :** {after.channel.mention}",
            }
        elif not before.channel and after.channel:
            msg = {
                "title": "Member Joined Voice Channel",
                "description": f"**Member :** {member}\n**Channel :** {after.channel.mention}",
            }
        elif before.channel and not after.channel:
            msg = {
                "title": "Member Left Voice Channel",
                "description": f"**Member :** {member}\n**Channel :** {before.channel.mention}",
            }
        elif before.deaf != after.deaf:
            if after.deaf:
                msg = {
                    "title": "Member Voice Deafened by Moderator",
                    "description": f"**Member :** {member}",
                }
            elif before.deaf:
                msg = {
                    "title": "Member Voice Undeafened by Moderator",
                    "description": f"**Member:** {member}",
                }
        elif before.mute != after.mute:
            if after.mute:
                msg = {
                    "title": "Member Voice Muted by Moderator",
                    "description": f"**Member:** {member}",
                }
            elif before.mute:
                msg = {
                    "title": "Member Voice Unmuted by Moderator",
                    "description": f"**Member:** {member}",
                }
        if msg:
            hacker = discord.Embed(color=0x01f5b6,
                title=msg.get("title"), description=msg.get("description")
            )
            hacker.set_thumbnail( url=member.avatar.url if member.avatar else member.default_avatar.url)
            hacker.set_footer(text="Astroz", icon_url=self.bot.user.display_avatar.url)
            hacker.timestamp = discord.utils.utcnow()
            hacker.set_author(name=member, icon_url=member.avatar.url if member.avatar else member.default_avatar.url)
            for chh in chnl:
                ch = self.bot.get_channel(int(chh))
            await ch.send(embed=hacker)





        
    @commands.Cog.listener()
    async def on_member_unban(self, member):
        data = loggingDB(member.guild.id)
        chnl = list(data["logging"]["channel"])
        hacker = discord.Embed(color=0x01f5b6,
                title="Member has been unbanned from this server."
            )
        hacker.set_thumbnail( url=member.avatar.url if member.avatar else member.default_avatar.url)
        hacker.add_field(name="User", value=f"{member.name}")
        hacker.add_field(name="Id", value=f"{member.id}")
        hacker.add_field(name="Account Created at", value=f"<t:{int(member.created_at.timestamp())}:F>")
        hacker.set_footer(text="Astroz", icon_url=self.bot.user.display_avatar.url)
        hacker.timestamp = discord.utils.utcnow()
        hacker.set_author(name=member, icon_url=member.avatar.url if member.avatar else member.default_avatar.url)
        for chh in chnl:
            ch = self.bot.get_channel(int(chh))
        await ch.send(embed=hacker)




    @commands.Cog.listener()
    async def on_member_ban(self, member):
        data = loggingDB(member.guild.id)
        chnl = list(data["logging"]["channel"]) 
        hacker = discord.Embed(color=0x01f5b6,
                title="Member has been banned from this server."
            )
        hacker.set_thumbnail( url=member.avatar.url if member.avatar else member.default_avatar.url)
        hacker.add_field(name="User", value=f"{member.name}")
        hacker.add_field(name="Id", value=f"{member.id}")
        hacker.add_field(name="Account Created at", value=f"<t:{int(member.created_at.timestamp())}:F>")
        hacker.set_footer(text="Astroz", icon_url=self.bot.user.display_avatar.url)
        hacker.timestamp = discord.utils.utcnow()
        hacker.set_author(name=member, icon_url=member.avatar.url if member.avatar else member.default_avatar.url)
        for chh in chnl:
            ch = self.bot.get_channel(int(chh))
        await ch.send(embed=hacker)




    @commands.Cog.listener()
    async def on_guild_emoji_create(self, emoji):
        data = loggingDB(emoji.guild.id)
        chnl = list(data["logging"]["channel"])  
        hacker = discord.Embed(color=0x01f5b6,
                description=f"Emoji ({emoji}) has been added."
            )
        hacker.set_footer(text="EMOJI CREATE", icon_url=self.bot.user.display_avatar.url)
        hacker.timestamp = discord.utils.utcnow()
        async for log in emoji.guild.audit_logs(
                limit=1):
            hacker.add_field(name="Added by", value=log.user)  
        hacker.set_author(name=log.user, icon_url=log.user.avatar.url if log.user.avatar else log.user.default_avatar.url)
        hacker.set_thumbnail( url=log.user.avatar.url if log.user.avatar else log.user.default_avatar.url)
        for chh in chnl:
            ch = self.bot.get_channel(int(chh))
        await ch.send(embed=hacker)




    
    @commands.Cog.listener()
    async def on_guild_emoji_remove(self, emoji):
         data = loggingDB(emoji.guild.id)
         chnl = list(data["logging"]["channel"])  
         hacker = discord.Embed(color=0x01f5b6,
                description=f"Emoji ({emoji}) has been deleted."
            )
         hacker.set_footer(text="EMOJI DELETED", icon_url=self.bot.user.display_avatar.url)
         hacker.timestamp = discord.utils.utcnow()
         async for log in emoji.guild.audit_logs(
                limit=1):
            hacker.add_field(name="Deleted by", value=log.user)  
         hacker.set_author(name=log.user, icon_url=log.user.avatar.url if log.user.avatar else log.user.default_avatar.url)
         hacker.set_thumbnail( url=log.user.avatar.url if log.user.avatar else log.user.default_avatar.url)
         for chh in chnl:
             ch = self.bot.get_channel(int(chh))
         await ch.send(embed=hacker)