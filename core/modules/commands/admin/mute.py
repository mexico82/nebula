import core.decorators
from config import Config
from telegram.ext.dispatcher import run_async
from telegram import ChatPermissions

#FUNCTION MUTE
@core.decorators.admin.user_admin
@core.decorators.bot_admin.bot_admin
@run_async
@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    var_message = update.message.text[5:]
    if var_message != "":
        bot.restrict_chat_member(update.effective_chat.id,
                                update.message.reply_to_message.from_user.id,
                                ChatPermissions(
        can_send_messages=False,
        can_send_media_messages=False,
        can_send_other_messages=False,
        can_add_web_page_previews=False)
        )
        bot.send_message(Config.LOG_CHANNEL,
            text="UTENTE MUTATO\nUSERNAME: {username}\nID: {id}\nGRUPPO: {chat_title}\n\nMOTIVO: {motivation}"
                .format(username="@"+update.message.reply_to_message.from_user.username,
                id=update.message.reply_to_message.from_user.id,
                chat_title=update.message.chat.title,
                motivation=var_message)
                , parse_mode='HTML')
    else:
        bot.send_message(update.message.chat_id,
                         text="<b>Attenzione devi specificare una motivazione per il comando</b>"\
                         "<code>/muta</code>\n Il formato corretto è <code>/muta motivo</code>",
                         parse_mode='HTML')