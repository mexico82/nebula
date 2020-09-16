import core.decorators
from core.sql.db_connect import Connection
from core.sql.handler_sql import Sql_Welcome

@core.decorators.owner.init
def init(update, context):
    chat = update.effective_message.chat_id
    user = update.effective_user.id
    row = Connection().getUserById([user])
    message = "{}".format(row[0])
    context.bot.send_message(chat,message)