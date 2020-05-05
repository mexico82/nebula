import core.decorators
from config import Config

@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    bot.send_message(update.message.chat_id, text="<b>     @{botname}</b>\n"
                                          "====================\n\n"
                                          "<b>Linguaggio:</b> <em>Python</em>\n\n"
                                          "<b>Versione</b>:<em>{source}</em>\n\n"
                                          "<b>Developer</b>:<em>{author}</em>\n\n"
                                            "<b>Sorgente</b>:<a href=\"{repo}\"> GitHub</a>"
                                          .format(source=Config.VERSION,
                                                  repo=Config.SOURCE,
                                                  author=Config.AUTHOR,
                                                  botname = bot.username),
                                          parse_mode = 'HTML')