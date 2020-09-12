import core.decorators
from core.sql.db_connect import Connection
from core.sql.commands_sql import Sql_reputation

def init(update, context):
    connector = Connection()
    chatid = str(update.effective_chat.id)
    usr = str(update.effective_user.id)
    sql = Sql_reputation.SQL_Select
    connector.cur.execute(sql,(usr,chatid))
    row = connector.cur.fetchone()
    if row is not None:
        message = "{} il tuo <b>punteggio</b> nella chat {} è di <code>{}</code> punti!".format(update.effective_user.first_name,update.message.chat.title,row[3])
        update.effective_message.reply_html(message)
    else:
        update.effective_message.reply_html("Non sei abilitato al voto!\nContatta un admin per l'abilitazione!")