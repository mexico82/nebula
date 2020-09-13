import core.decorators
from core.utility.strings import str_request_function

@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    message = update.message.text[9:]
    if message != "":
            bot.send_message(1065189838,str_request_function.HELP_MESSAGE
                             .format(message,
                                     username="@"+update.message.from_user.username),
                             parse_mode='HTML')
    else:
            bot.send_message(update.message.chat_id, str_request_function.ERROR_MESSAGE)