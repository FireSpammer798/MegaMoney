import main,json
@main.commands.command(name='buy',aliases=['Purchasing','purchase'])
@main.commands.check(main.check)
async def buy(context:main.commands.context.Context,item,itemOrAmount=None,amount=1):
	main.storage.userRegister(context.author)
	amountValue = 'amount'
	if itemOrAmount == None:
		itemOrAmount = '1'
	if '0' in itemOrAmount or '1' in itemOrAmount or '2' in itemOrAmount or '3' in itemOrAmount or '4' in itemOrAmount or '5' in itemOrAmount or '6' in itemOrAmount or '7' in itemOrAmount or '8' in itemOrAmount or '9' in itemOrAmount:
		try:
			amount = int(itemOrAmount)
			amountValue = 'itemOrAmount'
		except ValueError:
			await main.deletable(main.mm,context,main.Embed(context,'Purchasing Error','This is not a valid amount to buy!'))
			return
	if amount // 1 == amount / 1:
		amount = int(amount)
	if amountValue == 'amount':
		item = item + ' ' + itemOrAmount
	item = item.lower()
	suffix = 'single'
	if amount != 1:
		suffix = 'plural'
	if item not in list(main.storage.buyables):
		await main.deletable(main.mm,context,main.Embed(context,'Purchasing Error','That item is not in my shop!'))
		return
	with open('profiles.json','r') as file:
		profiles = json.load(file)
	profile = profiles[str(context.author.id)]
	if profile['coins'] < main.storage.buyables[item]['buy']*amount:
		await main.deletable(main.mm,context,main.Embed(context,'Purchasing Error',f'You need more coins to buy {amount} {main.storage.buyables[item][suffix]}!'))
		return
	inventory = profile['inventory']
	inventory[item] += amount
	profile['coins'] -= main.storage.buyables[item]['buy']*amount
	buy = main.storage.buyables[item]['buy']
	with open('profiles.json','w') as file:
		json.dump(profiles,file,indent=2)
	await main.deletable(main.mm,context,main.Embed(context,'Successful Purchase',f'You successfully bought {amount} {main.storage.buyables[item][suffix]} for {"{:,}".format(amount*buy)} coins!'))
def setup(mm):
	mm.add_command(buy)
