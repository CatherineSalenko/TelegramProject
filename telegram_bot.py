"""
Telegram bot function
"""
import telebot

import settings

bot = telebot.TeleBot(settings.bottoken)

# start
def start_message():
    print("test")

# поиск контрагента
def find_company():
    print("test")


def find_company_by_unp():
    print("test")


def find_company_by_name():
    print("test")


def get_company_debit():
    print("test")


def get_debt_detailing():
    print("test")


bot.infinity_polling()



