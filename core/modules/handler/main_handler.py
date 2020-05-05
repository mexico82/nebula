from config import Config
from . import (
    admin_command,
    custom_handler,
    bad_words,
	super_ban_handler,
	debug_terminal
    )

msg = ""

def trigger(match):
	return msg.lower().startswith(match.lower())

#FUNCTION DECLARATION
def init(update, context):
	global msg #pylint: disable=global-statement

	bad_words.init(update, context)
	super_ban_handler.init(update, context)
	debug_terminal.init(update)
	if update.message is None or update.message.text is None:
		return

	msg = update.message.text

	if trigger("@admin"):
		admin_command.init(update, context)
	elif trigger(Config.BOT_NAME):
		custom_handler.customhandler(update, context)
	elif trigger("/"):
		custom_handler.customhandler(update, context)