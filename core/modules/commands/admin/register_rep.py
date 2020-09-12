import core.decorators
from core.sql.db_connect import Connection
from core.sql.commands_sql import Sql_reputation

@core.decorators.admin.user_admin
@core.decorators.bot_admin.bot_admin
@core.decorators.public_command.init
@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    dbsel = Connection()
    chat = update.effective_chat.id
    usr = str(update.message.reply_to_message.from_user.id)
    msg_usr = update.message.reply_to_message.from_user
    usr_format = "@"+msg_usr.username or msg_usr.first_name
    query = Sql_reputation.SQL_Select
    dbsel.cur.execute(query,(usr,chat))
    row = dbsel.cur.fetchone()
    if row is None:
        dbins = Connection()
        default_rep = '0'
        sql = Sql_reputation.SQL_Insert
        dbins.cur.execute(sql,(usr,chat,default_rep))
        message = "{} Ora sei abilitato alle votazioni !".format(usr_format)
        bot.send_message(chat,message,parse_mode='HTML')
    else:
        bot.send_message(chat, "Questo utente è già abilitato alle votazioni!")