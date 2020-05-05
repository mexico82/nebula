import core.decorators
@core.decorators.public_command.init
@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    message=str(update.message.text[6:]).strip()
    if message != "":
        bot.send_photo(update.message.chat_id,
                   photo="https://www.qwant.com/QWANT_Meta.png?1563875041675",
                   caption="<b>WEB:</b> https://www.qwant.com/?q={0}&t=web\n"\
                       "<b>IMMAGINI:</b> https://www.qwant.com/?q={0}&t=images\n"\
                   "<b>VIDEO:</b> https://www.qwant.com/?q={0}&t=videos"
                   .format(message.replace(' ','+')),
                   parse_mode='HTML')
    else:
        bot.send_message(update.message.chat_id, text="Devi digitare un criterio di ricerca!")