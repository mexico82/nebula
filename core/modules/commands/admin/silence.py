import core.decorators
from telegram import ChatPermissions
from core.utility.strings import str_admin_command
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

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
    keyboard = [[InlineKeyboardButton("Unsilence", callback_data='unsilence_button')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.set_chat_permissions(update.message.chat_id,permission)
    bot.send_message(update.message.chat_id,str_admin_command.SILENCE_MESSAGE,reply_markup=reply_markup,parse_mode='HTML')

@core.decorators.admin.user_admin
def unsilence_button(update,context):
    bot = context.bot
    perm_true = ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_polls=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True,
        can_change_info=False,
        can_invite_users=False,
        can_pin_messages=False)
    message = str_admin_command.UNSILENCE_MESSAGE
    query = update.callback_query
    query.answer()
    bot.set_chat_permissions(update.effective_chat.id, perm_true)
    query.edit_message_text(message,parse_mode='HTML')