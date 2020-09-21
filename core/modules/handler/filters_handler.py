import core.decorators

@core.decorators.public_command.init
def exe(update, context):
    bot = context.bot
    bot.send_message(update.message.chat_id, "I file .exe non sono ammessi!")
    bot.delete_message(update.message.chat_id, update.message.message_id)