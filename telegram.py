import telebot
import os
from dotenv import load_dotenv
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv()

bot = telebot.TeleBot(os.getenv('TOKEN'), parse_mode=None)  # You can set parse_mode by default. HTML or MARKDOWN
# print(os.getenv('TOKEN'))

# user = bot.get_me()
# updates = bot.get_updates()

# @bot.message_handler(commands=['starts', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")
#
# def get_chat_id_by_username(updates_array,tele_username):
# 	if tele_username==updates_array.message.chat.username:
# 		chat_id=updates_array.message.chat.id
#
# 		return chat_id
# 	else: return False
#
# i = 0
# while i <= len(updates)-1:
# 	desiredid = get_chat_id_by_username(updates[i], os.getenv('CHAT_USERNAME'))
# 	if desiredid != False:
# 		break
# 	i += 1


text = "**Welcome to notification system ..**\n"
chatid = os.getenv('CHAT_ID')
text += "Hi VSSUT, How are you?"
# bot.send_message(chatid, text)

class SendTelegram:
    def __init__(self,date,title,link):
        self.date = date
        self.title = title
        self.link = link

        text=""+"New Notification Received"+""+" \n\n"
        text += f"Dated: {self.date} \nTitle:    {self.title} \nUrl:{self.link}\n"
        markup = InlineKeyboardMarkup([[InlineKeyboardButton(text='Download Notice', url=self.link)],])

        bot.send_message(chatid, text, reply_markup=markup)

# t=SendTelegram("Date","Title","mabia.in")