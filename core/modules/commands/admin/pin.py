import core.decorators
from core.sql.db_connect import Connection
from core.sql.commands_sql import Sql_Pin


@core.decorators.admin.user_admin
@core.decorators.bot_admin.bot_admin
@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    chatid = str(update.message.chat_id)
    connector = Connection()
    query = Sql_Pin.SQL
    connector.cur.execute(query,[chatid])
    row = connector.cur.fetchone()
    message_text = "{}".format(row[0])
    bot.send_message(update.message.chat_id, text=message_text, parse_mode='HTML')
    bot.pin_chat_message(update.message.chat_id, update.message.message_id+1,
        disable_notification=True)
    connector.cur.close()
    connector.db.close()