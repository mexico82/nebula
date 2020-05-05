import core.decorators
from config import Config

@core.decorators.private_command.init
def init(update, context):
    update.message.reply_text('Ciao sono {bot} \n'\
        'creata da InfocomTeam\nSorgente: {repo}'
                              .format(repo=Config.SOURCE,
                              bot=Config.BOT_USER))