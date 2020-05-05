import core.decorators
from config import Config
from telegram.ext.dispatcher import run_async

@core.decorators.admin.user_admin
@core.decorators.bot_admin.bot_admin
@core.decorators.public_command.init
@run_async
@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    var_message = update.message.text[4:].replace('{}',update.message.from_user.username)
    if var_message != "":
        bot.send_message(update.message.chat_id, text="{id} è stato <b>bannato</b> da {chat_title}\n"\
                    "per il seguente motivo: {motivation}".format(
                             id=update.message.reply_to_message.from_user.id,
                             chat_title=update.message.chat.title,
                             motivation=var_message),
                     parse_mode='HTML')
        bot.send_message(Config.LOG_CHANNEL,
                     text="<b>UTENTE BANNATO!</b>\n"\
                                 "ID: {id}\n"\
                                 "GRUPPO: {chat_title}\n"\
                                     "MOTIVO: {motivation}"
                                     .format(username=update.message.reply_to_message.from_user.first_name,
                                             id=update.message.reply_to_message.from_user.id,
                                             chat_title=update.message.chat.title,
                                             motivation=var_message)
                                     ,parse_mode='HTML')
        bot.delete_message(update.message.chat_id, update.message.reply_to_message.message_id)
        bot.kick_chat_member(update.message.chat_id,
                         update.message.reply_to_message.from_user.id)
    else:
        bot.send_message(update.message.chat_id,
                         text="<b>Attenzione devi specificare il motivo del ban!</b>",
                         parse_mode='HTML')