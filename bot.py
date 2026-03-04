import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Bot Token ကို ထည့်ပါ
BOT_TOKEN = '8725144078:AAGjdSgr_detzhsVgPGC4h8RT6V9S8x8LSg'
bot = telebot.TeleBot(BOT_TOKEN)

# /start သို့မဟုတ် /help ကို နှိပ်လျှင် ပြသမည့် စာသား
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    text = ("မင်္ဂလာပါ။ 🕹️\n\n"
            "Game ဆော့ရန် ဖုန်းနံပါတ်ကို အောက်ပါအတိုင်း ရိုက်ထည့်ပါ။\n"
            "👉 ဥပမာ - /09#######")
    bot.reply_to(message, text)

# /game ဟု ရိုက်ထည့်လျှင် အလုပ်လုပ်မည့် အပိုင်း
@bot.message_handler(commands=['game'])
def send_game_link(message):
    try:
        # User ပို့လိုက်သော စာသားကို ခွဲထုတ်ခြင်း (ဥပမာ - /game 09676111042)
        parts = message.text.split()
        
        # ဖုန်းနံပါတ် မပါခဲ့လျှင် သတိပေးမည်
        if len(parts) < 2:
            bot.reply_to(message, "⚠️ ဖုန်းနံပါတ် ထည့်ရန် ကျန်နေပါသည်။\n👉 ဥပမာ - /game 09676111042")
            return

        phone_number = parts[1]
        
        # API Link တည်ဆောက်ခြင်း
        game_url = f"https://sheepblock.com/index/land?mobile={phone_number}&channelId=myid"

        # Telegram တွင် နှိပ်၍ရသော ခလုတ် (Button) ဖန်တီးခြင်း
        markup = InlineKeyboardMarkup()
        # web_app parameter ကို မသုံးချင်ဘဲ ရိုးရိုး Browser နဲ့ ဖွင့်ချင်ပါက url=game_url လို့ ပြောင်းနိုင်ပါသည်
        button = InlineKeyboardButton(text="🕹️ Game ဆော့မည်", url=game_url)
        markup.add(button)

        bot.reply_to(message, f"✅ {phone_number} အတွက် Game Link အဆင်သင့်ဖြစ်ပါပြီ။ အောက်က ခလုတ်ကို နှိပ်ပြီး ဝင်ဆော့နိုင်ပါတယ်။", reply_markup=markup)

    except Exception as e:
        bot.reply_to(message, "❌ အမှားအယွင်းဖြစ်ပေါ်နေပါသည်။")

# Bot ကို အမြဲတမ်း Run နေစေရန်
if __name__ == '__main__':
    print("Bot is running...")
    bot.infinity_polling()
  
