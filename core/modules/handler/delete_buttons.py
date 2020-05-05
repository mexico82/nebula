import core.decorators
from core.sql.db_connect import Connection
from core.sql.commands_sql import Sql_Buttons

RECEIVE_ID = range(2)

@core.decorators.admin.user_admin
def init(update, context):
    chatid = str(update.message.chat_id)
    connector = Connection()
    query = Sql_Buttons.SQL_1
    connector.cur.execute(query,[chatid])
    rows = connector.cur.fetchall()
    string = ""
    for link in rows:
        string += f"<code>{link[0]}:</code> <a href=\"{link[2]}\">{link[1]}</a>\n"
    message = "Ok, rispondi a questo messaggio con gli ID per i link(pulsanti) che vuoi eliminare. Nel formato " \
              "<code>0,1,2</code>. Non scrivere nient'altro nel messaggio. Oppure usa /cancel"
    update.effective_message.reply_html(message + "\n\nLista bottoni:\n" + string)
    return RECEIVE_ID

@core.decorators.admin.user_admin
def receive_id(update, context):
    chatid = str(update.message.chat_id)
    connector = Connection()
    ids = update.effective_message.text.split(", ")
    for actual_id in ids:
         query = Sql_Buttons.SQL_2
         connector.cur.execute(query,[actual_id,chatid])
    update.effective_message.reply_text("Ho cancellato i bottoni!")
    return -1

@core.decorators.admin.user_admin
def cancel(update, context):
    update.effective_message.reply_text("CANCELLED!")
    return -1