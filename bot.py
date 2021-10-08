import discord
from discord.ext import commands
import base64
import os


# permissions integer: 534723951680
bot = discord.ext.commands.Bot(command_prefix='.')


@bot.command()
async def b64(ctx, task, string=None):
    if ctx.author.nick == None:
        username = bot.user
    else:
        username = ctx.author.nick

    if task == 'encode':
        stringBytes = string.encode("ascii")

        b64Bytes = base64.b64encode(stringBytes)
        b64String = b64Bytes.decode("ascii")

        embed = discord.Embed(title=f"Encoded string for {username}:", description=b64String,
                              colour=discord.Colour.green())
        await ctx.send(embed=embed)

    if task == 'decode':
        b64Bytes = string.encode("ascii")

        stringBytes = base64.b64decode(b64Bytes)
        decodedString = stringBytes.decode("ascii")

        embed = discord.Embed(title=f"Decoded string for {username}:", description=decodedString, colour=discord.Colour.green())
        await ctx.send(embed=embed)

    if task == 'help':
        result = """To encode:
.b64 encode <string>

To decode:
.b64 decode <string>

To toggle list of commands:
.b64 help"""

        embed = discord.Embed(title="List of commands:", description=result, colour=discord.Colour.green())
        await ctx.send(embed=embed)


bot.run(os.getenv('TOKEN'))