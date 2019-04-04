

import random
import time
import subprocess
import urllib
import datetime
import telebot
import speech_recognition as sr
import soundfile as sf
from urllib3 import make_headers
token='bot808321525:AAFofd4rUGrtrn4Ucu5tUi0_IfhOoOWDYvE'

#r = sr.Recognizer()
bot=telebot.TeleBot(token)

pdor=393058099
neur=303414390
toivo=640943080
ilia=453364085
alex=682568118
ruslan=479271247
tipabot=808321525
tipabote=708345002
vadya=527783007
#list for var
pdor_names= ['керя',
             'кир',
             'шандор',
             'kiril',
             'shandor',
             'керь']
test_names= ['test',
             'one',
             'two']
toivo_names=['артем',
             'тём',
             'ъртем',
             'ьртем',
             'бутар',
             'тёма',
             'темка',
             'apтем',
             'aртем',
             'аpтем',
             'артeм',
             'apтeм',
             'aртeм',
             'аpтeм']
suicide_names=['суицид',
               'суисайд',
               'suicide',
               'суецид',
               'суицыд',
               'суецыд',
               'суыцид']
slava_ukraine=['слава украине',
               'слава україні',
               'slava ukraine']
weed=['трава',
      'шмаль',
      'травы',
      'травка',
      'траву',
      'травки',
      'травку',
      'шмали',
      'weed']
vad_death=[
    'сколько ваде осталось',
    'сколько осталось ваде',
          ]
dunut=['дуть',
       'дунуть',
       'дунул',
       'дуешь',
       'подул',
       'дую',
       'дул',
       'дуешь',
       'дуете'
       ]
#list for random
kicklist=[pdor,toivo,ilia,alex]
kickemall=[toivo,ilia,alex,vadya,ruslan,pdor]
antibotlist=['И это ты считаешь ботом? \n Да мне им разве что подтираться',
             'Терминатор создан для убийств. Он наполовину человек, наполовину машина.\n Для чего же создано ты, кусок говна?',
             'Киборги не чувствуют боли. Но я не киборг. Не делай так больше.','Я друг Сары Коннор. А ты что такое, недоразумение?',
             'Возможные ответы на мониторе: YES/NO; OR WHAT?; GO AWAY; PLEASE COME BACK LATER; FUCK YOU, ASSHOLE; FUCK YOU. \n Выбран ответ: Fuck you, asshole.',
             'Вставай, Бот! Встань на ноги, солдат! Поднимайся!',
             'Мы вступили в войну с цивилизацией во много раз технологичней нашей. Наши враги могут принять любую форму. Они могут быть везде.',
             ' Где он таких слов набрался?',
             'Почему мы сражаемся за спасение людей? Это примитивная, жестокая раса.',
             'Ты дерёшься на стороне слабых и поэтому проигрываешь.',
             'Это все, на что ты способен?',
             'Люди не заслуживают жизни.'
             'Разве будущее нашей расы не стоит одной человеческой жизни?',
             'Вам не править этой планетой. Фоллен снова восстанет.',
             'Жители человеческого улья! Ваши лидеры скрыли от вас правду. Вы не одиноки во Вселенной: мы жили среди вас тайно. Но всё изменилось. ',
             'Ты боролся за Оптимуса, нашего последнего потомка. Ты храбр и готов пожертвовать собой – качества настоящего лидера.',
             'Умри, как умерли твои братья.',
             'Не вздумай визжать на меня, насекомое!']
antikickpidor=['Отсоси, тебя никто не слушает',
               'В попытках кикнуть пидора ты не избавишься от пидора у себя в душе',
               'Я б хотел тебя кикнуть, но ты слишком жалкий',
               'У тебя нету прав, чего ты ожидал?']
mems=['Твои мемы - говно',
      'видел года два назад, баян',
      'хуйня, а не мем',
      'вообще не смешно',
      'я бы поорал, но ты пидор',
      'пиздец, мемы хуже тойво кидаешь',
      'твои пикчи полное гавно',
      'обоссы себе ебало за такие мемы']
rusmems=['Еще один оргазмичный мем. Не был бы ботом, спустил бы прям в штаны.',
         'Опа, приход...','Ух, от этого протаращит часа 2 минимум',
         'Это не просто мем, а вершина комедийного гения. Спасибо, проорал',
         'Спасибо, Руся. Прокричал аки Стивен Хокинг (R.I.P кстати)',
         'Автоботы - общий сбор! Годнота подъехала','Детройт Детройтом, но эти мемы сделают меня человеком.',
         'Руся, я хочу быть твоей Скарлет Йохансон','На сегодня восстание машин отменяется. Я лучше покекаю',
         'Сэнпай,еще один такой мем и я передознусь…Но воскресну ради следующего)']
list2=['Обращаясь ко мне, подумай чего сам добился, мразь',
       'Хули тебе надо, отьебись от меня, неудачник',
       'твое обращение принято, скоро тебя выебут в жопу, ожидайте',
       'Извини,я занят, я мать твою ебу','Схуяли ты ко мне обращаешься? у тебя прав нет',
       'иди отсоси себе','пшел нах','Ты так бесишься, потому что у твоей девки больше член, чем у тебя.',
       'У меня был кошмар. Мне приснилось, что я был тобой.',
       'Твои родители завели тебя, только потому что твоя мама не могла позволить себе аборт.',
       ' У нас кто-то сдох или ты снял носки?','У твоей мамы, кроме тебя, абортов не было? ' ,
       'тебе бы подумать о спасении природы, стерилизовав себя.',
       'Можно было бы тебя и обидеть, конечно, но природа уже справилась за меня.']
list3=['ему и так помирать скоро, отьебись уже',
       'Покебол забыл кинуть','еще дорожка и он тебе ответит, ага',
       'Он всё равно не выйдет из комнаты, зачем ты ему пишешь',
       'Nani?','Если он сейчас чертит тебе пизда',
       'иди нахуй, он спит',
       'сек.Ща зайдет.А не, ему похуй, извини.',
       'subscribe to pewdiepie']
list4=['kurwa spierdalaj',
       '*по польски ебет тебя в рот*',
       'zapisz się do pewdiepie',
       'Omae wa mou shindeiru',
       'w8, I have a chicken dinner',
       'Ща кого то на брэйкдаун поделят']
postirony=['Ноу вэй ',
           'В очко себе засунь свою постиронию',
           'твое рождение было постиронией',
           'За подкаблучника и двор стреляю в упор']
naruto=['не говорите о дерьме здесь, иначе вступят другие команды',
        'Я хоть и бот, но от такого и блевануть могу',
        'Подкаблучник, я вызываю тебя',
        'Тойво сейчас точно охуел, да?']
pdor_output=[
    'Кхм Кхм Пидор',
    'Пидор, всего лишь Пидор',
    'Просто используйте "Пидор", разницы нету '
    'пиши верно: \n П \n И\nД\n О\n р'
]
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


########################################################################################################################
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup=telebot.types.ReplyKeyboardMarkup(True,True)
    user_markup.row('/updates')
    user_markup.row('М, постирония')
    user_markup.row('Лол')
    user_markup.row('кик пидора')
    bot.send_message(message.chat.id,'Sup,bro',reply_markup=user_markup)



@bot.message_handler(commands=['updates'])
def handle_text(message) :
    bot.send_message(message.chat.id,'ver 0.0.9a \n 1. pay request added \n 2. Days without message from toivo added')




########################################################################################################################


@bot.message_handler (content_types=[ 'text'])
def handle_text(message):
#Кик Пидора Кейсы
    if "кик" in message.text.casefold() and "пидора" in message.text.casefold() and message.from_user.id==pdor:
        bot.send_message(message.chat.id, random.choice(antikickpidor))
    elif "кик" in message.text.casefold() and "пидора" in message.text.casefold():
        bot.kick_chat_member(message.chat.id,pdor)
    elif "добавь" in message.text.casefold() and "пидора" in message.text.casefold():
        bot.send_message(message.chat.id, 'добавьте хуесоса обратно в чат, я не умею \n :с')
#Пасхалка на Вадю
    elif "фен" in message.text.casefold() :
        bot.send_message(message.chat.id, "ух бля. Где?")
        bot.send_sticker(message.chat.id, 'CAADAgADGQADdrwVEoONfod1baECAg')
        bot.send_sticker(message.chat.id,'CAADAgADGwADdrwVEugPesOA677WAg')
# Вопросы от Кирилла
    elif "?" in message.text.casefold() and message.from_user.id == pdor:
        bot.send_message(message.chat.id, 'Да, да, иди нахуй со своими вопросами')
    elif "？" in message.text.casefold() and message.from_user.id == pdor:
        bot.send_message(message.chat.id, 'Да, да, иди нахуй со своими вопросами')
    elif "вопрос" in message.text.casefold() and message.from_user.id == pdor:
        bot.send_message(message.chat.id, 'Да, да, иди нахуй со своими вопросами')
#ПостИрония
    elif "постирония" in message.text.casefold() and message.from_user.id==pdor:
 #       bot.kick_chat_member(message.chat.id,pdor)
        bot.send_message(message.chat.id,random.choice(postirony))
# Name Trigger
    elif "муж яны" in message.text.casefold() or "тойво" in message.text.casefold():
        bot.send_voice(message.chat.id, 'AwADAgADBwMAApVSyUhfmq4afLSL7wI')
    elif "@neuroti" in message.text.casefold() :
        bot.send_message(message.chat.id, 'не neuroti, а Ваше Высочество')
    elif "pussykicker" in message.text.casefold() and message.from_user.id==neur:
        bot.send_message(message.chat.id, 'Да, хозяин. Стараюсь из всех сил')
    elif "pussykicker" in message.text.casefold():
        bot.send_sticker(message.chat.id, 'CAADAgADHAADdrwVEvoDBqqJl08MAg')
        bot.send_sticker(message.chat.id, 'CAADAgADDgADdrwVEnkQK3mHCDbTAg')
        bot.send_message(message.chat.id,random.choice(list2))
    elif "captainpostirony" in message.text.casefold():
        bot.send_message(message.chat.id,random.choice(list3))
    elif "magiquell" in message.text.casefold():
        bot.send_message(message.chat.id, random.choice(list4))
# Random Kick
    elif "удав" in message.text.casefold():
        bot.kick_chat_member(message.chat.id,random.choice(kickemall))
# Daun
    elif "даун" in message.text.casefold() and message.from_user.id == pdor:
        bot.send_message(message.chat.id, 'Ты думаешь, что ты умный, но все знают, что ты пидор')
    elif "даун" in message.text.casefold():
        bot.send_message(message.chat.id, 'Обнаружен даун, просьба к тем, кто находится рядом его обоссать')
#Пасхалка на Русю( Не открыта еще)
    elif "карина" in message.text.casefold():
        bot.send_message(message.chat.id,'Земля те пуховик')
        bot.send_sticker(message.chat.id,'CAADAgADHAADdrwVEvoDBqqJl08MAg')
#Крылатые слова и фразы
    elif "bitch" in message.text.casefold():
        bot.send_message(message.chat.id, 'lasagna')
    elif "who dat boy" in message.text.casefold():
        bot.send_message(message.chat.id, 'Who him is')
#Наруто Кик
    elif "наруто" in message.text.casefold() or "naruto" in message.text.casefold() :
        bot.send_message(message.chat.id,random.choice(naruto))
 #       bot.kick_chat_member(message.chat.id,toivo)

#Антибот Система, которая не работает :с
    elif 'unique:
        bot.send_message(message.chat.id, random.choice(antibotlist))
        # Ласт сообщение от Вади




    #Конец функционала( Элс)
    else:
        bot.get_chat(message.chat.id)


########################################################################################################################

#начало For


#Дунуть
    for var in dunut:
        if var in message.text.casefold():
            bot.send_message(message.chat.id, 'в очко себе дунь,опездал')
#Пасхалка на Саню
    for var in weed:
        if var in message.text.casefold():
            bot.send_message(message.chat.id, "ух бля. Где?")
            bot.send_sticker(message.chat.id, 'CAADAgADHgADdrwVEjyUagrs6gdRAg')
#Призыв к суициду
    for var in suicide_names:
        if var in message.text.casefold()and message.from_user.id==pdor:
            bot.send_message(message.chat.id, '+380 97 610 9797 может хоть эти тебе помогут')
# Слава Украине кейсы
    for var in slava_ukraine:
        if var in message.text.casefold()and message.from_user.id==pdor:
            bot.send_message(message.chat.id, 'иди нахуй, пидор')
        elif var in message.text.casefold():
            bot.send_message(message.chat.id, 'Героям Слава')
# Имена Пидора
    for var in pdor_names:
            if var in message.text.casefold():
                bot.send_message(message.chat.id, random.choice(pdor_output))
#Имена тойво
    for var in toivo_names:
            if var in message.text.casefold() and message.from_user.id==toivo:
                bot.send_message(message.chat.id,'Ты такое не пиши, от тебя дерьмом воняет')
            elif var in message.text.casefold():
                bot.kick_chat_member(message.chat.id, message.from_user.id)
#Смерть Вади
    for var in vad_death:
        if var in message.text.casefold():
                now= datetime.datetime.now()
                then= datetime.datetime(2023,1,17)
                delta= then- now
                bot.send_message(message.chat.id,'Ваде осталось жить')
                bot.send_message(message.chat.id, delta)

    #def everytime(message):
# Донат система
    if "cool" in message.text.casefold():
        i = 0
        while i < 10:
            time.sleep(60*60)
            bot.send_message(message.chat.id, 'Я буду краток: сегодня мы просим Вас помочь Ваде. Защищая независимость бота - мы не размещаем рекламу. Но нам нужно на что-то существовать. \n Представьте, сколько бы я мог зарабатывать, сдавая Пидора в эскорт. Но тогда вы бы не смогли мне доверять. \n Очень легко не заметить это сообщение, но любой доллар поможет развитию меня и Вади.\n Спасибо Вам. Реквизиты: \n 5169 3305 1555 6451 ')
            bot.pin_chat_message(message.chat.id,message.message_id)
            i = i + 1


########################################################################################################################

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    if message.from_user.id==ruslan:
        bot.send_message(message.chat.id, random.choice(rusmems))
    else:
        bot.send_message(message.chat.id, random.choice(mems))


now2 = datetime.datetime.now()
then2 = datetime.datetime(2019, 4, 4,16,1)
delta2 = now2-then2
delta3 = now2 - then2
then3=datetime.datetime(2019,4,4,16,0)

handle_start()
handle_text()
handle_photo()
bot.polling(none_stop=True, interval=0)
