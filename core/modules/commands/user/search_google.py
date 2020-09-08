def init(update, context):
    bot = context.bot
    message=str(update.message.text[7:]).strip()
    if message != "":
        bot.send_message(update.message.chat_id,
                     text="https://www.google.com/search?&q={0}"
                     .format(message.replace(' ','+')),
                     parse_mode='HTML')
    else:
        bot.send_message(update.message.chat_id, text="Devi digitare un criterio di ricerca!")