import core.decorators
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

MASTER_KEYBOARD = [[
    InlineKeyboardButton("Welcome Help", callback_data='welcome_button'),
    InlineKeyboardButton("Admin Commands", callback_data='admin_command'),
    InlineKeyboardButton("User Commands", callback_data='user_command')
    ]]
BACK_BUTTON = [[InlineKeyboardButton("Back", callback_data='back_button')]]

@core.decorators.private_command.init
def init(update, context):
    bot = context.bot
    reply_markup = InlineKeyboardMarkup(MASTER_KEYBOARD)
    update.message.reply_text('Hi I am @{} if you need help press the buttons below'
    .format(bot.username),reply_markup=reply_markup)

def welcome_button(update, context):
    help_message = "WELCOME SETTINGS:\n"\
                   "<code>/setwelcome set the welcome for your group</code>\n"\
                   "<code>/listwelcome	watch your welcome by group</code>\n"\
                   "<code>/updatewelcome	update your welcome by group</code>\n"\
                   "<code>/add BUTTON,example.com	add button into welcome</code>\n"\
                   "<code>/listbutton	remove and see the welcome buttons</code>"
    reply_markup = InlineKeyboardMarkup(BACK_BUTTON)
    query = update.callback_query
    query.answer()
    query.edit_message_text(help_message,reply_markup=reply_markup,parse_mode='HTML')

def admin_command(update,context):
    help_message = "LIST ADMIN COMMANDS:\n"\
                   "<b>[text] = text to insert</b>\n"\
                   "<code>/a [text] announcement</code>\n\n"\
                   "BAN COMMAND:\n"\
                   "<code>/ban -m [text] or /ban @username -m [text] ban the user</code>\n"\
                   "<code>/unban Remove the ban from a user</code>\n"\
                   "<code>/info Username info and Chat Info</code>\n"\
                   "<code>/mute	mute the user</code>\n"\
                   "<code>/unmute unmute the user</code>\n"\
                   "<code>/kick	kick the user in the group</code>\n"\
                   "<code>/setpin [text] set pin message by bot</code>\n"\
                   "<code>/pin pin message by bot in your group</code>\n"\
                   "<code>/warn warn the user(Beta)</code>\n"\
                   "<code>/badword [text] Add badword in your group</code>\n"\
                   "<code>/badlist Badword List</code>"\
                   "<code>/silence Mute the whole group</code>"\
                   "<code>/delete This command deletes a message</code>"\
                   "<code>/say [text] Get the bot talking</code>"\
                   "<code>/enable enables voting for a user in the group</code>"
    reply_markup = InlineKeyboardMarkup(BACK_BUTTON)
    query = update.callback_query
    query.answer()
    query.edit_message_text(help_message,reply_markup=reply_markup,parse_mode='HTML')

def user_command(update,context):
    help_message = "LIST USER COMMANDS:\n"\
                   "<b>[text] = text to insert , Example: /wikipedia New York</b>\n"\
                   "<code>/wikipedia [text] wikipedia</code>\n"\
                   "<code>/distro random Linux Distro by DistroWatch</code>\n"\
                   "<code>/joke	Random Humor(Only Italian)</code>\n"\
                   "<code>/io Your Information</code>\n"\
                   "<code>/source Github Source Code</code>\n"\
                   "<code>/feedback [text] feedback</code>\n"\
                   "<code>/help see help</code>\n"\
                   "<code>/rules or /regole group rules</code>\n"\
                   "<code>/cerca [text] Search into Qwant</code>\n"\
                   "<code>/google [text] Search into Google</code>\n"\
                   "<code>/staff See group staff</code>\n"\
                   "<code>/gdpr Delete you in database</code>"\
                   "<code>/traduci Translate from Italian to English</code>"\
                   "<code>/vote or /downvote Vote for a user or Remove a user's vote</code>"\
                   "<code>/score View your score in the group</code>"
    reply_markup = InlineKeyboardMarkup(BACK_BUTTON)
    query = update.callback_query
    query.answer()
    query.edit_message_text(help_message,reply_markup=reply_markup,parse_mode='HTML')

def back_button(update, context):
    bot = context.bot
    reply_markup = InlineKeyboardMarkup(MASTER_KEYBOARD)
    query = update.callback_query
    query.answer()
    query.edit_message_text('Hi I am @{} if you need help press the buttons below'
    .format(bot.username),reply_markup=reply_markup)