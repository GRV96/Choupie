import discord
from sys import argv

from rps_game import\
	rand_elem_name,\
	rps_game


guild_id = argv[1]
bot_token = argv[2]

bot = discord.Bot()


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.slash_command(guild_ids=[guild_id], name="hello")
async def hello(ctx):
    await ctx.respond("Hello!")


@bot.slash_command(guild_ids=[guild_id],
	name="rockpaperscissors", describe="Chose r, p or s.")
async def rock_paper_scissors(ctx, choice: discord.Option(str)):
	choupies_choice = rand_elem_name()
	result = rps_game(choice, choupies_choice)

	if result < 0:
		result = "Choupie wins."

	elif result == 0:
		result = "Draw"

	else:
		result = "You're winner!"

	await ctx.respond(f"You: {choice}\nChoupie: {choupies_choice}\n{result}")


@bot.slash_command(guild_ids=[guild_id], name="work")
async def work(ctx):
	await ctx.respond(f"I am working!\nLatency: {bot.latency*1000} ms")


bot.run(bot_token)
