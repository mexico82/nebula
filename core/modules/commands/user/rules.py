import core.decorators
from core.utility.strings import str_service
from core.sql.db_connect import Connection
from core.sql.commands_sql import Sql_Rules

activationWords = ["regole", "regola", "regolamento", "rules"]

@core.decorators.delete.init
def action(update, context):
    bot = context.bot
    connector = Connection()
    chatid = str(update.message.chat_id)
    query = Sql_Rules.SQL
    connector.cur.execute(query,[chatid])
    row = connector.cur.fetchone()
    if row is not None:
        rules_message = "{}".format(row[0])
        bot.send_message(update.message.chat_id,rules_message, parse_mode='HTML')
    else:
        bot.send_message(update.message.chat_id,str_service.RULES_MESSAGE,parse_mode='HTML')