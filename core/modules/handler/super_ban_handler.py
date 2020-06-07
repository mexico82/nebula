from config import Config
import core.decorators
from core.sql.db_connect import Connection
from core.sql.handler_sql import Sql_Super_Ban
from telegram.ext.dispatcher import run_async

#SuperBan
@core.decorators.bot_admin.bot_admin
@run_async
def init(update, context):
    bot = context.bot
    connector = Connection()
    chat = update.message.chat_id
    ban_user = str(update.effective_user.id)
    query = Sql_Super_Ban.SQL
    connector.cur.execute(query, [ban_user])

    rows = connector.cur.fetchall()
    if rows:
        bot.send_message(chat,
            text="<b>The superban has banned:</b> <code>{id}!</code>".format(id=update.message.from_user.id),
            parse_mode='HTML')
        bot.delete_message(chat, update.message.message_id)
        bot.kick_chat_member(chat,update.message.from_user.id)