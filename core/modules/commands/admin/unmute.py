import core.decorators
from config import Config
from telegram.ext.dispatcher import run_async
from telegram import ChatPermissions

@core.decorators.admin.user_admin
@core.decorators.bot_admin.bot_admin
@run_async
@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    bot.restrict_chat_member(update.message.chat_id,update.message.reply_to_message.from_user.id,ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_other_messages=True,
    can_add_web_page_previews=True)
    )
    bot.send_message(Config.LOG_CHANNEL,
		text="UTENTE SMUTATO\nUSERNAME: {username}\nID: {id}\nGRUPPO: {chat_title}"
			.format(username="@"+update.message.reply_to_message.from_user.username,
           id=update.message.reply_to_message.from_user.id,
           chat_title=update.message.chat.title)
			, parse_mode='HTML')