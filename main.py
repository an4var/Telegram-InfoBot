import telebot
import datetime
from config import TOKEN
from menus import show_main_menu
from handlers import register_handlers

bot = telebot.TeleBot(TOKEN)

# Старт
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 Привіт! Радий бачити тебе в моєму FAQ-боті!")
    show_main_menu(bot, message.chat.id)

register_handlers(bot)

print(f"✅ Бот запущено: {datetime.datetime.now()}")

bot.polling()