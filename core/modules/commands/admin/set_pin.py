import core.decorators
from core.sql.db_connect import Connection
from core.sql.commands_sql import Sql_Pin

@core.decorators.admin.user_admin
@core.decorators.bot_admin.bot_admin
@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    message = update.message.text[7:]
    connector = Connection()
    chatid = str(update.message.chat_id)
    query = Sql_Pin.SQL_SET
    connector.cur.execute(query, [message,chatid])
    connector.cur.close()
    connector.db.close()
    bot.send_message(update.message.chat_id, text="<b>Hai salvato il seguente pin per il tuo gruppo:</b>\n\n{}"
			.format(message), parse_mode='HTML')