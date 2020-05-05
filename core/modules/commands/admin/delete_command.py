import core.decorators

@core.decorators.admin.user_admin
@core.decorators.bot_admin.bot_admin
@core.decorators.delete.bot_delete_controller
@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    bot.delete_message(update.message.chat_id, update.message.reply_to_message.message_id)