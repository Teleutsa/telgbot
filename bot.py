import telebot

bot=telebot.TeleBot(token='720384880:AAG1hfSFV6XXau0S4X99WU1mkb7S4ZYKZls')

print(bot.get_me())
def log(message, answer):
    print("\n ------")
    from datetime import datetime
    print( datetime.now())
    print("message from {0} {1}. (id= {2}) \n text- {3}".format(message.from_user.first_name,
                                                                message.from_user.last_name,
                                                                str(message.from_user.id),
                                                                message.text))
    print(answer)
@bot.message_handler(commands=['start'])
def handle_text(message):
    bot.send_message(message.chat.id, """ Керя - Пидор и должен сдохнуть. Мужа Яны ебали он сосал""")

@bot.message_handler (content_types=[ 'text'])

def handle_text(message):
    if message.text.contains("Фен" or "фен") :
        bot.send_message(message.chat.id, "ух бля. Где?")
        bot.send_sticker(message.chat.id,sticker=CAADAgADGQADdrwVEoONfod1baECAg)
        bot.send_sticker(message.chat.id,sticker=CAADAgADGwADdrwVEugPesOA677WAg)
    elif message.text.contains("Рок" or "Роцк" or "рок" or "роцк") :
        bot.send_sticker(message.chat.id,sticker=CAADAgADDQADdrwVErT6I6S-qMfAAg)


@bot.message_handler (content_types=[ 'text'])
def handle_text(message):
    if message.text == "кик пидора" or "Кик пидора":
        bot.kick_chat_member(message.chat.id,393058099)
    elif message.text == "добавь пидора" or "Добавь Пидора":
        bot.add_Chat_members(message.chat.id, 393058099)

@bot.message_handler(content_types=['text'])

def handle_text(message):

    if message.text.contains("Рок" or "Роцк" or "рок" or "роцк"):
        bot.send_sticker(message.chat.id, sticker=CAADAgADAwADdrwVEtiQ9qVIudLyAg)
    elif message.text.contains("каблук" or "Каблук"):
        bot.send_sticker(message.chat.id,sticker=CAADAgADCAADdrwVErhBs8fQWsdLAg)

@bot.message_handler(content_types=['text'])

def handle_text(message):

    if message.text.contains("Тема" or "Тёма" or "Бутар" or "Артём" or "Артем" or "тёма" or "артем" or  "артём"):
        bot.send_voice(message.chat.id, voice=CAADAgADAwADdrwVEtiQ9qVIudLyAg)
    elif message.text.contains("каблук" or "Каблук"):
        bot.send_sticker(message.chat.id,sticker=CAADAgADCAADdrwVErhBs8fQWsdLAg)


bot.polling(none_stop= True,interval=0)
