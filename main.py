import telebot
import smtp
import asyncio

bot = telebot.TeleBot("6861791009:AAEeKrURb7wLi-ctJBlgwq2Yga3TvZRF_q0")

@bot.message_handler(commands=["start"])
def cmd_start(message):
     bot.send_message(message.chat.id, "Hi! I'm a registration bot for karaoke-quiz LALAFA! What is your team name?")
     bot.register_next_step_handler(message, user_entering_name)

def user_entering_name(message):
    global name
    name = message.text
    bot.send_message(message.chat.id, "Great! How many people are in your team. Please remember we accept team from 4 to 12 people.")
    bot.register_next_step_handler(message, user_entering_count)

def user_entering_count(message):
     global count
     count = message.text
     bot.send_message(message.chat.id, "Nice! Please provide your phone number.")
     bot.register_next_step_handler(message, user_entering_phone)

def user_entering_phone(message):
    global phone
    phone = message.text
    bot.send_message(message.chat.id, "Thanks! Your information was sent to quiz team. They will contact you soon.")
    asyncio.run(smtp.send_mail('New team in TG', 'floridaquiz@gmail.com', f'<p>Team - {name} is {count} people. Phone number - {phone}</p>'))


asyncio.run(bot.polling())

