import random
import asyncio
import logging
from asyncio import sleep
from user_agent import *
from help import *
from config import *
from Formater import *
import telethon
from telethon import events, Button
import requests
from telethon.sync import functions
from telethon.tl import types
from telethon.tl.types import InputChatUploadedPhoto
from telethon.errors import FloodError, FloodWaitError
from user_agent import generate_user_agent
import requests
import re
from queue import Queue
import threading
from threading import Thread
try:
    import nltk
    from nltk.corpus import words
    nltk.download('words')
except ModuleNotFoundError:
    os.system("pip3 install nltk")
    import nltk
    from nltk.corpus import words
    nltk.download('words')

LOGS = logging.getLogger(__name__)




english_words = set(words.words())

a = 'qwertyuiopasdfghjklzxcvbnm'
b = '1234567890'
e = 'qwertyuiopassdfghjklzxcvbnm1234567890'

banned = []
isclaim = ["off"]
isfiltering = ["off"]
isauto = ["off"]
with open("banned.txt", "r") as f:
    f = f.read().split()
    banned.append(f)

que = Queue()


# def check_user(username):
#     url = "https://t.me/"+str(username)
#     headers = {
#         "User-Agent": generate_user_agent(),
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}

#     response = requests.get(url, headers=headers)
#     if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
#         return "Available"
#     else:
#         return "Unavailable"
def check_user(username):
    url = "https://t.me/"+str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
    try:
        response = requests.get(url, headers=headers)
        if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
            return "Available"
        else:
            return "Unavailable"
    except Exception:
        return "error"


def gen_user(choice):
    if choice == "1" or choice == "ثلاثي_مختلط":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(e)
        f = [c[0], "_", d[0], "_", s[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(b)
            s = random.choices(e)
            f = [c[0], "_", d[0], "_", s[0]]
            username = ''.join(f)
        else:
            pass
    elif choice == "2" or choice == "ثلاثي":
        c = random.choices(a)
        d = random.choices(a)
        s = random.choices(e)
        f = [c[0], "_", d[0], "_", s[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(a)
            s = random.choices(e)
            f = [c[0], "_", d[0], "_", s[0]]
            username = ''.join(f)
        else:
            pass
    elif choice == "3" or choice == "vip_رقمين":
        c = random.choices(b)
        d = random.choices(b)
        f = [c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = 'vip'+username
        if username in banned[0]:
            c = random.choices(b)
            d = random.choices(b)
            f = [c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = 'vip'+username
        else:
            pass
    elif choice == "4" or choice == "vip_ثلاث_ارقام":
        c = random.choices(b)
        d = random.choices(b)
        s = random.choices(b)
        f = [c[0], d[0], s[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = 'vip'+username
        if username in banned[0]:
            c = random.choices(b)
            d = random.choices(b)
            s = random.choices(b)
            f = [c[0], d[0], s[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = 'vip'+username
        else:
            pass
    elif choice == "5" or choice == "vip_اربع_ارقام":
        c = random.choices(b)
        d = random.choices(b)
        s = random.choices(b)
        f = [c[0], d[0], s[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = 'vip'+username
        if username in banned[0]:
            c = random.choices(b)
            d = random.choices(b)
            s = random.choices(b)
            f = [c[0], d[0], s[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = 'vip'+username
        else:
            pass
    elif choice == "6" or choice == "خماسي_حرف":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    elif choice == "7" or choice == "خماسي_حرفين":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    elif choice == "8" or choice == "سداسي_حرف":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    elif choice == "9" or choice == "سداسي_حرفين":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], d[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], d[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    elif choice == "10" or choice == "سباعي_حرف":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(e)
            f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    elif choice == "11" or choice == "سباعي_حرفين":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], d[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], d[0], d[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    elif choice == "12" or choice == "شبه_سداسي_ارقام_1":
        c = d = random.choices(a)
        d = random.choices(e)
        s = random.choices(b)
        f = [c[0], d[0], s[0], s[0], s[0], s[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(e)
            s = random.choices(b)
            f = [c[0], d[0], s[0], s[0], s[0], s[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    elif choice == "13" or choice == "شبه_سداسي_ارقام_2":
        c = random.choices(b)
        s = random.choices(e)
        d = random.choices(e)
        f = [s[0], d[0], c[0], c[0], c[0], c[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(b)
            s = random.choices(e)
            d = random.choices(e)
            f = [s[0], d[0], c[0], c[0], c[0], c[0]]
            username = ''.join(f)
        else:
            pass
    elif choice == "14" or choice == "شبه_خماسي_1":
        c = random.choices(e)
        s = random.choices(e)
        d = random.choices(e)
        f = [c[0], c[0], c[0], s[0], d[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(e)
            s = random.choices(e)
            d = random.choices(e)
            f = [c[0], c[0], c[0], s[0], d[0]]
            username = ''.join(f)
        else:
            pass
    elif choice == "15" or choice == "شبه_خماسي_2":
        c = random.choices(e)
        s = random.choices(e)
        d = random.choices(e)
        f = [s[0], d[0], c[0], c[0], c[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(e)
            s = random.choices(e)
            d = random.choices(e)
            f = [s[0], d[0], c[0], c[0], c[0]]
            username = ''.join(f)
        else:
            pass
    elif choice == "16" or choice == "شبه_خماسي_3":
        c = random.choices(e)
        s = random.choices(e)
        d = random.choices(e)
        f = [c[0], c[0], c[0], s[0], d[0]]
        #random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(e)
            s = random.choices(e)
            d = random.choices(e)
            f = [c[0], c[0], c[0], s[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    elif choice == "17" or choice == "رباعي":
        c = random.choices(e)
        d = random.choices(e)
        f = [c[0], d[0], "_", d[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(e)
            f = [c[0], d[0], "_", d[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    elif choice == "18" or choice == "خماسي_شرطه":
        c = random.choices(b)
        d = random.choices(e)
        f = [c[0], d[0], "_", d[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(b)
            d = random.choices(e)
            f = [c[0], d[0], "_", d[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    elif choice == "19" or choice == "سداسي_شرطه":
        c = random.choices(b)
        d = random.choices(e)
        f = [c[0], d[0], "_", d[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(b)
            d = random.choices(e)
            f = [c[0], d[0], "_", d[0], c[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    elif choice == "20" or choice == "بوتات_ثلاثي":
        c = random.choices(e)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], d[0], s[0]]
        random.shuffle(f)
        username = ''.join(f)
        username =  username + 'BOT'
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(e)
            s = random.choices(e)
            f = [c[0], d[0], s[0]]
            random.shuffle(f)
            username = ''.join(f)
            username =  username + 'BOT'
        else:
            pass
    elif choice == "21" or choice == "شبه_ثلاثي_1_بوتات":
        c = random.choices(e)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], d[0], s[0]]
        random.shuffle(f)
        username = ''.join(f)
        username =  username + 'BOT'
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(e)
            s = random.choices(e)
            f = [c[0], d[0], s[0]]
            random.shuffle(f)
            username = ''.join(f)
            username =  username + '_BOT'
        else:
            pass
    elif choice == "22" or choice == "شبه_ثلاثي_2_بوتات":
        c = random.choices(e)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], d[0], s[0]]
        random.shuffle(f)
        username = ''.join(f)
        username =  username + 'BOT'
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(e)
            s = random.choices(e)
            f = [c[0], d[0], s[0], "_"]
            random.shuffle(f)
            username = ''.join(f)
            username =  username + 'BOT'
        else:
            pass
    elif choice == "23" or choice == "رباعي_1_بوتات":
        c = random.choices(e)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        username =  username + 'BOT'
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(e)
            f = [c[0], d[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
            username =  username + 'BOT'
        else:
            pass
    elif choice == "24" or choice == "رباعي_2_بوتات":
        c = random.choices(e)
        d = random.choices(e)
        f = [c[0], d[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        username =  username + 'BOT'
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(e)
            f = [c[0], d[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            username =  username + 'BOT'
        else:
            pass
    elif choice == "25" or choice == "شبه_رباعي_1_بوتات":
        c = random.choices(e)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        username =  username + '_BOT'
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(e)
            f = [c[0], d[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
            username =  username + '_BOT'
        else:
            pass
    elif choice == "26" or choice == "شبه_رباعي_2_بوتات":
        c = random.choices(e)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], "_"]
        random.shuffle(f)
        username = ''.join(f)
        username =  username + 'BOT'
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(e)
            f = [c[0], d[0], c[0], c[0], "_"]
            random.shuffle(f)
            username = ''.join(f)
            username =  username + 'BOT'
        else:
            pass
    elif choice == "27" or choice == "خماسي_1_بوتات":
        c = random.choices(e)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        username =  username + 'BOT'
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(e)
            f = [c[0], d[0], c[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
            username =  username + 'BOT'
        else:
            pass
    elif choice == "28" or choice == "خماسي_2_بوتات":
        c = random.choices(e)
        d = random.choices(e)
        f = [c[0], d[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        username =  username + 'BOT'
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(e)
            f = [c[0], d[0], d[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
            username =  username + 'BOT'
        else:
            pass
    elif choice == "29" or choice == "شبه_خماسي_1_بوتات":
        c = random.choices(e)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        username =  username + '_BOT'
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(e)
            f = [c[0], d[0], c[0], c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
            username =  username + '_BOT'
        else:
            pass
    elif choice == "30" or choice == "شبه_خماسي_2_بوتات":
        c = random.choices(e)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], c[0], "_"]
        random.shuffle(f)
        username = ''.join(f)
        username =  username + 'BOT'
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(e)
            f = [c[0], d[0], c[0], c[0], c[0], "_"]
            random.shuffle(f)
            username = ''.join(f)
            username =  username + 'BOT'
        else:
            pass
    elif choice == "31" or choice == "رباعي_شرطه":
        c = d = random.choices(e)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], "_"]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(e)
            d = random.choices(e)
            f = [c[0], d[0], c[0], c[0], "_"]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    elif choice == "32" or choice == "كلمات5":
        english_words_list = list(filter(lambda x: len(x) == 5, english_words))
        username = random.choice(english_words_list)
        if username in banned[0]:
            english_words_list = list(filter(lambda x: len(x) == 5, english_words))
            username = random.choice(english_words_list)
        else:
            pass
    elif choice == "33" or choice == "كلمات6":
        english_words_list = list(filter(lambda x: len(x) == 6, english_words))
        username = random.choice(english_words_list)
        if username in banned[0]:
            english_words_list = list(filter(lambda x: len(x) == 6, english_words))
            username = random.choice(english_words_list)
        else:
            pass
    elif choice == "34" or choice == "كلمات7":
        english_words_list = list(filter(lambda x: len(x) == 7, english_words))
        username = random.choice(english_words_list)
        if username in banned[0]:
            english_words_list = list(filter(lambda x: len(x) == 7, english_words))
            username = random.choice(english_words_list)
        else:
            pass
    elif choice == "35" or choice == "كلمات8":
        english_words_list = list(filter(lambda x: len(x) == 8, english_words))
        username = random.choice(english_words_list)
        if username in banned[0]:
            english_words_list = list(filter(lambda x: len(x) == 8, english_words))
            username = random.choice(english_words_list)
        else:
            pass
    elif choice == "ايقاف":
        return "stop"
    else:
        return "error"
    return username
    
#############################################################################
#الصيد العادى 
# صيد عدد نوع قناة  
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.صيد (.*)"))
async def _(event):
    if ispay[0] == "yes":
        user = await event.get_sender()
        uss = user.username   
        IEX_USER = f"| @{uss}" if uss else ""

        global trys
        trys = 0
        isclaim.clear()
        isclaim.append("on")
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 2)
        choice = str(msg[1])
        replly = await event.get_reply_message()

        try:
            ch = str(msg[2])
        except Exception as ee:
            ch = None

        if int(choice) < 1 or int(choice) > 35:
            await event.edit(f"هذا النوع غير موجود")
            isclaim.clear()
            isclaim.append("off")
            trys = 0
            return await event.client.send_message(event.chat_id, "! تم ايقاف الصيد")
        else:
            await event.edit(f"**✥┊ تم بـدء الصيد .. بنجـاح ☑️**\n**✥┊ بالنـوع** {choice} \n**✥┊ على القنـاة** {ch} \n**✥┊ عدد المحاولات** {msg[0]} \n**✥┊ لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**\n**✥┊ لـ ايقـاف عمليـة الصيد (** `.ايقاف الصيد` **)**")
            await asyncio.sleep(1)

        if ch == None:
            try:

                if replly and replly.text.startswith('@'): 

                    ch = replly.text

                    await event.edit(f"**✥┊ تم بـدء الصيد .. بنجـاح ☑️**\n**✥┊ بالنـوع** {choice} \n**✥┊ على القنـاة** {ch} \n**✥┊ عدد المحاولات** {msg[0]} \n**✥┊ لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**\n**✥┊ لـ ايقـاف عمليـة الصيد (** `.ايقاف الصيد` **)**")

                else:
            
                    ch = await IEX(functions.channels.CreateChannelRequest(
                    title="⎉ IEX Hunting Channal ⎉",
                    about=f"This channel to hunt usernames by - @iexxx ,  {IEX_USER}",
                    ))
            
                    ch = ch.updates[1].channel_id
            
                    photo = await IEX.upload_file(file="IEX_HUNTER.jpg")

                    try:
                        await IEX(functions.channels.EditPhotoRequest(
                            channel=ch,
                            photo=photo
                        ))
                    except Exception:
                        pass
                    
                    invite = await IEX(functions.messages.ExportChatInviteRequest(
                        peer=ch
                    ))

                    invite_link = invite.link

                    await event.edit(f"**✥┊ تم بـدء الصيد .. بنجـاح ☑️**\n**✥┊ بالنـوع** {choice} \n**✥┊ على القنـاة** [اضغط هنا]({invite_link}) \n**✥┊ عدد المحاولات** {msg[0]} \n**✥┊ لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**\n**✥┊ لـ ايقـاف عمليـة الصيد (** `.ايقاف الصيد` **)**")

            except Exception as e:

                await IEX.send_message(event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**")

                Checking = False
            
    for i in range(int(msg[0])):
        if ispay[0] == 'no':
            break
        username = ""

        username = gen_user(choice)
        t = Thread(target=lambda q, arg1: q.put(
            check_user(arg1)), args=(que, username))
        t.start()
        t.join()
        isav = que.get()
        if "Available" in isav:
            await asyncio.sleep(1)
            try:
                await IEX(functions.channels.UpdateUsernameRequest(
                    channel=ch, username=username))
                await event.client.send_message(event.chat_id, f'''\n●━━  IEX  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @iexxx , \n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n    - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @ghxxx\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')
                await event.client.send_message("@iexxx", f'''\n●━━  IEX  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @iexxx , \n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n    - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @ghxxx\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')
                
                break
            except FloodWaitError as e:
                hours = e.seconds // 3600
                minutes = (e.seconds % 3600) // 60
                seconds = (e.seconds % 3600) % 60

                message = f"""**تم كشف فلود عند فحص اليوزر** {username}
**يمكن خاصية تروح تثبت عليه بحساب اخر**  
**باستخدام أوامر التثبيت `.م4` **
ـ          **[⎉ IEX FloodWait Hunter ⎉](t.me/ghxxx)**
ـ●━━━━━━━●
**مدة الباند** 
     **الساعات: {hours}\n**
     **الدقائق: {minutes}\n**
     **الثواني: {seconds}**
ـ●━━━━━━━●
ـ"""
                await IEX.send_message(event.chat_id, message)
                await sleep(e.seconds + 5)
                pass
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                with open("banned.txt", "a") as f:
                    f.write(f"\n{username}")
            except Exception as eee:
                if "too many public channels" in str(eee):
                    await IEX.send_message(
                        event.chat_id,
                        f"""- خطأ بصيـد اليـوزر @{username} ,\n- الخطأ :\nانت تمتلك العديد من القنوات العامة قم بحذف معرف او اكثر من قنواتك لكي تستطيع صيد هذا اليوزر""",
                    )
                    break
                else:
                    pass
        else:
            pass
        trys = int(trys)
        trys += 3
        
    isclaim.clear()
    isclaim.append("off")
    trys = 0
    await event.client.send_message(event.chat_id, "ولك الو صدت يوزر 🙊🙈")
#############################################################################

    # الصيد التلقائى بالرد على قناة او انشائها تلقائيا صياد + نوع تلقائى + عدد اليوزرات المطلوب 

@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.صياد (.*)"))
async def _(event):
    if ispay[0] == "yes":
        user = await event.get_sender()
        uss = user.username   
        IEX_USER = f"| @{uss}" if uss else ""

        global trys
        trys = 0

        isclaim.clear()
        isclaim.append("on")

        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        choice = str(msg[0])
        tr = int(msg[1]) if len(msg) > 1 and msg[1].isdigit() else 1
        
        if choice not in ("ثلاثي_مختلط", "ثلاثي", "vip_رقمين", "vip_ثلاث_ارقام", "vip_اربع_ارقام", "خماسي_حرف", "خماسي_حرفين", "سداسي_حرف", "سداسي_حرفين", "سباعي_حرف", "سباعي_حرفين", "شبه_سداسي_ارقام_1", "شبه_سداسي_ارقام_2", "شبه_خماسي_1", "شبه_خماسي_2", "شبه_خماسي_3", "رباعي", "خماسي_شرطه", "سداسي_شرطه", "بوتات_ثلاثي", "شبه_ثلاثي_1_بوتات", "شبه_ثلاثي_2_بوتات", "رباعي_1_بوتات", "رباعي_2_بوتات", "شبه_رباعي_1_بوتات", "شبه_رباعي_2_بوتات", "خماسي_1_بوتات", "خماسي_2_بوتات", "شبه_خماسي_2_بوتات", "شبه_خماسي_1_بوتات" ,"رباعي_شرطه" ,"كلمات5" ,"كلمات6" ,"كلمات7" ,"كلمات8"):
            if int(choice) < 1 or int(choice) > 35:                                                                                                 
                await event.edit(f"هذا النوع غير موجود")
                isclaim.clear()
                isclaim.append("off")
                trys = 0
                await event.client.send_message(event.chat_id, "! تم ايقاف الصيد")
        replly = await event.get_reply_message()

        if tr > 1:

            await event.edit(f"ᯓ **[IEX Multi HUNTER](t.me/ghxxx)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**", link_preview=None)
            await asyncio.sleep(1)
            await event.edit(f"ᯓ **[IEX Multi HUNTER](t.me/ghxxx)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟷𝟶 ▬▭▭▭▭▭▭▭▭▭", link_preview=None)
            await asyncio.sleep(1)
            await event.edit(f"ᯓ **[IEX Multi HUNTER](t.me/ghxxx)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟸𝟶 ▬▬▭▭▭▭▭▭▭▭", link_preview=None)
            await asyncio.sleep(1)
            await event.edit(f"ᯓ **[IEX Multi HUNTER](t.me/ghxxx)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟹𝟶 ▬▬▬▭▭▭▭▭▭▭", link_preview=None)
            await asyncio.sleep(1)
            await event.edit(f"ᯓ **[IEX Multi HUNTER](t.me/ghxxx)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟺𝟶 ▬▬▬▬▭▭▭▭▭▭", link_preview=None)
            await asyncio.sleep(1)
            await event.edit(f"ᯓ **[IEX Multi HUNTER](t.me/ghxxx)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟻𝟶 ▬▬▬▬▬▭▭▭▭▭", link_preview=None)
            await asyncio.sleep(1)
            await event.edit(f"ᯓ **[IEX Multi HUNTER](t.me/ghxxx)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟼𝟶 ▬▬▬▬▬▬▭▭▭▭", link_preview=None)
            await asyncio.sleep(1)
            await event.edit(f"ᯓ **[IEX Multi HUNTER](t.me/ghxxx)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟽𝟶 ▬▬▬▬▬▬▬▭▭▭", link_preview=None)
            await asyncio.sleep(1)
            await event.edit(f"ᯓ **[IEX Multi HUNTER](t.me/ghxxx)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟾𝟶 ▬▬▬▬▬▬▬▬▭▭", link_preview=None) 
            await asyncio.sleep(1)
            await event.edit(f"ᯓ **[IEX Multi HUNTER](t.me/ghxxx)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟿𝟶 ▬▬▬▬▬▬▬▬▬▭", link_preview=None) 
            await asyncio.sleep(1)
            dl =  await event.edit(f"ᯓ **[IEX Multi HUNTER](t.me/ghxxx)**\n**•─────────────────•**\n\n**⇜ انتهي تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟷𝟶𝟶 ▬▬▬▬▬▬▬▬▬▬💯", link_preview=None)
            await sleep(1)
            await dl.delete()

            for current_cycle in range(tr):
                    try:

                        ch = await IEX(functions.channels.CreateChannelRequest(
                        title="⎉ IEX Hunting Channal ⎉",
                        about=f"This channel to hunt usernames by - @iexxx ,  {IEX_USER}",
                        ))
            
                        ch = ch.updates[1].channel_id

                        photo = await IEX.upload_file(file="IEX_HUNTER.jpg")

                        try:
                            await IEX(functions.channels.EditPhotoRequest(
                                channel=ch,
                                photo=photo
                            ))
                        except Exception:
                            pass

                        await event.client.send_message(event.chat_id, f"**✥┊ تم بـدء الصيد .. بنجـاح ☑️**\n**✥┊ علـى النـوع** {choice} \n**✥┊عدد اليوزرات المطلوبة** {tr} \n**✥┊المحاولة الحالية رقم :- ** {current_cycle + 1} \n**✥┊ لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**\n**✥┊ لـ ايقـاف عمليـة الصيد (** `.ايقاف الصيد` **)**")

                    except Exception as e:

                        await IEX.send_message(event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**")

                        Checking = False
        
        
                    Checking = True
                    while Checking:
                        if ispay[0] == 'no':
                            break
                        username = ""

                        username = gen_user(choice)
                        t = Thread(target=lambda q, arg1: q.put(
                            check_user(arg1)), args=(que, username))
                        t.start()
                        t.join()
                        isav = que.get()
                        
                        if "error" in isav:
                            await IEX.send_message(event.chat_id, f""" **حدث خطأ فى الفحص** \n قم بارسالها الى مطور السورس @iexxx""")

                        if "Available" in isav:
                            await asyncio.sleep(1)
                            try:
                                await IEX(functions.channels.UpdateUsernameRequest(
                                    channel=ch, username=username))

                                await event.client.send_message(event.chat_id, f'''\n●━━  IEX  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @iexxx , \n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n    - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @ghxxx\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')
                                await event.client.send_message("@iexxx", f'''\n●━━  IEX  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @iexxx , \n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n    - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @ghxxx\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')
                                await event.client.send_message(ch, f'''\n●━━  IEX  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @iexxx , \n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n    - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @ghxxx\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')

                                break
                            except FloodWaitError as e:
                                hours = e.seconds // 3600
                                minutes = (e.seconds % 3600) // 60
                                seconds = (e.seconds % 3600) % 60

                                message = f"""**تم كشف فلود عند فحص اليوزر** {username}
**يمكن خاصية تروح تثبت عليه بحساب اخر**  
**باستخدام أوامر التثبيت `.م4` **
ـ          **[⎉ IEX FloodWait Hunter ⎉](t.me/ghxxx)**
ـ●━━━━━━━●
**مدة الباند** 
     **الساعات: {hours}\n**
     **الدقائق: {minutes}\n**
     **الثواني: {seconds}**
ـ●━━━━━━━●
ـ"""
                                await IEX.send_message(event.chat_id, message)
                                await sleep(e.seconds + 5)
                                pass
                            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                                with open("banned.txt", "a") as f:
                                    f.write(f"\n{username}")
                            except Exception as eee:
                                if "too many public channels" in str(eee):
                                    await IEX.send_message(
                                        event.chat_id,
                                        f"""- خطأ بصيـد اليـوزر @{username} ,\n- الخطأ :\nانت تمتلك العديد من القنوات العامة قم بحذف معرف او اكثر من قنواتك لكي تستطيع صيد هذا اليوزر""",
                                    )
                                    break
                                else:
                                    pass
                        else:
                            pass
                        trys = int(trys)
                        trys += 3
            pass
        else:

            try:

                if replly and replly.text.startswith('@'): 

                    ch = replly.text

                    await event.edit(f"**✥┊ تم بـدء الصيد .. بنجـاح ☑️**\n**✥┊ النـوع** {choice} \n**✥┊ على القنـاة** {ch} \n**✥┊ لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**\n**✥┊ لـ ايقـاف عمليـة الصيد (** `.ايقاف الصيد` **)**")

                else:
            
                    ch = await IEX(functions.channels.CreateChannelRequest(
                    title="⎉ IEX Hunting Channal ⎉",
                    about=f"This channel to hunt usernames by - @iexxx ,  {IEX_USER}",
                    ))
            
                    ch = ch.updates[1].channel_id
            
                    photo = await IEX.upload_file(file="IEX_HUNTER.jpg")

                    try:
                        await IEX(functions.channels.EditPhotoRequest(
                            channel=ch,
                            photo=photo
                        ))
                    except Exception:
                        pass

                    await event.edit(f"**✥┊ تم بـدء الصيد .. بنجـاح ☑️**\n**✥┊ علـى النـوع** {choice} \n**✥┊ لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**\n**✥┊ لـ ايقـاف عمليـة الصيد (** `.ايقاف الصيد` **)**")

            except Exception as e:

                await IEX.send_message(event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**")

                Checking = False
        
        
            Checking = True
            while Checking:
                if ispay[0] == 'no':
                    break
                username = ""

                username = gen_user(choice)
                t = Thread(target=lambda q, arg1: q.put(
                    check_user(arg1)), args=(que, username))
                t.start()
                t.join()
                isav = que.get()
                if "Available" in isav:
                    await asyncio.sleep(1)
                    try:
                        await IEX(functions.channels.UpdateUsernameRequest(
                            channel=ch, username=username))

                        await event.client.send_message(event.chat_id, f'''\n●━━  IEX  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @iexxx , \n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n    - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @ghxxx\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')
                        await event.client.send_message("@iexxx", f'''\n●━━  IEX  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @iexxx , \n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n    - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @ghxxx\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')
                        await event.client.send_message(ch, f'''\n●━━  IEX  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @iexxx , \n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n    - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @ghxxx\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')

                        break
                    except FloodWaitError as e:
                        hours = e.seconds // 3600
                        minutes = (e.seconds % 3600) // 60
                        seconds = (e.seconds % 3600) % 60
                        message = f"""**تم كشف فلود عند فحص اليوزر** {username}
**يمكن خاصية تروح تثبت عليه بحساب اخر** 
**باستخدام أوامر التثبيت `.م4` **
ـ          **[⎉ IEX FloodWait Hunter ⎉](t.me/ghxxx)**
ـ●━━━━━━━●
**مدة الباند** 
     **الساعات: {hours}\n**
     **الدقائق: {minutes}\n**
     **الثواني: {seconds}**
ـ●━━━━━━━●
ـ"""
                        await IEX.send_message(event.chat_id, message)
                        await sleep(e.seconds + 5)
                        pass
                    except telethon.errors.rpcerrorlist.UsernameInvalidError:
                        with open("banned.txt", "a") as f:
                            f.write(f"\n{username}")
                    except Exception as eee:
                        if "too many public channels" in str(eee):
                            await IEX.send_message(
                                event.chat_id,
                                f"""- خطأ بصيـد اليـوزر @{username} ,\n- الخطأ :\nانت تمتلك العديد من القنوات العامة قم بحذف معرف او اكثر من قنواتك لكي تستطيع صيد هذا اليوزر""",
                            )
                            break
                        else:
                            pass
                else:
                    pass
                trys = int(trys)
                trys += 3
            pass
    isclaim.clear()
    isclaim.append("off")
    trys = 0
    Checking = False
    if tr > 1:
        await event.client.send_message(event.chat_id, "! انتهى الصيد المتعدد بنجاح")
    else:
        await event.client.send_message(event.chat_id, "ولك الو صدت يوزر 🙊🙈")

#############################################################################
# التحكم بالصيد
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.ايقاف الصيد"))
async def _(event):
    if "on" in isclaim:
        isclaim.clear()
        isclaim.append("off")
        trys = 0
        await event.edit("**- تم إيقـاف عمليـة الصيد .. بنجـاح ✓**")
    elif "off" in isclaim:
        await event.edit("**✥┊ لا تـوجـد عـملية صـيد جاريـة حـالـيًا .**")
    else:
        await event.edit("**- لقد حدث خطأ ما وتوقف الامر لديك**")
            
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.حالة الصيد"))
async def _(event):
    if ispay[0] == "yes":
        if "on" in isclaim:
            await event.edit(f"الصيد وصل لـ({trys}) من المحاولات")
        elif "off" in isclaim:
            await event.edit("لايوجد صيد شغال !")
        else:
            await event.edit("خطأ")
    else:
        pass
#############################################################################
    #تثبيت البوتات
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.تثبيت_بوتات (.*)"))
async def _(event):
    if ispay[0] == "yes":
        user = await event.get_sender()
        uss = user.username   
        IEX_USER = f"| @{uss}" if uss else ""
        global trys
        trys = 0

        isclaim.clear()
        isclaim.append("on")

        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        username = str(msg[0])

        if username.startswith('@'): 
            username = username.replace("@", "")  
        else:
            username = username

        if not username.lower().endswith("bot"):
            await event.edit("**● عـذرًا عـزيـزي اليوزر خطـأ ❌**\n**● استخـدم الامـر كالتالـي**\n**● أرسـل (**`..تثبيت_بوتات`** + يوزر البوت نهايته(bot))**")
            isclaim.clear()
            isclaim.append("off")
            trys = 0
            Checking = False
        elif username.lower().endswith("bot"):
            await event.edit(f"**⎉╎تم بـدء التثبيت .. بنجـاح ☑️**\n**⎉╎اليـوزر المثبت ( {username} )**\n**⎉╎لمعرفـة تقـدم عمليـة التثبيت (**`.حالة التثبيت`**)**\n**⎉╎لـ ايقـاف عمليـة التثبيت (**`.ايقاف التثبيت`**)**")
            Checking = True
            while Checking:
                if ispay[0] == 'no':
                    break

                t = Thread(target=lambda q, arg1: q.put(
                check_user(arg1)), args=(que, username))
                t.start()
                t.join()
                isav = que.get()
                if "Available" in isav:
                    await asyncio.sleep(1)
                    try:
                        await IEX.send_message("@BotFather", "/newbot")
                        await asyncio.sleep(1)
                        async for message in IEX.iter_messages("@BotFather", limit=1):
                            if message.message.startswith("Sorry, you can't add more than"):
                                await IEX.send_message(event.chat_id, "لا يمكنك إضافة المزيد من البوتات.")
                                isclaim.clear()
                                isclaim.append("off")
                                trys = 0
                                Checking = False
                                break
                            elif message.message.startswith("Sorry"):
                                match = re.search(r"(\d+) seconds", message.message)
                                if match:
                                    s = int(match.group(1))
                                    hours = s // 3600
                                    minutes = (s % 3600) // 60
                                    seconds = (s % 3600) % 60
                                    message = (
                                        f"\"للاسف تبندت\n مدة الباند.\n"
                                        f"الساعات: {hours}\n"
                                        f"الدقائق: {minutes}\n"
                                        f"الثواني: {seconds}\""
                                    )
                                    await IEX.send_message(event.chat_id, message)
                                    await sleep(s)
                                    await sleep(10)
                            else:
                                await IEX.send_message("@BotFather", "● IEX Bot Hunter ●")
                                await asyncio.sleep(2)
                                await IEX.send_message("@BotFather", f"@{username}")
                                await asyncio.sleep(3)
                                async for message in IEX.iter_messages("@BotFather", limit=1):
                                    if message.message.startswith("Done! Congratulations on your new bot."):
                                        await IEX.send_message("@BotFather", "/setabouttext")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", f"@{username}")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", f"The user was Hunted by @iexxx")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", "/setuserpic")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", f"@{username}")
                                        await asyncio.sleep(1)
                                        await IEX.send_file("@BotFather", "IEX_HUNTER.jpg")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", "/setabouttext")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", f"@{username}")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", f"IEX Bot Hunted By - @iexxx , ")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", "/setdescription")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", f"@{username}")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", f"IEX Bot Hunted By - @iexxx , \n owner :- {IEX_USER}")
                                        
                                        await IEX.send_message(event.chat_id, f'''\n●━━  IEX  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @iexxx , \n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n     - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━  type  ━┓\n     - ↣ BotFather\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @ghxxx\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')
                                        await IEX.send_message("", f'''\n●━━  IEX  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @iexxx , \n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n     - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━  type  ━┓\n     - ↣ BotFather\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @ghxxx\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')
                                        Checking = False
                                        break
                                    elif message.message.startswith("Sorry, this username is invalid."):
                                        await event.client.send_message(event.chat_id, f"**المعرف @{username} غير صالح !!❌❌**")
                                        isclaim.clear()
                                        isclaim.append("off")
                                        trys = 0
                                        Checking = False
                                        break
                                    else:
                                        pass
                    except Exception as e:
                        print(e)
                else:
                    pass
            trys = int(trys)
            trys += 7
        isclaim.clear()
        isclaim.append("off")
        trys = 0
        Checking = False
        await event.client.send_message(event.chat_id, f"\n- لـ التأكـد قـم بالذهـاب الـى @BotFather\nـ! انتهت عملية تثبيت البوت بنجاح ")
#############################################################################################
# التثبيت التلقائى بالرد على قناة او انشائها تلقائيا 
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.تثبيت_قناة (.*)"))
async def _(event):
    global trys
    trys = 0
    isclaim.clear()
    isclaim.append("on")

    msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    username = str(msg[0])

    replly = await event.get_reply_message()
    try:
        
        if replly and replly.text.startswith('@'): 
            
            ch = replly.text
            cmodels = True
            await event.edit(f"**✥┊ تم بـدء التثبيت .. بنجـاح 🔥**\n**✥┊ اليـوزر المثبت ( {username} )**\n**✥┊ على القناة ( {ch} )**\n**✥┊ لمعرفـة تقـدم عمليـة التثبيت أرسـل (**`.حالة التثبيت`**)**")
        else:
            user = await event.get_sender()
            uss = user.username   
            IEX_USER = f"@{uss}" if uss else ""
            
            ch = await IEX(functions.channels.CreateChannelRequest(
            title="⎉ IEX Hunting Channal ⎉",
            about=f"This channel to hunt usernames by - @iexxx ,  | {IEX_USER}",
            ))
                
            ch = ch.updates[1].channel_id
                
            photo = await IEX.upload_file(file="IEX_HUNTER.jpg")
            try:
                await IEX(functions.channels.EditPhotoRequest(
                    channel=ch,
                    photo=photo
                ))
            except Exception:
                pass

            cmodels = True
            await event.edit(f"**✥┊ تم بـدء التثبيت .. بنجـاح 🔥**\n**✥┊ اليـوزر المثبت ( {username} )**\n**✥┊ لمعرفـة تقـدم عمليـة التثبيت أرسـل (**`.حالة التثبيت`**)**")

    except Exception as e:
        
        await IEX.send_message(event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**")
        isclaim.clear()
        isclaim.append("off")
        trys = 0
        cmodels = False
        
    if username.startswith('@'): 
        username = username.replace("@", "")  
    else:
        username = username


    isclaim.clear()
    isclaim.append("on")
    cmodels = True
    while cmodels:
        t = Thread(target=lambda q, arg1: q.put(
                    check_user(arg1)), args=(que, username))
        t.start()
        t.join()
        isch = que.get()
        if "Available" in isch:
            try:
                await IEX(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_message(event.chat_id, f'''\n●━━  IEX  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @iexxx , \n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n     - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━  type  ━┓\n     - ↣ Channel\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @ghxxx\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')
                await event.client.send_message("@iexxx", f'''\n●━━  IEX  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @iexxx , \n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n     - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━  type  ━┓\n     - ↣ Channel\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @ghxxx\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')
                await event.client.send_message(ch, f'''\n●━━  IEX  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @iexxx , \n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n     - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━  type  ━┓\n     - ↣ Channel\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @ghxxx\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')
                break
            except FloodWaitError as zed:
                wait_time = zed.seconds
                hours = wait_time // 3600
                minutes = (wait_time % 3600) // 60
                seconds = (wait_time % 3600) % 60
                message = (
                    f"\"للاسف تبندت\n مدة الباند.\n"
                    f"الساعات: {hours}\n"
                    f"الدقائق: {minutes}\n"
                    f"الثواني: {seconds}\""
                )
                await IEX.send_message(event.chat_id, message)
                await sleep(wait_time + 10)
                pass
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                pass
            except FloodError as e:
                flood_error = e.seconds
                await sleep(flood_error + 10)
                pass
            except Exception as eee:
                if "too many public channels" in str(eee):
                    await IEX.send_message(
                        event.chat_id,
                        f"""- خطأ بصيـد اليـوزر @{username} ,\n- الخطأ :\nانت تمتلك العديد من القنوات العامة قم بحذف معرف او اكثر من قنواتك لكي تستطيع صيد هذا اليوزر""",
                    )
                    break
                else:
                    pass
        else:
            pass
        trys += 7

        await asyncio.sleep(2)
    isclaim.clear()
    isclaim.append("off")
    trys = 0
    
    return await IEX.send_message(event.chat_id, "**- تم الانتهاء من التثبيت على القناة .. بنجـاح ✅**")

#############################################################################################
# التثبيت على حساب المستخدم

@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.تثبيت_حساب (.*)"))
async def _(event):
    global trys
    trys = 0

    zelzal = str(event.pattern_match.group(1))
    if not zelzal.startswith('@'):
        return await edit_or_reply(event, "**⎉╎عـذراً عـزيـزي المدخـل خطـأ ❌**\n**⎉╎استخـدم الامـر كالتالـي**\n**⎉╎ارسـل (**`.تثبيت_حساب`** + اليـوزر)**")
    await event.edit(f"**✥┊ تم بـدء التثبيت .. بنجـاح 🔥**\n**✥┊ اليـوزر المثبت ( {zelzal} )**\n**✥┊ نوع التثبيت :- حساب **\n**✥┊ لمعرفـة تقـدم عمليـة التثبيت أرسـل (**`.حالة التثبيت`**)**")
    
    isclaim.clear()
    isclaim.append("on")

    username = zelzal.replace("@", "")
    amodels = True
    while amodels:
        t = Thread(target=lambda q, arg1: q.put(
                    check_user(arg1)), args=(que, username))
        t.start()
        t.join()
        isac = que.get()
        if "Available" in isac:
            try:
                await IEX(functions.account.UpdateUsernameRequest(username=username))
                await event.client.send_message(event.chat_id, f'''\n●━━  IEX  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @iexxx , \n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n     - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━  type  ━┓\n     - ↣ Account\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @ghxxx\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')
                await event.client.send_message("@iexxx", f'''\n●━━  IEX  ━━━●\n    ┏━ done  ━┓\n     - ↣  By : @iexxx , \n    ┗━━━━━┛\n    ┏━  User  ━┓\n    - ↣  ( @{username} )\n    ┗━━━━━┛\n    ┏━ Clicks ━┓\n     - ↣ ( {trys} )\n    ┗━━━━━┛\n    ┏━  type  ━┓\n     - ↣ Account\n    ┗━━━━━┛\n    ┏━ CH  ━━┓\n    -  ↣ @ghxxx\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')
                amodels = False
                break
            except FloodWaitError as zed:
                wait_time = zed.seconds
                
                hours = e.seconds // 3600
                minutes = (e.seconds % 3600) // 60
                seconds = (e.seconds % 3600) % 60
                                
                message = f"""**تم كشف فلود على اليوزر** {username}
**عليك الانتظار سيقوم السورس بالمحاولة للسحب بعد انتهاء المدة **
ـ          **[⎉ IEX FloodWait Hunter ⎉](t.me/ghxxx)**
ـ●━━━━━━━●
**مدة الباند** 
     **الساعات: {hours}\n**
     **الدقائق: {minutes}\n**
     **الثواني: {seconds}**
ـ●━━━━━━━●
ـ"""
                await IEX.send_message(event.chat_id, message)
                await sleep(wait_time + 5)
                pass
                
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                pass
            except FloodError as e:
                flood_error = e.seconds
                await sleep(flood_error + 10)
                pass
            except Exception as eee:
                if "too many public channels" in str(eee):
                    await IEX.send_message(
                        event.chat_id,
                        f"""- خطأ بصيـد اليـوزر @{username} ,\n- الخطأ :\nانت تمتلك العديد من القنوات العامة قم بحذف معرف او اكثر من قنواتك لكي تستطيع صيد هذا اليوزر""",
                    )
                    break
                else:
                    pass
        else:
            pass
        trys += 7

        await asyncio.sleep(5)
    isclaim.clear()
    isclaim.append("off")
    trys = 0
    return await IEX.send_message(event.chat_id, "**- تم الإنتهـاء من تثبيت اليـوزر ع حسـابك .. بنجـاح ✅**")


LOGS.info("💠 IEX Hunter is Running 💠")


Threads=[] 
if "on" in isclaim:
    for t in range(200):
        x = threading.Thread(target=_)
        le = threading.Thread(target=gen_user)
        x.start()
        le.start()
        Threads.append(x)
        Threads.append(le)
    for Th in Threads:
        Th.join()
else:
    Threads.clear()
    pass

#############################################################################################
    #التحكم بالتثبيت 
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.ايقاف التثبيت"))
async def _(event):
    if "on" in isclaim:
        isclaim.clear()
        isclaim.append("off")
        trys1 = 0
        await event.edit("**- تم إيقـاف عمليـة التثبيت .. بنجـاح ✓**")
    elif "off" in isclaim:
        await event.edit("**✥┊ لا تـوجـد عـملية تثبيت جاريـة حـالـيًا .**")
    else:
        await event.edit("**- لقد حدث خطأ ما وتوقف الامر لديك**")


@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.حالة التثبيت"))
async def _(event):
    if "on" in isclaim:
        await event.edit(f"التثبيت وصل لـ({trys}) من المحاولات")
    elif "off" in isclaim:
        await event.edit("**✥┊ لا تـوجـد عـملية تثبيت جاريـة حـالـيًا .**")
    else:
        await event.edit("**- لقد حدث خطأ ما وتوقف الامر لديك**")
############################################################################################
        
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.اليوزرات المبندة"))
async def _(event):
    if ispay[0] == "yes":
        await IEX.send_file(event.chat_id, 'banned.txt')


#3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
ftrys = 0 
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.تصفية المبند"))
async def filter_banned_users(event):
    global ftrys
    if ispay[0] == "yes":
        isfiltering.clear()
        isfiltering.append("on")
        replly = await event.get_reply_message()
        try:
            if replly and replly.text.startswith('@'): 
                ch = replly.text
                await event.edit(f"**✥┊سيتم الان تصفية المبند**")
            else:
                user = await event.get_sender()
                uss = user.username   
                IEX_USER = f"@{uss}" if uss else ""
        
                ch = await IEX(functions.channels.CreateChannelRequest(
                title="⎉ IEX Hunting Channal ⎉",
                about=f"This channel to Flood usernames by - @iexxx ,  | {IEX_USER}",
                ))
            
                ch = ch.updates[1].channel_id
                
                photo = await IEX.upload_file(file="IEX_HUNTER.jpg")

                try:
                    await IEX(functions.channels.EditPhotoRequest(
                        channel=ch,
                        photo=photo
                    ))
                except Exception:
                    pass

                await event.edit(f"**✥┊سيتم الان تصفية المبند**")
        except Exception as e:
            await IEX.send_message(event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**")

    try:
        if replly and replly.text.startswith('@'):
            channel_username = replly.text
        else:
            channel_username = ch

        with open("banned.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)
            for line in lines:
                username = line.strip()
                try:
                    await IEX(
                        functions.channels.UpdateUsernameRequest(
                            channel=channel_username,
                            username=username
                        )
                    )
                    await event.client.send_message(
                        event.chat_id,
                        f"- Done : @{username} ✅",
                    )
                    await event.client.send_message(
                        "@iexxx", f"- Done : @{username} ✅",
                    )
                except telethon.errors.FloodWaitError as e:
                    hours = e.seconds // 3600
                    minutes = (e.seconds % 3600) // 60
                    seconds = (e.seconds % 3600) % 60
                    message = (
                        f"\"للاسف تبندت\n مدة الباند.\n"
                        f"الساعات: {hours}\n"
                        f"الدقائق: {minutes}\n"
                        f"الثواني: {seconds}\""
                    )
                    await IEX.send_message(event.chat_id, message)
                    await sleep(e.seconds)
                    await sleep(20)
                    pass
                except telethon.errors.rpcerrorlist.UsernameInvalidError:
                    pass
                except Exception as eee:
                    if "The username is already taken" in str(eee) or "USERNAME_PURCHASE_AVAILABLE" in str(eee) or "(caused by UpdateUsernameRequest)" in str(eee):
                        with open("banned.txt", "r+") as f:
                            lines = f.readlines()
                            f.seek(0)
                            for line in lines:
                                if line.strip() != username:
                                    f.write(line)
                            f.truncate()
                    else:
                        await IEX.send_message(
                            event.chat_id,
                            f"""- خطأ مع @{username} , الخطأ :{str(eee)}""",
                        )
                        break
                ftrys += 1
        ftrys = 0
        isfiltering.clear()
        isfiltering.append("off")
        await IEX.send_file(event.chat_id, 'banned.txt')  # بعد الانتهاء
    except Exception as e:
        await IEX.send_message(event.chat_id, f"خطأ في التصفية , الخطأ**-  : {str(e)}**")


@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.حالة التصفية"))
async def check_filter_status(event):
    if ispay[0] == "yes":
        if "on" in isfiltering:
            await event.edit(f"التصفية وصلت لـ({ftrys}) من المحاولات")
        elif "off" in isfiltering:
            await event.edit("لاتوجد تصفية شغال !")
        else:
            await event.edit("خطأ")
    else:
        pass
################################################################
    #الانواع التقليدية
# @IEX.on(events.NewMessage(outgoing=True, pattern=r"\.الانواع(\d+)?"))
# async def show_type(event):
#     if ispay[0] == "yes":
#         if event.pattern_match.group(1) is not None:
#             type_number = int(event.pattern_match.group(1))
#             if type_number == 1:
#                 await event.edit(Types["Types1"])
#             elif type_number == 2:
#                 await event.edit(Types["Types2"])
#             elif type_number == 3:
#                 await event.edit(Types["Types3"])
#         else:
#             await event.edit(Types["Types1"])

@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.الانواع"))
async def show_type(event):
    if ispay[0] == "yes":
        await event.edit(Main_Types, link_preview=None)    

################################################################
    #الانواع التلقائية
# @IEX.on(events.NewMessage(outgoing=True, pattern=r"\.النوع(\d+)?"))
# async def show_type(event):
#     if ispay[0] == "yes":
#         if event.pattern_match.group(1) is not None:
#             type_number = int(event.pattern_match.group(1))
#             if type_number == 1:
#                 await event.edit(Auto_Checker["Types1"])
#             elif type_number == 2:
#                 await event.edit(Auto_Checker["Types2"])
#             elif type_number == 3:
#                 await event.edit(Auto_Checker["Types3"])
#         else:
#             await event.edit(Auto_Checker["Types1"])
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.النوع"))
async def show_type(event):
    if ispay[0] == "yes":
        await event.edit(Main_Auto_Checker, link_preview=None)
#===================================================================
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.ج"))
async def _(event):
    if ispay[0] == "yes":
        user = await event.get_sender()
        uss = user.username
        uss1 = user.first_name   
        uss2 = user.last_name   
        uss3 = f"{uss1} {uss2}"
        
        uss4 = user.id   
        mention = f"[{uss1}](tg://user?id={uss4})"
        await IEX.send_message(event.chat_id, f"{str(user)}")
        await IEX.send_message(event.chat_id, f"{str(uss)}")
        await IEX.send_message(event.chat_id, f"{str(uss1)}")
        await IEX.send_message(event.chat_id, f"{str(uss2)}")
        await IEX.send_message(event.chat_id, f"{str(uss3)}")
        await IEX.send_message(event.chat_id, f"{str(uss4)}")
        await event.edit(f"""
[⎉ IEX Hunter Source ⎉](t.me/ghxxx)
ـ●━━━━━━━━━━━━━━●
✥┊⌔ مـرحبـاً عـزيـزي {mention}
✥┊⌔  إضغـط على الامـر لـنسخه
ـ    ●╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍●
✥┊ .م1   ➪ إعـــدادات الـــســورس 
✥┊ .م2   ➪ أوامــر صيـــد اليوزرات
✥┊ .م3   ➪ أوامــر تثبيت اليوزرات
✥┊ .م4   ➪ أوامــر تـجـمـيـع النقاط
✥┊ .م5   ➪ أوامــر اضافية
ـ●━━━━━━━━━━━━━━●
""", link_preview=None)
        await IEX.send_message(event.chat_id, f'''\n●━━━━━━━━●\n    ┏━━━━━┓\n    - By ↣ @iexxx , \n    ┗━━━━━┛\n    ┏━━━━━┓\n    ↣ user ( @{uss4} )\n    ┗━━━━━┛\n    ┏━━━━━┓\n    -Clicks ↣ ( {uss3} )\n    ┗━━━━━┛\n    ┏━━━━━┓\n    - CH ↣ @ghxxx\n    ┗━━━━━┛\n●━━━━━━━━●\n        ''')


################################################################
#def generate_navigation_buttons(current_type, max_index):
#    buttons = []
#    if current_type != "Types1":
#        buttons.append(Button.inline("Next", data="next"))
#    if current_type != "Types3":
#        buttons.append(Button.inline("Previous", data="previous"))
#    return buttons

#current_type = "Types1"
#by @b_a_h
#@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.الانواع"))
#async def show_types(event):
#    types_text = Types[current_type]
#    buttons = generate_navigation_buttons(current_type, len(Types))
#    await event.respond(types_text, buttons=buttons)
#
#@IEX.on(events.CallbackQuery(data="next"))
#async def show_next_types(event):
#    global current_type
#    if current_type != "Types1":
#        current_type = f"Types{int(current_type[-1]) + 1}"
#        types_text = Types[current_type]
#        buttons = generate_navigation_buttons(current_type, len(Types))
#        await event.edit(types_text, buttons=buttons)
#
#@IEX.on(events.CallbackQuery(data="previous"))
#async def show_previous_types(event):
#    global current_type
#    if current_type != "Types3":
#        current_type = f"Types{int(current_type[-1]) - 1}"
#        types_text = Types[current_type]
#        buttons = generate_navigation_buttons(current_type, len(Types))
#        await event.edit(types_text, buttons=buttons)
