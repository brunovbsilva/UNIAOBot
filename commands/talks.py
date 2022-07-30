import discord
from discord.ext import commands
import random

class Talks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="segredo", help="é segredo")
    async def secret(self, ctx):
        try:
            await ctx.author.send("Comi o cu de quem ta lendo")
            await ctx.send(f"@{ctx.author}, te contei um segredo no privado!")
        except discord.errors.Forbidden:
            await ctx.send(f"@{ctx.author}, Não consigo te enviar mensagem no privado.")
    
    @commands.command(name="salve", help="o bot te manda um salve")
    async def salve(self, ctx):
        await ctx.send(f"Olá {ctx.author}")

    
    @commands.command(name='VDN', help="frases aleatórias do sonoplasta do 'Vai Dar Namoro'")
    async def get_random_phrase_VDN(self, ctx):
        phrases = [
            'CAVALO',
            'UUUUUUUUUII!',
            'TOME',
            'ELE GOSTA...',
            'É O FILHIN DE PAPAI É?',
            'VAMO DANÇA? VAMO?',
            'IIIIIIIIIIIIIIIIIIÇA',
            'AAAAAAAAAAAAAAAAAIII AIII AIII... AHHHHHHH MAMÃEEEE'
        ]
        await ctx.send(random.choice(phrases))
            

def setup(bot):
    bot.add_cog(Talks(bot))