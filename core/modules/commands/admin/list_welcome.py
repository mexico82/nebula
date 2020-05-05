import core.decorators
from core.sql.db_connect import Connection
from core.sql.handler_sql import Sql_Welcome

@core.decorators.admin.user_admin
def init(update, context):
    connector = Connection()
    chatid = str(update.message.chat_id)
    query = Sql_Welcome.SQL
    connector.cur.execute(query,[chatid])
    row = connector.cur.fetchone()
    if row is not None:
        message = "<b>Ecco il welcome del tuo gruppo:</b>\n<code>{}</code>".format(row[0])
        update.effective_message.reply_html(message)
    else:
        update.effective_message.reply_html("Non hai impostato nessun Welcome per questo gruppo!")