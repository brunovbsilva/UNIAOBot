from google_images_search import GoogleImagesSearch
from decouple import config
import discord
from discord.ext import commands

GCS_DEVELOPER_KEY = config('GCS_DEVELOPER_KEY')
GCS_CX = config('GCS_CX')

class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="bot", help="apresentação do bot")
    async def get_random_image(self, ctx):
        embed = discord.Embed(
            title = "UNIÃOBot!",
            description = "Olá, sou o boto da união\nPS: Mensagem automática!",
            color=0x0000FF,
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed.set_footer(text="Bot da união está evoluindo!")
        # embed.add_field(name="Gian é gay", value="O Lucas e o Yuri também!")
        embed.set_image(url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)
    
    @commands.command(name="pesquisa", help="retorna uma imagem ou gif. uso 'u!pesquisa [o que quiser]'")
    async def get_search_image(self, ctx, *expression):
        pesquisa = ' '.join(expression)
        gis = GoogleImagesSearch(GCS_DEVELOPER_KEY, GCS_CX)
        _search_params = {
            'q': str(' '.join(expression)),
            'num': 1,
            'fileType': 'jpg|gif|png'
        }
        gis.search(search_params=_search_params)
        if len(gis.results())>0:
            for image in gis.results():
                embed = discord.Embed(
                    title = f"Imagem: {pesquisa}",
                    color=0x0000FF,
                )
                embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                embed.set_footer(text="Bot da união está evoluindo!")
                embed.set_image(url=image.url)
                await ctx.send(embed=embed)
        else:
            await ctx.send('Não encontrei nenhum resultado para a pesquisa.')

def setup(bot):
    bot.add_cog(Images(bot))