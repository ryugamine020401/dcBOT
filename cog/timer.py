import asyncio, json, datetime
import time

import discord
from discord.ext import commands
from core.classes import Cog_extension

# 引入方式亂七八糟 但可以讀到 可能是bot跟其他都有連結 所以jfile完全共用...
with open('Setting.json', 'r', encoding="UTF-8") as jfile:
    jsondata = json.load(jfile)
class timer(Cog_extension):

    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        self.cnt = 0

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

        # async def interval():   # 間隔
        #     await self.bot.wait_until_ready()
        #     # print("inininin")
        #
        #     self.channel = self.bot.get_channel(jsondata['Timer_channel_ID'])
        #     #print(self.bot.is_closed())
        #     while (not self.bot.is_closed()):
        #         await self.channel.send("HIHI")
        #         await asyncio.sleep(3600) #time.sleep()
        # self.bg_task = self.bot.loop.create_task(interval())
        async def interval2():   # 間隔
            await self.bot.wait_until_ready()
            # print("inininin")
            self.channel = self.bot.get_channel(jsondata['Timer_channel_ID'])
            #print(self.bot.is_closed())
            while (not self.bot.is_closed()):
                with open('Setting.json', 'r') as jfile:
                    tmp = json.load(jfile)

                nowtime = datetime.datetime.now().strftime('%H%M')
                if (nowtime == tmp['time'] and tmp['timer_counter'] == "0"):
                    tmp['timer_counter'] = "1"
                    # with open要放在任何的await前面
                    with open('Setting.json', 'w', encoding='utf8') as jfile:
                        json.dump(tmp, jfile, indent=4)
                    await self.channel.send("time now...")
                    await asyncio.sleep(5)  # time.sleep()
                else:
                    #print("不進去了",tmp['timer_counter'] == "0", nowtime == tmp['time'], type(nowtime))
                    await asyncio.sleep(5)  # time.sleep()
        self.bg_task2 = self.bot.loop.create_task(interval2())
    @commands.command()
    async def timer(self, ctx):
        await ctx.send("cntcnt")

    @commands.Cog.listener()
    async def on_ready(self):
        print(">>COG TIMER IS LOADING...<<")
async def setup(bot):
    await bot.add_cog(timer(bot))