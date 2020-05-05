import core.decorators
from core.sql.db_connect import Connection
from core.sql.commands_sql import Sql_Insert_Rules
from core.utility.strings import str_service
from telegram.ext.dispatcher import run_async


@core.decorators.admin.init
@core.decorators.public_command.init
@run_async
@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    message = str(update.message.text[9:]).strip()
    if message != "":
        chatid = str(update.message.chat_id)
        connector = Connection()
        query= Sql_Insert_Rules.SQL
        connector.cur.execute(query, [message,chatid])
        connector.db.commit()
        bot.send_message(update.message.chat_id,
                         text="Hai creato il regolamento del gruppo",
                         parse_mode='HTML')
    else:
        bot.send_message(update.message.chat_id,str_service.RULES_HELP,
                         parse_mode='HTML')