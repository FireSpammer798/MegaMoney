import main
@main.commands.command(name='help',aliases=['Help'])
@main.commands.check(main.check)
async def help(context):
	await main.deletable(main.mm,context,main.complexEmbed(context,[f'{context.prefix}math',f'{context.prefix}profile [member]',f'''{context.prefix}buy <item> [amount]
{context.prefix}purchase <item> <amount>''',f'''{context.prefix}donate <member> <coins>
{context.prefix}give <member> <coins>''',f'{context.prefix}mine',f'''{context.prefix}reload
{context.prefix}refresh
{context.prefix}restart''',f'''{context.prefix}stats
{context.prefix}megamoney''',f'''{context.prefix}shop
{context.prefix}store''',f'{context.prefix}support'],['This will give you somewhere from 50 to 150 coins for solving a math problem in 10 seconds.','This will let you view either your own or someone else\'s profile.',f'This will let you buy an item from my shop. You need to have enough coins for this!','This will let you give someone a certain amount of coins. You must have enough coins to donate!','This will let you mine for ores.','This will let you refresh me. Please run this command if anything seems to be working improperly.','This will let you view my stats.','This will let you view my shop.'
'This will give you a a link to my support server and to invite me to your own server.']))
def setup(mm):
	mm.add_command(help)
