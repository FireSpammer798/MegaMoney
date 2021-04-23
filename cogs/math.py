import main
@main.commands.command(name='math',aliases=['Math'])
@main.commands.cooldown(1,15)
@main.commands.check(main.check)
async def math(context):
	main.storage.userRegister(context.author)
	with open('profiles.json','r') as file:
		profiles = main.json.load(file)
	def randomProblem():
		mathOperations = ['*','+','-']
		strOperations = ['times','plus','minus']
		titleOperations = ['Multiplication','Addition','Subtraction']
		operationIndex = main.random.randint(0,len(mathOperations)-1)
		operation = mathOperations[operationIndex]
		if operation in '+-':
			number1 = main.random.randint(0,5000)
			number2 = main.random.randint(0,5000)
		elif operation == '*':
			number1 = main.random.randint(0,100)
			number2 = main.random.randint(0,100)
		if operation == '*':
			answer = number1*number2
		elif operation == '+':
			answer = number1+number2
		elif operation == '-':
			answer = number1-number2
		return number1,operation,number2,answer,strOperations[operationIndex],titleOperations[operationIndex]
	number1,operation,number2,answer,strOperation,title = randomProblem()
	if operation != '!':
		messages = [await context.reply(embed=main.Embed(context,title,f'What is {str(number1)} {strOperation} {str(number2)}? You have 15 seconds to answer.')),context.message]
	else:
		messages = [await context.reply(embed=main.Embed(context,title,f'What is {number1} factorial? You have 15 seconds to answer.'))]
	response = ''
	while True:
		try:
			msg = await main.mm.wait_for('message',timeout=15)
			if msg.author == context.author and msg.channel == context.channel:
				try:
					response = float(msg.content)
				except ValueError:
					response = ''
				if type(response) in [float,int] and float(response) == answer:
					messages.append(msg)
					coins = main.random.randint(5000,15000)
					coins /= 100
					messages.append(await msg.reply(embed=main.makeEmbed(context,'Correct Answer',f'Congratulations! You answered the question correctly! You received {coins} coins.')))
					with open('profiles.json','r') as file:
						profiles = main.json.load(file)
					profile = profiles[str(context.author.id)]
					profile['coins'] += coins
					with open('profiles.json','w') as file:
						main.json.dump(profiles,file,indent=2)
					break
				elif type(response) in [float,int] and response != answer:
					messages.append(msg)
					messages.append(await msg.reply(embed=main.makeEmbed(context,'Incorrect Answer',f'Sorry, {context.author.mention}, but that is not the answer. Better luck next time!')))
					break
		except main.asyncio.TimeoutError:
			messages.append(await context.reply(embed=main.makeEmbed(context,'Math Timeout',f'Sorry, {context.author.mention}, but you didn\'t answer the question in time. Try again later.')))
			break
	await messages[len(messages)-1].add_reaction('🚫')
	while True:
		reaction,user=await main.mm.wait_for('reaction_add')
		if reaction.message == messages[len(messages)-1] and str(reaction.emoji) == '🚫' and user == context.author:
			for message in messages:
				try:
					await message.delete()
				except Exception:
					pass
def setup(mm):
	mm.add_command(math)
