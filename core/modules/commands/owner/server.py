#!/usr/bin/python
import core.decorators
import psutil
from core.utility.strings import str_service

@core.decorators.owner.init
@core.decorators.delete.init
def init(update, context):
        bot = context.bot
        bot.send_message(update.message.chat_id,str_service.SERVER_MESSAGE
                         .format(cpu=psutil.cpu_percent(),
                                 ram=psutil.virtual_memory()[2]),
                         parse_mode='HTML')