from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def init(update, context):
  bot = context.bot
  chat = update.effective_chat
  if chat.type != chat.PRIVATE:
    update.effective_message.reply_text("Contact me in PM to get the list of possible commands.",
    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Help",url="t.me/{}?start=help".format(bot.username))]]))
    return