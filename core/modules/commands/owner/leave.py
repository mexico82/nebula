import core.decorators

@core.decorators.owner.init
def init(update, context):
    bot = context.bot
    bot.leaveChat(update.message.chat_id)