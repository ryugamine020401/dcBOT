import discord
from discord.ext import commands
from core.classes import Cog_extension

class Embed(Cog_extension):
    # 已經繼承Cog_extension內的東西了
    # def __int__(self, bot):
    #     self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print("COG COMMAND IS LOADING...<<")
    @commands.command()
    # https://cog-creators.github.io/discord-embed-sandbox/
    async def EMB(self, ctx):
        embed = discord.Embed(title="BOT SOURCE CODE", url="https://github.com/ryugamine020401/dcBOT", description="botDC",
                              color=0x77e647)
        embed.set_author(name="YMZK", url="https://github.com/ryugamine020401",
                         icon_url="https://i.pixiv.cat/img-master/img/2021/02/11/07/24/25/87679148_p0_master1200.jpg")
        embed.add_field(name="1", value="11", inline=True)
        embed.add_field(name="2", value="22", inline=True)
        embed.add_field(name="3", value="33", inline=True)
        embed.add_field(name="4", value="44", inline=True)
        embed.set_footer(text="FONT TEXT")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Embed(bot))

