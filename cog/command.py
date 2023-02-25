import discord, json
from discord.ext import commands
from core.classes import Cog_extension

# 引入方式亂七八糟 但可以讀到 可能是bot跟其他都有連結 所以jfile完全共用...
with open('Setting.json', 'r', encoding="utf8") as jfile:
    jsondata = json.loads(jfile.read())
    #print(jsondata['TOCKEN'])

class command(Cog_extension):
    # 已經繼承Cog_extension內的東西了
    # def __int__(self, bot):
    #     self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(">>COG COMMAND IS LOADING...<<")

    @commands.command()
    async def Ping(self, ctx):
        await ctx.send("pong")

    @commands.command()
    async def Settime(self, ctx, time):
        # await print("進settime")
        # await ctx.send(time)
        jsondata['time'] = time
        jsondata['timer_counter'] = "0"
        # 輸出方式亂七八糟 但可以讀到 可能是bot跟其他都有連結 所以jfile完全共用...
        with open('Setting.json', "w", encoding="utf8") as jfile:
            print("客戶端輸入 更動定時器時間...")
            json.dump(jsondata, jfile, indent=4)
        await ctx.send("time set successful.")


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

# with open('..\\Setting.json', 'w', encoding='UTF-8') as jfile:
#     print("寫入")
#     json.dump(jsondata, jfile, indent=4)

async def setup(bot):
    await bot.add_cog(command(bot))