import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

status_dict = {}

@bot.command()
async def done(ctx, name):
    status_dict[name] = "✅"
    await ctx.send(f"{name} を ✅ に記録しました")

@bot.command()
async def fail(ctx, name):
    status_dict[name] = "❌"
    await ctx.send(f"{name} を ❌ に記録しました")

@bot.command()
async def list(ctx):
    if not status_dict:
        await ctx.send("記録がありません")
    else:
        msg = "\n".join(f"{name}: {mark}" for name, mark in status_dict.items())
        await ctx.send(msg)

@bot.command()
async def reset(ctx):
    status_dict.clear()
    await ctx.send("全ての記録をリセットしました")

bot.run("MTQwMDc4OTM3MTE2NjEzMDIzNw.GsvSXn.GQzovzCE6ajH6nBOfLxIC_elnde5hBHDEWNtfk")
