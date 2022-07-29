from discord.ext import commands
import random

class Smarts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="calcular")
    async def calculate_expression(self, ctx, *expression):
        expression = "".join(expression)
        response = eval(expression)
        await ctx.send("A resposta é: " + str(response))

    @commands.command(name='roll', help='Sorteia um número entre 1 ao número passado. argumentos: [número]')
    async def roll_(self, ctx, expression):
        response = []
        count = 0
        while count<eval(expression):
            count = count+1
            response.append(count)
        
        if len(response)>0:
            await ctx.send(f"numero sorteado: {random.choice(response)}")
        else:
            await ctx.send("Argumentos não estão na forma correta! Digite u!help para mais informações.")
            
def setup(bot):
    bot.add_cog(Smarts(bot))