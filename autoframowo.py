if id == "894205595337490543":
	prefix = prefix
	keep_alive()
	bot = commands.Bot(command_prefix=prefix,
                   	help_command=None,
                   	case_insensitive=True,
                   	self_bot=True)
	@bot.command(pass_context=True)
	async def run(ctx):
		await ctx.message.delete()
		await ctx.send('Run AutoFarm OwO')
		global dm
		dm = True
		while dm:
			async with ctx.typing():
				ran = int(random.randint(1,15))
				await ctx.send("Owo h")
				a += 1
				if a == 5:
					asyncio.sleep(30)
				else:
					if b > 0:
						time = 15 - ran
						asyncio.sleep(ran)
						b = b - 1
					else:
						b += 1
						asyncio.sleep(ran)
					
				await ctx.send("Owo sell all")
				asyncio.sleep(10)
				await ctx.send("owo cash")

	@bot.command()
	async def stop(ctx):
		await ctx.message.delete()
		await ctx.send('Stop AutoFarm OwO')
		global dm
		dm = False
	@bot.event
	async def on_message(message):
		if "Please complete your captcha to verify that you are human! " in message.content():
			global dm
			dm = False
			print("Tài khoản của bạn đang bị captcha hãy vào tài khoản để xác minh đi")
		else:
			await bot.process_commands(message)
		