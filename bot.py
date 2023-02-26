import json, os, asyncio, discord
import datetime
from discord.ext import commands
# https://discord.com/developers/applications
# client 是我們與 Discord 連結的橋樑，intents 是我們要求的權限
intents_ = discord.Intents.default()
intents_.message_content = True
prefix = "!"
bot = commands.Bot(command_prefix=prefix, intents=intents_)

#調用 event 函式庫
@bot.event
#當機器人完成啟動時
async def on_ready():
    await bot.tree.sync()
    print('>>>BOT ONLINE<<<', bot.user)

@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f'cog.{extension}')
    await ctx.send(f'{extension} Load Successful.')


@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f'cog.{extension}')
    await ctx.send(f'{extension} Reload Successful.')


@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f'cog.{extension}')
    await ctx.send(f'{extension} Unload Successful.')
    #await self.bot.unload_extension(, name=f'cog.{extension}')

@bot.tree.command(name='ping', description='ping say pong')
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'PONG! {bot.latency*1000}')

# @bot.event
# async def on_message(message):
#     #排除自己的訊息，避免陷入無限循環
#     if message.author == bot.user:
#         return
#     #如果包含 ping，機器人回傳 pong
#     if message.content == f'ping':
#         await message.channel.send('中文')

async def load_cog():
    for file_name in os.listdir('./cog'):
        if(file_name.endswith('.py')):
            #print(f'code.{file_name}')
            await bot.load_extension(f'cog.{file_name[:-3]}')


async def main():
    async with bot:
        await load_cog()
        await bot.start(jsondata['TOCKEN'])


with open('./Setting.json', 'r', encoding="UTF-8") as jfile:
    jsondata = json.load(jfile)

TOCKEN = ""

if __name__ =="__main__":

    asyncio.run(main())
