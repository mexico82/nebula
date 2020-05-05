from core.sql.db_connect import Connection
from core.sql.handler_sql import Sql_Badword

#BAD WORDS FILTER By Concetto & Hersel Giannella
def init(update, context):
    bot = context.bot
    try:
        connector = Connection()
        chatid = str(update.message.chat_id)
        bad_var = str(update.effective_message.text)
        query = Sql_Badword.SQL
        connector.cur.execute(query, [bad_var,chatid])
        rows = connector.cur.fetchall()
        if rows:
            message="{} hai utilizzato una parola proibita!\nLeggi le /regole".format(update.message.from_user.first_name)
            bot.delete_message(update.message.chat_id, update.message.message_id)
            bot.send_message(update.message.chat_id,message)
    except:
        print("questa chat non ha badword")