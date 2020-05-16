import core.decorators
from config import Config
from telegram.ext.dispatcher import run_async

from cli._ext.argparse import ArgumentParser

@core.decorators.admin.user_admin
@core.decorators.bot_admin.bot_admin
@core.decorators.public_command.init
@run_async
@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    chat = update.message.chat

    user = None

    parser = ArgumentParser()
    parser.add_argument("username",           nargs="?", help="username of user to ban")
    parser.add_argument("-m", "--motivation", nargs="*", help="motiviation of the ban")

    args = update.message.text[5:].strip().split()

    try:
        options = parser.parse_args(args)

        if update.message.reply_to_message:
            user = update.message.reply_to_message.from_user

        if options.username:
            chat.send_message(
                text="<b>Questa operazione non e' ancora implementata!</b>\n" \
                    "\n" \
                    "Stai tentando di eseguire il vecchio ban?\n" \
                    "\n" \
                    "Usa il comando <code>/ban -m motivazione</code> in risposta all'utente che vuoi bannare.",
                parse_mode="HTML"
            )
            return

        if options.motivation:
            for index, word in enumerate(options.motivation):
                options.motivation[index] = word.replace('{}',update.message.from_user.username)

        if ban(bot, chat, user, options):
            if update.message.reply_to_message:
                bot.delete_message(chat.id, update.message.reply_to_message.message_id)

    except Exception as e:
        bot.send_message(Config.LOG_CHANNEL, "%s" % e)
        chat.send_message("%s" % e)
    1

def ban(bot, chat, user, options):
    if not user:
        chat.send_message(
            text="<b>Attenzione l'utente non e' stato trovato!</b>\n" \
                "\n" \
                "Usa il comando <code>/ban -m motivazione</code> in risposta all'utente che vuoi bannare.",
            parse_mode="HTML"
        )
        return False

    if not options.motivation:
        chat.send_message(
            text="<b>Attenzione devi specificare il motivo del ban!</b>" \
                "\n" \
                "Usa il comando <code>/ban -m motivazione</code> in risposta all'utente che vuoi bannare.",
            parse_mode="HTML"
        )
        return False

    if user.id == bot.id:
        chat.send_message(
            text="<b>Attenzione non mi posso bannare da solo!</b>",
            parse_mode="HTML"
        )
        return False

    chat.kick_member(user.id)
    chat.send_message(
        text="{id} è stato <b>bannato</b> da {chat_title}\n" \
            "per il seguente motivo: {motivation}"
            .format(
                id=user.id,
                chat_title=chat.title,
                motivation=options.motivation
            ),
        parse_mode="HTML"
    )
    bot.send_message(Config.LOG_CHANNEL,
        text="<b>UTENTE BANNATO!</b>\n"\
            "ID: {id}\n"\
            "GRUPPO: {chat_title}\n"\
            "MOTIVO: {motivation}"
            .format(
                username=user.first_name,
                id=user.id,
                chat_title=chat.title,
                motivation=options.motivation
            ),
        parse_mode="HTML"
    )
    return True