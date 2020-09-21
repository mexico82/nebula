import core.decorators
from core.sql.db_connect import Connection
from core.sql.commands_sql import Sql_Warn

@core.decorators.admin.user_admin
@core.decorators.delete.init
def init(update,context):
    bot = context.bot
    connector = Connection()
    usr = str(update.message.reply_to_message.from_user.id)
    chat = str(update.message.chat_id)
    msg_usr = update.message.reply_to_message.from_user
    usr_format = "@"+msg_usr.username or msg_usr.first_name
    query = Sql_Warn.SQL_Del_Warn
    connector.cur.execute(query,(usr,chat))
    bot.send_message(update.message.chat_id,text="Hai rimosso i warn di {}".format(usr_format))
    bot.unban_chat_member(update.message.chat_id,update.message.reply_to_message.from_user.id)