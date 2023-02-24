import discord
from discord.ext import commands
from core.classes import Cog_extension

class Command(Cog_extension):
    # 已經繼承Cog_extension內的東西了
    # def __int__(self, bot):
    #     self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print("COG COMMAND IS LOADING...<<")
    @commands.command()
    async def Ping(self, ctx):
        await ctx.send("pong")

async def setup(bot):
    await bot.add_cog(Command(bot))