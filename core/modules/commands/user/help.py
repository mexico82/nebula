from config import Config

def init(update, context):
    bot = context.bot
    help_message = "@{} HELP:\n\nWELCOME SETTINGS:\n"\
                   "<code>/setwelcome set the welcome for your group</code>\n"\
                   "<code>/listwelcome	watch your welcome by group</code>\n"\
                   "<code>/updatewelcome	update your welcome by group</code>\n"\
                   "<code>/add BUTTON,example.com	add button into welcome</code>\n"\
                   "<code>/listbutton	remove and see the welcome buttons</code>"
    bot.send_message(update.message.chat_id,help_message.format(bot.username), parse_mode='HTML')