import config
import telebot

API_TOKEN = '8668686105:AAHZy4gfevC1kJYzfEZ8W1KTA_Lhe7qVfds'

bot = telebot.TeleBot(API_TOKEN)


# Обработка команд '/start' и '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет, я EchoBot.
Я здесь для того, чтобы повторить ваши добрые слова. Просто скажите что-нибудь приятное, и я отвечу вам тем же!\
""")


# Обработка всех остальных сообщений с типом контента 'text' (по умолчанию для content_types используется ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

@bot.message_handler(commands=['slog'])
def slog(message):
    a = int(input())
    b = int(input())
    c = a + b
    bot.reply_to(message, c)

@bot.message_handler(content_types=['new_chat_members'])
def make_some(message):
    bot.send_message(message.chat.id, 'I accepted a new user!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)

bot.infinity_polling()