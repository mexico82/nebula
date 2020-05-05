import core.decorators
from telegram import ChatPermissions


@core.decorators.admin.user_admin
@core.decorators.bot_admin.bot_admin
@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    bot.set_chat_permissions(update.message.chat_id, ChatPermissions(can_send_messages=True, can_send_media_messages=True,
                           can_send_polls=True, can_send_other_messages=True,
                           can_add_web_page_previews=True, can_change_info=False,
                           can_invite_users=False, can_pin_messages=False))
    bot.send_message(update.message.chat_id, text="<b>Silenzio Globale Disattivato!\n</b>"\
                                                  "Gli utenti possono tornare regolarmente a scrivere!",
                                                  parse_mode='HTML')