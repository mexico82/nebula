import core.decorators

@core.decorators.admin.user_admin
@core.decorators.delete.init
def init(update, context):
	bot = context.bot
	message = update.message.text[2:]
	if message != "":
		bot.send_message(update.message.chat_id,
		text="<b>ANNUNCIO:\n</b>{}".format(message),
		parse_mode='HTML')
	else:
		bot.send_message(update.message.chat_id,
		text="Non puoi mandare un annuncio vuoto!")