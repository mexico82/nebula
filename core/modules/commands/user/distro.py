import core.decorators
import requests
from bs4 import BeautifulSoup

@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    r = requests.get("https://distrowatch.com/random.php")
    parsed_html = BeautifulSoup(r.text, features="html.parser")
    distro_long_name = parsed_html.title.string[17:].lower()
    distro_name = distro_long_name.split()[0]
    distro_url = f'https://distrowatch.com/table.php?distribution={distro_name}'
    bot.send_message(update.message.chat_id, text=distro_url)