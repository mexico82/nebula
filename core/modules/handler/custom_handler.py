from core.sql.db_connect import Connection
from core.sql.handler_sql import Sql_Custom_Handler

#This command calls the answers from the database, watch:/core/modules/commands/admin/insert_custom_handler.py
def customhandler(update, context):
    connector = Connection()
    chatid = str(update.message.chat_id)
    var_answer = str(update.message.text).lower()
    query = Sql_Custom_Handler.SQL
    connector.cur.execute(query, ([var_answer],[chatid]))
    row = connector.cur.fetchone()
    if row is not None:
        parsed_message = row[0].replace('{first_name}',
		update.message.from_user.first_name).replace('{chat_title}',
		update.message.chat.title).replace('{username}',
		"@"+update.message.from_user.username)
        message = "{}".format(parsed_message)
        update.message.reply_text(text=message, parse_mode='HTML')
        row = connector.cur.fetchone()
        connector.cur.close()
        connector.db.close()