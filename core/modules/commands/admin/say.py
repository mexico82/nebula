import core.decorators

@core.decorators.admin.user_admin
@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    try:
        message = update.message.text[4:]
        bot.send_message(update.message.chat_id,
                         text='{}'.format(message),
                         parse_mode='HTML')
    except:
        bot.send_message(update.message.chat_id,
        text="<b>Non hai scritto alcun messaggio!"\
            "Riprova scrivendo un messaggio dopo il comando /say</b>",
            parse_mode='HTML')