import core.decorators
from config import Config
import pyowm
from yandex.Translater import Translater

@core.decorators.public_command.init
@core.decorators.delete.init
def init(update, context):
	bot = context.bot
	var_messagge = update.message.text[8:]
	# Variables
	currenttimestr = 'Tempo attuale a '
	citynotfoundstr = 'Non ho trovato la città'
	tempunit = 'celsius'
	tempstr = 'C°'
	lang = 'it'
	# Code
	try:
		tr = Translater()
		tr.set_key(Config.YANDEX_API)
		tr.set_from_lang('en')
		tr.set_to_lang(lang)
		weather = pyowm.OWM(Config.OPENWEATHER_API).weather_at_place(var_messagge.lower().capitalize()).get_weather()
		status = weather.get_status()
		desc = weather.get_detailed_status()
		for a,b in weather.get_temperature(unit=tempunit).items():
			if a == 'temp':
				temp = b
			if a == 'temp_min':
				mintemp = b
			if a == 'temp_max':
				maxtemp = b
		def sendweathermsg(icon):
			msgtext = currenttimestr+var_messagge.lower().capitalize()+':\n\n'
			if icon == '':
				msgtext = msgtext+desc.capitalize()
			else:
				msgtext = msgtext+icon+' '+desc.capitalize()+' '+icon
			msgtext = msgtext+'\nHumidity: '+str(weather.get_humidity())+'%\nTemp: '+str(temp)+tempstr+', Min Temp: '+str(mintemp)+tempstr+', Max Temp: '+str(maxtemp)+tempstr
			tr.set_text(msgtext)
			bot.send_message(update.message.chat_id, text=tr.translate(), parse_mode='HTML')
		if status == 'Clouds':
			sendweathermsg('☁️')
		elif status == 'Clear':
			sendweathermsg('☀️')
		elif status == 'Rain':
			sendweathermsg('🌧')
		elif status == 'Drizzle':
			sendweathermsg('🌧')
		elif status == 'Mist':
			sendweathermsg('🌫')
		else:
			sendweathermsg('')
	except:
		bot.send_message(update.message.chat_id, text=citynotfoundstr, parse_mode='HTML')