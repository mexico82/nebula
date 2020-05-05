from core.sql.db_connect import Connection
from core.sql.handler_sql import Sql_Super_Ban

#SuperBan
def init(update, context):
    bot = context.bot
    connector = Connection()
    ban_user = str(update.effective_user.id)
    query = Sql_Super_Ban.SQL
    connector.cur.execute(query, [ban_user])

    rows = connector.cur.fetchall()
    if rows:
        bot.send_message(
            update.message.chat_id,
            text="<b>IL SUPERBAN HA BANNATO:</b> <code>{id}!</code>".format(id=update.message.from_user.id),
            parse_mode='HTML')
        bot.kick_chat_member(update.message.chat_id,
                         update.message.from_user.id)