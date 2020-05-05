import re
import core.decorators

@core.decorators.public_command.init
def init(update, context):
    bot = context.bot
    text = update.message.text
    regex = r"[^\x00-\x7F\x80-\xFF\u0100-\u017F\u0180-\u024F\u1E00-\u1EFF]"
    matches = re.search(regex, text, re.UNICODE)
    if matches:
        bot.send_message(update.message.chat_id, "{} I caratteri Non Latin non sono accettati!".format(update.message.from_user.first_name))
        bot.delete_message(update.message.chat_id, update.message.message_id)
        bot.kick_chat_member(update.message.chat_id, update.message.from_user.id)