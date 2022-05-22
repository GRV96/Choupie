import discord

from sys import argv

guild_id = argv[1]
bot_token = argv[2]

bot = discord.Bot()


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.slash_command(guild_ids=[guild_id], name="hello")
async def hello(ctx):
    await ctx.respond("Hello!")


@bot.slash_command(guild_ids=[guild_id], name="work")
async def work(ctx):
	await ctx.respond(f"I am working!\nLatency: {bot.latency*1000} ms")


bot.run(bot_token)
