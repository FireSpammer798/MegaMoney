import main
@main.commands.command(name='donate',aliases=['Donation','give'])
@main.commands.check(main.check)
async def donate(context,member:main.discord.Member,coins=0):
	main.storage.userRegister(context.author)
	main.storage.userRegister(member)
	message = None
	if member.bot:
		await main.deletable(main.mm,context,main.Embed(context,'Donation Error',f'You can not donate to {member.mention} because they are a bot!'))
	try:
		coins = float(coins)
	except ValueError:
		await main.deletable(main.mm,context,main.Embed(context,'Donation Error',f'You need to specify a proper amount of coins to donate to {member.mention}!'))
		return
	authorProfile = profiles[str(context.author.id)]
	if authorProfile['coins'] < coins:
		await main.deletable(main.mm,context,main.Embed(context,'Donation Error','You don\'t have enough coins to do this! Earn more coins first.'))
		return
	if message != None:
		await main.deleteMessage(main.mm,context,message=message)
		return
	memberProfile = profiles[str(member.id)]
	memberProfile['coins'] += coins
	authorProfile['coins'] -= coins
	with open('profiles.json','w') as file:
		main.json.dump(profiles,file,indent=2)
	word = 'coins'
	if coins == 1:
		word = 'coin'
	message = await context.reply(embed=main.makeEmbed(context,'Successful Donation',f'You successfully gave {member.mention} {coins} {word}!'))
	await main.deleteMessage(main.mm,context,message)
def setup(mm):
	mm.add_command(donate)
