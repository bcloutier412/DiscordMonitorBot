import threading
import discord
from discord.ext import commands
from aquaHQ import aquaHQrun
from yuckPass import yuckPassrun
from test import testrun
from servercollection import aquaHQ, yuckPass, test, servercollection


# def ping_hosts_and_put_in_db():
#     while True:
#         print('ping a host...')
#         time.sleep(3)

# def main_menu():
#     while True:
#         choice = input('choose an option ')
#         if choice == 'scan':
#             t = threading.Thread(target=ping_hosts_and_put_in_db)
#             t.start()
#         else:
#             print('valid options are "scan"')

# if __name__ == '__main__':
#     main_menu()

# client = discord.Client()

# @client.event
# async def on_ready():
#     print('Bot is now online and ready to roll')


# @client.event
# async def on_message(message):

#     if message.author == client.user:
#         return
    
#     if message.content == 'hello':
#         await message.channel.send('Welcome here')

# client.run('OTU2NjYzNTgzNzE3MDkzMzc3.YjzgZA.rdHO42UDG60_M7AIb8aPTS8dAFU')

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def run(ctx, arg=''):
    if arg == 'aquaHQ' and aquaHQ.isLive == False:
        aquaHQ.isLive = True
        t = threading.Thread(target=aquaHQrun)
        t.start()
        await ctx.send('aquaHQ online')

    elif arg == 'yuckPass' and yuckPass.isLive == False:
        yuckPass.isLive = True
        t = threading.Thread(target=yuckPassrun)
        t.start()
        await ctx.send('yuckPass online')
    
    elif arg == 'test' and test.isLive == False:
        test.isLive = True
        t = threading.Thread(target=testrun)
        t.start()
        await ctx.send('test monitor is online')
    
    else:
        await ctx.send('Invalid Entry')

@bot.command()
async def isonline(ctx, arg=''):
    if arg == 'aquaHQ':
        await ctx.send(aquaHQ.isLive)
    elif arg == 'yuckPass':
        await ctx.send(yuckPass.isLive)
    else:
        await ctx.send('invalid arg')

@bot.command()
async def status(ctx):
    for value in servercollection:
        await ctx.send(value.serverName + ': ' + str(value.isLive))
bot.run('OTU2NjYzNTgzNzE3MDkzMzc3.YjzgZA.rdHO42UDG60_M7AIb8aPTS8dAFU')
