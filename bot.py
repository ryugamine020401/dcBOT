import os
import asyncio
import discord
import datetime
from discord.ext import commands
#client 是我們與 Discord 連結的橋樑，intents 是我們要求的權限
intents_ = discord.Intents.default()
intents_.message_content = True
prefix = "!"
bot = commands.Bot(command_prefix=prefix, intents=intents_)

#調用 event 函式庫
@bot.event
#當機器人完成啟動時
async def on_ready():
    print('>>>BOT ONLINE<<<', bot.user)
#當有訊息時

# @bot.event
# async def on_message(message):
#     #排除自己的訊息，避免陷入無限循環
#     if message.author == bot.user:
#         return
#     #如果包含 ping，機器人回傳 pong
#     if message.content == f'ping':
#         await message.channel.send('中文')

# class Main(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot
#     @commands.command()
#     async def ping(self, ctx):
#         await ctx.send(f'{round(self.bot.latency*1000)} ms')


# def setup(bot):
#     bot.add_cog(Main(bot))



    #print(file_name)

async def load_cog():
    for file_name in os.listdir('./cog'):
        if(file_name.endswith('.py')):
            #print(f'code.{file_name}')
            await bot.load_extension(f'cog.{file_name[:-3]}')


async def main():
    async with bot:
        await load_cog()
        await bot.start(TOCKEN)



# async def interval():
#     await bot.wait_until_ready()
#     print("???")
#     channel = bot.get_channel(863774440957149195)
#     while not bot.is_closed():
#         await channel.send("hello")
#         await asyncio.sleep(5)

TOCKEN = "MTA3NzU4OTU5ODEwNjA0NjU0Ng.GGJo9p.WsimgTFhSl5ydCqXsh3RwNvOq3FVjZIx2Lw5Oo"
if __name__ =="__main__":

    asyncio.run(main())