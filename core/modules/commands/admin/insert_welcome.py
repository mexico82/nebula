import core.decorators
from core.sql.db_connect import Connection
from core.sql.commands_sql import Sql_Insert_W
from core.utility.strings import str_service

@core.decorators.admin.user_admin
@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    message = str(update.message.text[11:]).strip()
    if message != "":
        chatid = str(update.message.chat_id)
        default_b = 0
        connector = Connection()
        query= Sql_Insert_W.SQL
        connector.cur.execute(query, (chatid,message,default_b))
        connector.db.commit()
        bot.send_message(update.message.chat_id,
                         text="Hai inserito correttamente il messaggio di Benvenuto!",
                         parse_mode='HTML')
    else:
        bot.send_message(update.message.chat_id,str_service.INSERT_W,
                         parse_mode='HTML')