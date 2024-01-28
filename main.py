import os
from core.Astroz import Astroz
import asyncio,json
import jishaku, cogs
from discord.ext import commands, tasks
import discord
from discord.ext import commands
from discord import app_commands
import traceback
from discord.ext.commands import Context
from discord import Spotify
from itertools import cycle
from discord.ext import tasks
import random





os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"
os.environ["JISHAKU_HIDE"] = "True"
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_FORCE_PAGINATOR"] = "True"


client = Astroz()
tree = client.tree






    
async def astroz_stats():
    while True:
        servers = len(client.guilds)
        users = sum(g.member_count for g in client.guilds if g.member_count != None)
        sv_ch = client.get_channel(1050631119239913552)
        users_ch = client.get_channel(1050631157596835880)
        await asyncio.sleep(3000)
        await sv_ch.edit(name="Servers ; {}".format(servers))
        await users_ch.edit(name="Users ; {}".format(users))



class Embed(discord.ui.Modal, title='Embed Configuration'):
    tit = discord.ui.TextInput(
        label='Embed Title',
        placeholder='Embed title here',
    )

    description = discord.ui.TextInput(
        label='Embed Description',
        style=discord.TextStyle.long,
        placeholder='Embed description optional',
        required=False,
        max_length=400,
    )

    thumbnail = discord.ui.TextInput(
        label='Embed Thumbnail',
        placeholder='Embed thumbnail here optional',
        required=False,
    )

    img = discord.ui.TextInput(
        label='Embed Image',
        placeholder='Embed image here optional',
        required=False,
    )

    footer = discord.ui.TextInput(
        label='Embed footer',
        placeholder='Embed footer here optional',
        required=False,
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(title=self.tit.value, description=self.description.value,color=0x00FFE4)
        if not self.thumbnail.value is None:
          embed.set_thumbnail(url=self.thumbnail.value)
        if not self.img.value is None:
          embed.set_image(url=self.img.value)
        if not self.footer.value is None:
          embed.set_footer(text=self.footer.value)
        await interaction.response.send_message(embed=embed)

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)


        traceback.print_tb(error.__traceback__)


      
@tree.command(name="embed", description="Create A Embed Using Astroz")
async def _embed(interaction: discord.Interaction) -> None:
  await interaction.response.send_modal(Embed())



########################################




@client.event
async def on_ready():
    print("Loaded & Online!")
    print(f"Logged in as: {client.user}")
    print(f"Connected to: {len(client.guilds)} guilds")
    print(f"Connected to: {len(client.users)} users")
    await client.loop.create_task(astroz_stats())
    try:
        synced = await client.tree.sync()
        print(f"synced {len(synced)} commands")
    except Exception as e:
        print (e)



from flask import Flask
from threading import Thread

app = Flask(__name__) 
@app.route('/')
def home():
    return "lamao ded"
def run():
  app.run(host='0.0.0.0',port=8080)
def keep_alive():  
  server=Thread(target=run)
  server.start()
keep_alive()





@client.event
async def on_command_completion(context: Context) -> None:

    full_command_name = context.command.qualified_name
    split = full_command_name.split("\n")
    executed_command = str(split[0])
    hacker = client.get_channel(1046447249460305960) 
    if context.guild is not None:
        embed = discord.Embed(
                      color=0x01f5b6
              ) 
        embed.set_author(name=f"Executed {executed_command} Command By : {context.author}", icon_url=f"{context.author.avatar}") 
        embed.set_thumbnail(url =f"{context.author.avatar}")
        embed.add_field(name="<a:im_arrowr:1038029121881636884> Command Name :",
                    value=f"{executed_command}",
                    inline=False)  
        embed.add_field(name="<a:im_arrowr:1038029121881636884> Command Executed By :",
                    value=f"{context.author} | ID: [{context.author.id}](https://discord.com/users/{context.author.id})",
                    inline=False)   
        embed.add_field(name="<a:im_arrowr:1038029121881636884> Command Executed In :",
                    value=f"{context.guild.name}  | ID: [{context.guild.id}](https://discord.com/users/{context.author.id})",
                    inline=False) 
        embed.add_field(name="<a:im_arrowr:1038029121881636884> Command Executed In Channel :",
                    value=f"{context.channel.name}  | ID: [{context.channel.id}](https://discord.com/channel/{context.channel.id})",
                    inline=False)
        embed.set_footer(text="Powered By Astroz",icon_url=client.user.display_avatar.url)
        await hacker.send(embed=embed)
    else:
        embed1 = discord.Embed(
                      color=0x01f5b6)       
        embed1.set_author(name=f"Executed {executed_command} Command By : {context.author}", icon_url=f"{context.author.avatar}") 
        embed1.set_thumbnail(url =f"{context.author.avatar}")
        embed1.add_field(name="<a:im_arrowr:1038029121881636884> Command Name :",
                    value=f"{executed_command}",
                    inline=False)  
        embed1.add_field(name="<a:im_arrowr:1038029121881636884> Command Executed By :",
                    value=f"{context.author} | ID: [{context.author.id}](https://discord.com/users/{context.author.id})",
                    inline=False)
        embed1.set_footer(text="Powered By Astroz",icon_url=client.user.display_avatar.url)
        await hacker.send(embed=embed1)




@client.command()
async def spotify(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
        pass
    if user.activities:
        for activity in user.activities:
            if isinstance(activity, Spotify):
                nemo = discord.Embed(
                    title = f"{user.name}'s Spotify",
                    description = "Listening to {}".format(activity.title),
                    color = 0x01f5b6)
                nemo.set_thumbnail(url=activity.album_cover_url)
                nemo.add_field(name="Artist", value=activity.artist)
                nemo.add_field(name="Album", value=activity.album)
                nemo.set_footer(text="Song started at {}".format(activity.created_at.strftime("%H:%M")))
                await ctx.send(embed=nemo)





async def main():
    async with client:
      os.system("clear")
      await client.load_extension("cogs")
      await client.load_extension("jishaku")
      await client.start("MTAxMjYyNzA4ODIzMjE2NTM3Ng.G6fWNZ.oyQgaKEVU8T_zZ0Vk_Zj95QHQ4hVwqCgbBOFK4")  


   
if __name__ == "__main__":
  asyncio.run(main())




