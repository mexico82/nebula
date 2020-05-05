from functools import wraps
from telegram import Chat

def init(func):
    @wraps(func)
    def wrapped(update, context):
        bot = context.bot
        if update.message.text is not None:
          if update.message.text.startswith("/"):
              bot.delete_message(update.message.chat_id, update.message.message_id)
        return func(update, context)
    return wrapped

def can_delete(chat: Chat, bot_id: int) -> bool:
    return chat.get_member(bot_id).can_delete_messages

def bot_delete_controller(func):
    @wraps(func)
    def delete_rights(update,context, *args, **kwargs):
        bot = context.bot
        if can_delete(update.effective_chat, bot.id):
            return func(update,context, *args, **kwargs)
        else:
            update.effective_message.reply_text(
                "Non posso cancellare i messaggi qui!\n"\
                "Assicurati di avermi fatto admin.\n"\
                    "E di aver impostato correttamente i miei permessi!"
            )

    return delete_rights