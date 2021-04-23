import main
@main.commands.command(name='craft',aliases=['Crafting','build','make'])
@main.commands.check(main.check)
async def craft(ctx,*,item):
	main.storage.userRegister(ctx.author)
	if item.lower() not in main.storage.craftables:
		await main.deleteMessage(main.mm,ctx,await ctx.reply(embed=main.Embed(ctx,'Crafting Error','This item can not be crafted! It might not even be a valid item.')))
		return
def setup(mm):
	mm.add_command(craft)
