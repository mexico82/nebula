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
        usr_control = str(update.effective_user.id)
        query = Sql_reputation.SQL_Select
        dbsel.cur.execute(query,(usr,chat))
        rows = dbsel.cur.fetchall()
        if rows:
            for score in rows:
                if score[1] == usr_control:
                    bot.send_message(chat, "Non puoi votarti da solo!")
                elif score[1] != usr_control:
                    dbup = Connection()
                    sql = Sql_reputation.SQL_Update
                    dbup.cur.execute(sql,(usr,chat))
                    message = '<a href="tg://user?id={userid}">{user}</a> hai votato {usr_vote} !'.format(
                        userid=usr_control,
                        user=update.effective_user.username or update.effective_user.first_name,
                        usr_vote=usr_format)
                    bot.send_message(chat,message,parse_mode='HTML')
        else:
            bot.send_message(chat, "L'utente non è abilitato alle votazioni!")
    except:
        bot.send_message(chat, "Questo comando si utilizza in risposta ad un utente!")