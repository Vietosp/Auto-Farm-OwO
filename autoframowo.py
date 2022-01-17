import time
if id == "894205595337490543":
	#createteam = int(input(print("Tạo Team Zoo Animals\n[1] Ok\n[2] Ko")))
	
	prefix = prefix
	keep_alive()
	bot = commands.Bot(command_prefix=prefix,
                   	help_command=None,
                   	case_insensitive=True,
                   	self_bot=True)
                   
	@bot.event
	async def on_message(message):
		if "Please complete your captcha to verify that you are human! " in message.content():
			global dm
			dm = False
			print("Tài khoản của bạn đang bị captcha hãy vào tài khoản để xác minh đi")
		else:
			await bot.process_commands(message)
	@bot.command(pass_context=True)
	async def run(ctx):
		await ctx.message.delete()
		await ctx.send('Run AutoFarm OwO')
		global dmcs
		dmcs = True
		while dmcs:
			async with ctx.typing():
				ran = int(random.randint(1,15))
				await ctx.send("Owo hunt")
				a += 1
				if a == 5:
					time.sleep(30)
				else:
					if b > 0:
						time = 15 - ran
						time.sleep(ran)
						b = b - 1
					else:
						b += 1
						time.sleep(ran)
				await ctx.send("owo sell all")
				time.sleep(5)
				await ctx.send("owo cash")

	@bot.command()
	async def stop(ctx):
		await ctx.message.delete()
		await ctx.send('Stop AutoFarm OwO')
		global dmcs
		dmcs = False
	
		