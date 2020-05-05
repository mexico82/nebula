from functools import wraps
from telegram import Chat, ChatMember

def is_bot_admin(chat: Chat, bot_id: int, bot_member: ChatMember = None) -> bool:
    if chat.type == "private" or chat.all_members_are_administrators:
        return True

    if not bot_member:
        bot_member = chat.get_member(bot_id)
    return bot_member.status in ("administrator", "creator")

def bot_admin(func):
    @wraps(func)
    def is_admin(update,context, *args, **kwargs):
        bot = context.bot
        if is_bot_admin(update.effective_chat, bot.id):
            return func(update,context, *args, **kwargs)
        else:
            update.effective_message.reply_text("Non sono admin!")

    return is_admin