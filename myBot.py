from telegram import *
from telegram.ext import * 

bot = Bot("1864626654:AAG8VA_5l_1ea25xxgUeQgI5O3fsNiBY3M4")
#print(bot.get_me())
updater=Updater("1864626654:AAG8VA_5l_1ea25xxgUeQgI5O3fsNiBY3M4",use_context=True)
dispatcher=updater.dispatcher

def my_site(update:Update, context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="website link: https://todo-vishwaratna.herokuapp.com",
    )

start_value=CommandHandler('mysite',my_site)

dispatcher.add_handler(start_value)

def my_video(update:Update, context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Video link: https://youtu.be/_VRlRIe1N8Q",
    )

start_value1=CommandHandler('myvideo',my_video)

dispatcher.add_handler(start_value1)
print(bot.get_me())
updater.start_polling()
