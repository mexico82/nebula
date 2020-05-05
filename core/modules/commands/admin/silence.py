import core.decorators
from telegram import ChatPermissions
from core.utility.strings import str_admin_command
permission = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages=False,
    can_send_polls=False, can_send_other_messages=False,
    can_add_web_page_previews=False, can_change_info=False,
    can_invite_users=False, can_pin_messages=False)

@core.decorators.admin.user_admin
@core.decorators.bot_admin.bot_admin
@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    bot.set_chat_permissions(update.message.chat_id,permission)
    bot.send_message(update.message.chat_id,str_admin_command.SILENCE_MESSAGE,parse_mode='HTML')