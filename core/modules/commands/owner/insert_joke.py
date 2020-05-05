import core.decorators
from core.sql.db_connect import Connection
from core.sql.commands_sql import Sql_Insert_J

@core.decorators.admin.init
@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    message = update.message.text[8:]
    connector = Connection()
    query = Sql_Insert_J.SQL_1
    connector.cur.execute(query, [message])
    row = connector.cur.fetchone()
    if row is None:
        query = Sql_Insert_J.SQL_2
        connector.cur.execute(query,[message])
        connector.db.commit()
    else:
        bot.send_message(update.message.chat_id,
                         text="<b>Perfavore inserisci un'altra battuta questa esiste già!</b>",
                         parse_mode='HTML')
        connector.cur.close()
        connector.db.close()