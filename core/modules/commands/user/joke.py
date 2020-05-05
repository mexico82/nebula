import core.decorators
from core.sql.db_connect import Connection
from core.sql.handler_sql import Sql_Joke

@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    connector = Connection()
    query = Sql_Joke.SQL
    connector.cur.execute(query)
    row = connector.cur.fetchone()
    if row is not None:
        bot.send_message(update.message.chat_id, text=row[1], parse_mode='HTML')
        row = connector.cur.fetchone()
        connector.cur.close()
        connector.db.close()