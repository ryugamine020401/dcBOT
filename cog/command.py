import discord
from discord.ext import commands
from core.classes import Cog_extension

class command(Cog_extension):
    # 已經繼承Cog_extension內的東西了
    # def __int__(self, bot):
    #     self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print("COG COMMAND IS LOADING...<<")
    @commands.command()
    async def Ping(self, ctx):
        await ctx.send("pong")

    # @commands.command()
    # async def load(self, ctx, extension):
    #     await ctx.send(f'cog.{extension} load successful.')
    #     await self.bot.load_extension(f'cog.{extension}')
    #
    #
    # @commands.command()
    # async def reload(self, ctx, extension):
    #     await ctx.send(f'cog.{extension} reload successful.')
    #     await self.bot.reload_extension(f'cog.{extension}')
    #
    #
    # @commands.command()
    # async def unload(self, ctx, extension):
    #     print("有近來", extension, type(extension),f'cog.{extension}')
    #     await self.bot.unload_extension(f'cog.{extension}')
    #     await ctx.send(f'cog.{extension} unload successful.')
    #     #await self.bot.unload_extension(, name=f'cog.{extension}')




async def setup(bot):
    await bot.add_cog(command(bot))