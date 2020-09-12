import datetime
import core.decorators
from config import Config
from core.sql.db_connect import Connection
from core.sql.commands_sql import Sql_Superban
from core.utility.strings import str_service
from telegram.ext.dispatcher import run_async

@core.decorators.owner.init
@core.decorators.bot_admin.bot_admin
@run_async
@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    message = str(update.message.text[9:])
    if message != "":
        save_user_id = update.message.reply_to_message.from_user.id
        save_date = datetime.datetime.utcnow().isoformat()
        operator_id = update.message.from_user.id
        connector = Connection()
        query= Sql_Superban.SQL
        connector.cur.execute(query, [save_user_id,message,save_date,operator_id])
        connector.db.commit()
        bot.delete_message(update.message.chat_id, update.message.reply_to_message.message_id)
        bot.kick_chat_member(update.message.chat_id, update.message.reply_to_message.from_user.id)
        bot.send_message(update.message.chat_id,
                         text="You got super banned <code>{id}</code> !!!\n Go to https://hersel.it/apinebula.php"
                         .format(id=update.message.reply_to_message.from_user.id),
                         parse_mode='HTML')
    else:
        bot.send_message(update.message.chat_id,str_service.MESSAGE_SB,
                         parse_mode='HTML')