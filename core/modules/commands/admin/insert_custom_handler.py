import core.decorators
from core.sql.db_connect import Connection
from core.sql.commands_sql import Sql_Insert_CH

#This command allows to create a question and answer with the bot and it got the following parameters:
# {username} ; {chat_title} ; {first_name}
@core.decorators.admin.user_admin
@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    connector = Connection()
    chatid = str(update.message.chat_id)
    var_question = str(update.message.reply_to_message.text).lower()
    var_answer = str(update.message.text[12:]).lower()
    query = Sql_Insert_CH.SQL_1
    connector.cur.execute(query, [var_answer,chatid])
    row = connector.cur.fetchone()
    if row is None:
        query = Sql_Insert_CH.SQL_2
        connector.cur.execute(query, (var_question, var_answer,chatid))
        connector.db.commit()
    else:
        bot.send_message(update.message.chat_id,
                         text="<b>Perfavore inserisci un'altra risposta questa esiste già!</b>",
                         parse_mode='HTML')
        connector.cur.close()
        connector.db.close()