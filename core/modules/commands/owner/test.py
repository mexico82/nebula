import core.decorators
from config import Config
from core.utility.strings import str_admin_command
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

@core.decorators.owner.init
def init(update, context):
    bot = context.bot
    chat = update.effective_message.chat_id
    reply = update.message.reply_to_message
    if reply is not None:
        bot.forward_message(Config.STAFF_GROUP,
                    from_chat_id=chat,
                    message_id=reply.message_id)
    else:
        bot.send_message(chat, text="TEST ERRORE")