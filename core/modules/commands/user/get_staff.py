import core.decorators
from telegram.utils.helpers import escape_markdown
from telegram import ParseMode

@core.decorators.public_command.init
def init(update,context):
    administrators = update.effective_chat.get_administrators()
    text = "Staff *{}*:".format(update.effective_chat.title or "this chat")
    for admin in administrators:
        user = admin.user
        name = "[{}](tg://user?id={})".format(user.first_name + (user.last_name or ""), user.id)
        if user.username:
            name = escape_markdown("@" + user.username)
        text += "\n - {}".format(name)

    update.effective_message.reply_text(text, parse_mode=ParseMode.MARKDOWN)