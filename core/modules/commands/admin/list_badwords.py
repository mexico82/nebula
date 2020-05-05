import core.decorators
from core.sql.db_connect import Connection
from core.sql.handler_sql import Sql_Badword_Select

@core.decorators.admin.user_admin
def init(update, context):
    connector = Connection()
    chatid = str(update.message.chat_id)
    query = Sql_Badword_Select.SQL
    connector.cur.execute(query,[chatid])
    rows = connector.cur.fetchall()
    string = ""
    for link in rows:
        string += f"<code>{link[0]}:</code> <a href=\"{link[2]}\">{link[1]}</a>\n"
    message = "Ecco la lista delle parole proibite per questo gruppo:"
    update.effective_message.reply_html(message + "\n\nLista badwords:\n" + string)