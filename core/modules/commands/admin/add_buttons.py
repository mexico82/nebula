import core.decorators
from core.sql.db_connect import Connection
from core.sql.commands_sql import Sql_Add_Buttons
from core.utility.strings import str_service

@core.decorators.admin.user_admin
@core.decorators.public_command.init
@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    chatid = str(update.message.chat_id)
    button_text = update.message.text[4:].strip()
    if button_text != "":
        x = button_text.split(',')
        connector = Connection()
        query = Sql_Add_Buttons.SQL
        connector.cur.execute(query,[x[0],x[1],chatid])
        bot.send_message(update.message.chat_id,"Hai aggiunto un bottone al menu Welcome!")
    else:
        bot.send_message(update.message.chat_id,str_service.BUTTONS_INSERT,parse_mode='HTML')