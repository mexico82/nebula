import core.decorators
from config import Config
from core.utility.strings import str_admin_command
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

@core.decorators.public_command.init
def init(update, context):
    bot = context.bot
    keyboard = [[InlineKeyboardButton("Risolto✅", callback_data='resolved')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message = update.message.text[7:]
    if message != "":
        chatid = str(update.message.chat.id)[3:]
        update.message.reply_text("<b>Segnalazione effettuata!\nUn admin prenderà in carico la tua richiesta</b>",
        parse_mode='HTML')
        bot.send_message(Config.STAFF_GROUP,str_admin_command.HELP_MESSAGE
        .format(message,
        username="@"+update.message.from_user.username,
        msgid=update.message.message_id,
        chat_title=update.message.chat.title,
        chatid=chatid,
        linkurl="https://t.me/c/"),
        parse_mode='HTML',
        reply_markup=reply_markup)
        bot.send_message(Config.LOG_CHANNEL,str_admin_command.HELP_MESSAGE
        .format(message,
        username="@"+update.message.from_user.username,
        msgid=update.message.message_id,
        chat_title=update.message.chat.title,
        chatid=chatid,
        linkurl="https://t.me/c/"),
        parse_mode='HTML')
    else:
        bot.send_message(update.message.chat_id,str_admin_command.ERROR_MESSAGE)


def resolved(update, context):
    query = update.callback_query
    var_messaggio = query.message.text
    var_messaggio = query.message.text[6:]
    query.edit_message_text(text="{}\n<b>Risolto da: @{username}</b>"
    .format(var_messaggio,username=str(update.effective_user.username)),parse_mode='HTML')