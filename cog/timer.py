import asyncio, json
import time

import discord
from discord.ext import commands
from core.classes import Cog_extension
with open('.\\Setting.json', 'r', encoding="UTF-8") as jfile:
    jsonfile = json.load(jfile)
class timer(commands.Cog):

    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

        async def interval():   # 間隔
            await self.bot.wait_until_ready()
            print("inininin")
            self.channel = self.bot.get_channel(jsonfile['Timer_channel_ID'])
            print(self.bot.is_closed())
            while (not self.bot.is_closed()):
                await self.channel.send("HIHI")
                await asyncio.sleep(3600) #time.sleep()
        self.bg_task = self.bot.loop.create_task(interval())
    @commands.command()
    async def timer(self, ctx):
        await ctx.send("cntcnt")

    @commands.Cog.listener()
    async def on_ready(self):
        print(">loading<")
async def setup(bot):
    await bot.add_cog(timer(bot))