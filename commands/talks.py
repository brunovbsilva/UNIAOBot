import discord
from discord.ext import commands
import random
from utils.usual_functions import *

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
        await ctx.send(f"Salve <@{ctx.author.id}>")
    
    @commands.command(name='vaiDarNamoro', help="frases aleatórias do sonoplasta do 'Vai Dar Namoro'")
    async def get_random_phrase_VDN(self, ctx):
        phrases = readJson('VDN')
        await ctx.send(random.choice(phrases))
    
    @commands.command(name='addMessage', help='adiciona uma frase à lista de frases do servidor, acesse por u!getMessage')
    async def add_message(self, ctx, *expression):
        server = f'{ctx.guild.id}'
        data = readJson('messages')
        newId = 1
        if not server in data or data[server] == []:
            message = newMessage(newId, ctx.author.id, " ".join(expression))
            data[server] = [message]
        else:
            newId = data[server][-1]['id'] + 1
            message = newMessage(newId, ctx.author.id, " ".join(expression))
            data[server].append(message)
        
        writeJson('messages', data)
        await ctx.send('mensagem criada com sucesso!')

    @commands.command(name='getMessage', help='recebe uma frase aleatória das frases do servidor')
    async def get_message(self, ctx):
        server = f'{ctx.guild.id}'
        phrases = []
        data = readJson('messages')
        for x in data[server]:
            phrases.append(x['message'])
        await ctx.send(random.choice(phrases))

    @commands.command(name='getMyMessages', help='recebe uma lista no privado com suas mensagens adicionadas no servidor')
    async def get_my_messages(self, ctx):
        server = f'{ctx.guild.id}'
        phrases = []
        data = readJson('messages')
        for x in data[server]:
            if(x['user_id'] == ctx.author.id):
                phrases.append(x)
        
        sendAuthor = 'Suas mensagens no servidor:\n'
        for x in phrases:
            id, message = x['id'], x['message']
            sendAuthor = sendAuthor + f'id: { id }, mensagem: { message }\n'
        await ctx.author.send(sendAuthor)
    
    @commands.command(name='getAllMessages', help='[VIP] recebe uma lista no privado com as mensagens adicionadas no servidor')
    async def get_all_messages(self, ctx):
        if not isVIP(ctx.author.id):
            await ctx.send(f'Olá <@{ctx.author.id}>, O comando só pode ser usado por VIPs.')
            return

        server = f'{ctx.guild.id}'
        phrases = []
        data = readJson('messages')
        for x in data[server]:
            phrases.append(x)
        
        sendAuthor = 'Todas as mensagens no servidor:\n'
        for x in phrases:
            id, message = x['id'], x['message']
            sendAuthor = sendAuthor + f'id: { id }, mensagem: { message }\n'
        await ctx.author.send(sendAuthor)

    @commands.command(name='deleteMessage', help='delete a mensagem com o id passado, só funciona se a mensagem for sua ou você for VIP')
    async def delete_message(self, ctx, id):
        server = f'{ctx.guild.id}'
        data = readJson('messages')
        i = False
        for x in data[server]:
            if x['id'] == eval(id):
                if(isVIP(ctx.author.id) or x['user_id'] == ctx.author.id):
                    data[server].remove(x)
                    i = True

        writeJson('messages', data)
        if(i):
            await ctx.send('Mensagem apagada com sucesso!')
        else:
            await ctx.send('Nao foi possível apagar a mensagem, verifique se voce possui acesso para o mesmo ou se o id esta correto.')

def newMessage(id, authorId, message):
    return {
        'id': id,
        'user_id': authorId,
        'message': message
    }

def setup(bot):
    bot.add_cog(Talks(bot))