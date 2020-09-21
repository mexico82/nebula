import core.decorators
from core.sql.repository.group import GroupRepository

@core.decorators.owner.init
def init(update, context):
    chat = update.effective_message.chat_id
    row = GroupRepository().getById([chat])
    message = "{}".format(row[0])
    context.bot.send_message(chat,message)