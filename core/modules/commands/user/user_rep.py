import core.decorators
from core.sql.db_connect import Connection
from core.sql.commands_sql import Sql_reputation

@core.decorators.public_command.init
@core.decorators.delete.init
def init(update, context):
    try:
        bot = context.bot
        dbsel = Connection()
        chat = update.effective_chat.id
        usr = str(update.message.reply_to_message.from_user.id)
        msg_usr = update.message.reply_to_message.from_user
        usr_format = "@"+msg_usr.username or msg_usr.first_name
        query = Sql_reputation.SQL_Select
        dbsel.cur.execute(query,(usr,chat))
        row = dbsel.cur.fetchone()
        if row is not None:
            dbup = Connection()
            sql = Sql_reputation.SQL_Update
            dbup.cur.execute(sql,(usr,chat))
            message = "Hai votato {} !".format(usr_format)
            bot.send_message(chat,message,parse_mode='HTML')
        else:
            bot.send_message(chat, "L'utente non è abilitato alle votazioni!")
    except:
        bot.send_message(chat, "Questo comando si utilizza in risposta ad un utente!")