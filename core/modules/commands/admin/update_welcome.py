import core.decorators
from core.sql.db_connect import Connection
from core.sql.commands_sql import Sql_Update_W
from core.utility.strings import str_service

@core.decorators.admin.user_admin
@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    message = str(update.message.text[14:])
    if message != "":
        chatid = str(update.message.chat_id)
        connector = Connection()
        query= Sql_Update_W.SQL
        connector.cur.execute(query, (message,chatid))
        connector.db.commit()
        bot.send_message(update.message.chat_id,
                         text="Hai aggiornato correttamente il messaggio di Benvenuto!",
                         parse_mode='HTML')
    else:
        bot.send_message(update.message.chat_id,str_service.INSERT_W,
                         parse_mode='HTML')