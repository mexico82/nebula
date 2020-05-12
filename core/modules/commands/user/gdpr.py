import core.decorators
from core.sql.db_connect import Connection
from core.sql.commands_sql import Sql_GDPR

@core.decorators.delete.init
def init(update,context):
    bot = context.bot
    u_id = str(update.message.from_user.id)
    connector = Connection()
    query = Sql_GDPR.SQL
    connector.cur.execute(query,[u_id])
    bot.send_message(update.message.chat_id,
    text="You have been deleted from our database")