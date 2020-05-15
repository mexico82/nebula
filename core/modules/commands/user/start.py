import core.decorators
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

@core.decorators.private_command.init
def init(update, context):
    bot = context.bot
    keyboard = [[InlineKeyboardButton("Welcome Help", callback_data='welcome_button'),
    InlineKeyboardButton("Admin Commands", callback_data='admin_command')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Hi I am @{} if you need help press the buttons below'
    .format(bot.username),reply_markup=reply_markup)

def welcome_button(update, context):
    help_message = "WELCOME SETTINGS:\n"\
                   "<code>/setwelcome set the welcome for your group</code>\n"\
                   "<code>/listwelcome	watch your welcome by group</code>\n"\
                   "<code>/updatewelcome	update your welcome by group</code>\n"\
                   "<code>/add BUTTON,example.com	add button into welcome</code>\n"\
                   "<code>/listbutton	remove and see the welcome buttons</code>"
    keyboard = [[InlineKeyboardButton("Back", callback_data='back_button')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    query.answer()
    query.edit_message_text(help_message,reply_markup=reply_markup,parse_mode='HTML')

def admin_command(update,context):
    help_message = "LIST ADMIN COMMANDS:\n"\
                   "<b>[text] = text to insert</b>\n"\
                   "<code>/a [text] announcement</code>\n"\
                   "<code>/ban ban the user</code>\n"\
                   "<code>/mute	mute the user</code>\n"\
                   "<code>/unmute unmute the user</code>\n"\
                   "<code>/kick	kick the user</code>\n"\
                   "<code>/setpin [text] set pin message by bot</code>\n"\
                   "<code>/pin pin message by bot</code>"
    keyboard = [[InlineKeyboardButton("Back", callback_data='back_button')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    query.answer()
    query.edit_message_text(help_message,reply_markup=reply_markup,parse_mode='HTML')

def back_button(update, context):
    bot = context.bot
    keyboard = [[InlineKeyboardButton("Welcome Help", callback_data='welcome_button'),
    InlineKeyboardButton("Admin Commands", callback_data='admin_command')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    query.answer()
    query.edit_message_text('Hi I am @{} if you need help press the buttons below'
    .format(bot.username),reply_markup=reply_markup)