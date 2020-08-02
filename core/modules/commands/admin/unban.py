import core.decorators

@core.decorators.admin.user_admin
@core.decorators.bot_admin.bot_admin
@core.decorators.public_command.init
@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    chat = update.effective_message.chat_id
    reply = update.message.reply_to_message
    if reply is not None:
        message = "Ban removed to: <code>{}</code>".format(reply.from_user.id)
        bot.send_message(chat, message, parse_mode='HTML')
        bot.unban_chat_member(chat, reply.from_user.id)
    else:
        bot.send_message(chat, text="You must use this command in response to a user!")