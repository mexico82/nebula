import core.decorators
from core.utility.strings import str_service

@core.decorators.admin.user_admin
@core.decorators.delete.init
def init(update, context):
        bot = context.bot
        try:
            bot.send_message(update.message.from_user.id,str_service.GET_MESSAGE.format(
                    username="@" + update.message.reply_to_message.from_user.username,
                    id=update.message.reply_to_message.from_user.id,
                    chat_title=update.message.chat.title,
                    idchat=update.message.chat_id),
                    parse_mode='HTML')
        except:
                bot.send_message(update.message.chat_id,text="Devi avviare il bot in privato per questo comando!")