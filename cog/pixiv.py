import discord, requests, re
from bs4 import BeautifulSoup
from discord.ext import commands
from core.classes import Cog_extension

class pixiv(Cog_extension):
    # 已經繼承Cog_extension內的東西了
    # def __int__(self, bot):
    #     self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print("COG PIXIV IS LOADING...<<")
    @commands.command()
    async def TOP(self, ctx, n:int):
        headers = {'user-agent': 'Mozilla/5.0'}
        html = requests.get(url="https://www.pixiv.net/ranking.php?lang=zh_tw", headers=headers)
        soup = BeautifulSoup(html.text, "html.parser")
        req = soup.find_all("section", class_="ranking-item")
        for i in range(n):
            tmp = re.findall(r'data-src="([^"]+)"', str(req[i]))[0]
            tmp = re.sub(r'pximg.net/c/\d+x\d+',r'pixiv.cat', tmp)
            print(tmp)
            await ctx.send(tmp)

async def setup(bot):
    await bot.add_cog(pixiv(bot))