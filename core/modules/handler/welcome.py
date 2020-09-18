#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright hersel91 <hersel1991@gmail.com>
import time
from telegram.ext.dispatcher import run_async
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.utility import utils
from core.sql.db_connect import Connection
from core.sql.handler_sql import Sql_Welcome,Sql_SaveUser
from core.sql.commands_sql import Sql_Buttons
from core.utility.strings import str_service

@run_async
def init(update, context):
    bot = context.bot
    chat = update.effective_chat.id
    chat_title = update.message.chat.title
    for member in update.message.new_chat_members:
        if not member.is_bot:
            if member.username is not None:
                connector = Connection()
                usr_connector = Connection()
                u_id = str(member.id)
                u_username = str("@"+member.username)
                query = Sql_Welcome.SQL
                save_user = Sql_SaveUser.SQL
                connector.cur.execute(query,[chat])
                usr_connector.cur.execute(save_user,[u_id,u_username])
                row = connector.cur.fetchone()
                if row is not None:
                    parsed_message = row[0].replace('{first_name}',
                    update.message.from_user.first_name).replace('{chat_name}',
                    update.message.chat.title).replace('{username}',
                    "@"+member.username)
                    connector = Connection()
                    db_query = Sql_Buttons.SQL_1
                    connector.cur.execute(db_query,[chat])
                    rows = connector.cur.fetchall()
                    buttons = []
                    for link in rows:
                        buttons.append(InlineKeyboardButton(text=link[1], url=link[2]))
                    menu = utils.build_menu(buttons, 2)
                    welcome_message = "{}".format(parsed_message)
                    update.message.reply_text(welcome_message, reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML')
                else:
                    bot.send_message(chat,str_service.DEFAULT_WELCOME.format(username="@"+member.username,chat=chat_title))

            else:
                bot.send_message(chat,"{} set a username!\n You were kicked for safety!"
                                 .format(update.message.from_user.id))
                bot.kick_chat_member(chat, update.message.from_user.id,until_date=int(time.time()+30))
        else:
            bot.send_message(chat,str_service.BOT_WELCOME.format(chat_title))