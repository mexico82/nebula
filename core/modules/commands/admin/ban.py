import core.decorators
from config import Config
from telegram import User
from telegram.ext.dispatcher import run_async

from cli._ext.argparse import ArgumentParser
from core.sql.database import DatabaseAccessor

@core.decorators.admin.user_admin
@core.decorators.bot_admin.bot_admin
@core.decorators.public_command.init
@run_async
@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    chat = update.message.chat
    admin: User = update.message.from_user

    user = None

    parser = ArgumentParser()
    parser.add_argument("username",           nargs="?", help="username of user to ban")
    parser.add_argument("-m", "--motivation", nargs="*", help="motiviation of the ban")

    args = update.message.text[4:].strip().split()

    options = parser.parse_args(args)

    if update.message.reply_to_message:
        user = update.message.reply_to_message.from_user

    if options.username:
        row = DatabaseAccessor().getUserIdFrom(username=options.username).fetchall()
        if row is not None:
            data = row[0]
            user = User(data[1], ".", False, username=data[2])
        else:
            bot.send_message( admin.id,
                text="<b>Attenzione: non e' stata trovata alcuna corrispondenza con `{user}`</b>\n" \
                    "\n" \
                    "Stai tentando di eseguire il vecchio ban?\n" \
                    "\n" \
                    "Usa il comando <code>/ban -m motivazione</code> in risposta all'utente che vuoi bannare."
                    .format(
                        user=options.username
                    ),
                parse_mode="HTML"
            )

    if options.motivation:
        for index, word in enumerate(options.motivation):
            options.motivation[index] = word.replace('{}',update.message.from_user.username)

    if ban(bot, chat, admin, user, options):
        if update.message.reply_to_message:
            bot.delete_message(chat.id, update.message.reply_to_message.message_id)

def ban(bot, chat, admin, user, options):
    if not user:
        bot.send_message( admin.id,
            text="<b>Attenzione: l'utente non e' stato trovato!</b>\n" \
                "\n" \
                "Puoi usare il comando <code>/ban -m motivazione</code> in risposta all'utente che vuoi bannare.\n" \
                "\n" \
                "Oppure:\n" \
                "\n" \
                "Puoi usare il comando <code>/ban @username -m motivazione</code>.",
            parse_mode="HTML"
        )
        return False

    if not options.motivation:
        bot.send_message( admin.id,
            text="<b>Attenzione: devi specificare il motivo del ban!</b>\n" \
                "\n" \
                "Puoi usare il comando <code>/ban -m motivazione</code> in risposta all'utente che vuoi bannare.\n" \
                "\n" \
                "Oppure:\n" \
                "\n" \
                "Puoi usare il comando <code>/ban @username -m motivazione</code>.",
            parse_mode="HTML"
        )
        return False

    if user.id == bot.id:
        bot.send_message( admin.id,
            text="<b>Attenzione: non mi posso bannare!</b>",
            parse_mode="HTML"
        )
        return False

    motivation = ' '.join(str(x) for x in options.motivation)

    chat.kick_member(user.id)
    chat.send_message(
     text='<a href="tg://user?id={userid}">{user}</a> è stato <b>bannato</b> da {chat}\n'\
            "per il seguente motivo: {motivation}"
            .format(
                user=user.username or user.first_name,
                userid= user.id,
                chat=chat.title,
                motivation=motivation
            ),
        parse_mode="HTML"
    )
    bot.send_message(Config.LOG_CHANNEL,
        text="<b>UTENTE BANNATO!</b>\n"\
            "ID: {id}\n"\
            "GRUPPO: {chat}\n"\
            "MOTIVO: {motivation}"
            .format(
                username=user.username or user.first_name,
                id=user.id,
                chat=chat.title,
                motivation=motivation
            ),
        parse_mode="HTML"
    )
    return True