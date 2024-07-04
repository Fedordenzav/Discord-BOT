import random
import discord
from discord.ext import commands

bot = commands.Bot(intents=discord.Intents.all(), command_prefix="/")


@bot.command("info")
async def command_info(ctx:commands.Context):
    await ctx.send("Я классный бот!")



@bot.command("predictions")
async def command_predictions(ctx:commands.Context):
    await ctx.send("У тебя сегодня будет хороший день!")  



@bot.command("number")
async def command_number(ctx:commands.Context):
    await ctx.send("101") 


@bot.command("plus")
async def command_plus(ctx:commands.Context, a,b):
    a = int(a)
    b = int(b)
    result = a + b
    await ctx.send(result)


@bot.command("minus")
async def command_minus(ctx:commands.Context, a,b):
    a = int(a)
    b = int(b)
    result = a - b
    await ctx.send(result)



@bot.command("multiply")
async def command_multiply(ctx:commands.Context, a,b):
    a = int(a)
    b = int(b)
    result = a * b
    await ctx.send(result)

@bot.command("tripple_plus")
async def command_tripple_plus(ctx:commands.Context, a,b):
    a = int(a)
    b = int(b) 
    c = int(c)
    result = a + b + c
    await ctx.send(result)






@bot.command('guess')
async def guess_number(ctx, user_guess: int):
    await ctx.send(f'Твой ответ {user_guess}')
    await ctx.send(f'Бот {random.randint(1, 10)}')

    if random_number is None:
        await ctx.send('Сначала начните новую игру командой $startgame.')
        return

    if user_guess == random_number:
        await ctx.send(f':tada:Поздравляю! Вы угадали число {random_number}.')
        random_number = None
    elif user_guess < random_number:
        await ctx.send('Ваше число меньше загаданного. Попробуйте еще раз!')
    else:
        await ctx.send('Ваше число больше загаданного. Попробуйте еще раз!')







bot.run("NOOOO")

