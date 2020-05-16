import core.decorators
from core.sql.db_connect import Connection
from core.sql.commands_sql import Sql_Warn
from core.utility.strings import str_service

@core.decorators.admin.user_admin
@core.decorators.delete.init
def init(update,context):
    bot = context.bot
    connector = Connection()
    usr = str(update.message.reply_to_message.from_user.id)
    chat = str(update.message.chat_id)
    default_count = '1'
    msg_usr = update.message.reply_to_message.from_user
    usr_format = "@"+msg_usr.username or msg_usr.first_name
    query = Sql_Warn.SQL_Sel_Warn
    connector.cur.execute(query,(usr,chat))
    row = connector.cur.fetchone()

    if row is None:
        save_warn = Connection()
        insert_warn = Sql_Warn.SQL_Ins_Warn
        save_warn.cur.execute(insert_warn,(usr,default_count,chat))
        bot.send_message(update.message.chat_id,str_service.WARN_START
        .format(usr_format))
        return True
    elif row[0] == '1':
        Connection().cur.execute(Sql_Warn.SQL_Upd_Warn,(usr,chat))
        bot.send_message(update.message.chat_id,str_service.WARN_1
        .format(usr_format))
    elif row[0] == '2':
        Connection().cur.execute(Sql_Warn.SQL_Upd_Warn,(usr,chat))
        bot.send_message(update.message.chat_id,str_service.WARN_2
        .format(usr_format))
    elif row[0] == '3':
        bot.send_message(update.message.chat_id,str_service.WARN_END
        .format(usr_format))
        bot.kick_chat_member(update.message.chat_id,update.message.reply_to_message.from_user.id)