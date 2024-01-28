import discord
from discord.ext import commands

class hacker111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Welcome commands"""
  
    def help_custom(self):
		      emoji = '<:jk_lgging:1053691692835950592>'
		      label = "Logging"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __Logging__(self, ctx: commands.Context):
        """`logall` , `logall enable` , `logall disable` """

