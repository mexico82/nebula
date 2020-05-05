import core.decorators
from config import Config


@core.decorators.delete.init
@core.decorators.private_command.init
def init(update, context):
	bot = context.bot
	message = update.message.text[9:]
	if message != "":
		bot.send_message(Config.OWNER,
		text="<b>FEEDBACK:</b>\n<code>Messaggio:{}</code>"
		.format(message),
		parse_mode='HTML')
		bot.send_message(update.message.from_user.id,
		text='Feedback inviato correttamente!',
		parse_mode='HTML')
	else:
		bot.send_message(update.message.chat_id,
		text="Non puoi mandare un Feedback senza alcun messaggio!")