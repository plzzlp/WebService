import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Bot Token ကို ဒီနေရာမှာ ထည့်ပါ
BOT_TOKEN = '8725144078:AAGjdSgr_detzhsVgPGC4h8RT6V9S8x8LSg'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    text = ("🕹️ **Sheep Game Bot မှ ကြိုဆိုပါတယ်**\n\n"
            "Telegram ထဲမှာတင် တိုက်ရိုက်ကစားဖို့ ဖုန်းနံပါတ်ရိုက်ထည့်ပါ။\n"
            "ဥပမာ - `/game 09######` (နှိပ်ပြီး copy ကူးနိုင်သည်)")
    bot.reply_to(message, text, parse_mode="Markdown")

@bot.message_handler(commands=['game'])
def send_game_link(message):
    try:
        parts = message.text.split()
        if len(parts) < 2:
            bot.reply_to(message, "⚠️ ကျေးဇူးပြု၍ ဖုန်းနံပါတ် ထည့်ပေးပါ။\nဥပမာ - `/game 09$####`", parse_mode="Markdown")
            return

        phone_number = parts[1]
        
        # အရှေ့က 09 ပါလာရင် ဖြတ်ထုတ်ပေးမယ် (System နဲ့ ကိုက်ညီအောင်)
        clean_phone = phone_number
        if clean_phone.startswith('09'):
            clean_phone = clean_phone[2:]
        elif clean_phone.startswith('9'):
            clean_phone = clean_phone # 9 နဲ့စရင် အိုကေတယ်

        # Game Link တည်ဆောက်ခြင်း
        game_url = f"https://sheepblock.com/index/land?mobile={clean_phone}&channelId=myid"

        # WebAppInfo သုံးပြီး Telegram ထဲမှာတင် ပွင့်အောင် လုပ်ခြင်း
        markup = InlineKeyboardMarkup()
        # ဒီနေရာမှာ web_app parameter ကို သုံးထားပါတယ်
        button = InlineKeyboardButton(
            text="🎮 ဂိမ်းကစားရန် (TG ထဲမှာတင်)", 
            web_app=WebAppInfo(url=game_url)
        )
        markup.add(button)

        bot.reply_to(message, f"✅ ဖုန်းနံပါတ် {phone_number} အတွက် အဆင်သင့်ဖြစ်ပါပြီ။\nအောက်ကခလုတ်ကို နှိပ်လိုက်ပါဗျာ။", reply_markup=markup)

    except Exception as e:
        bot.reply_to(message, "❌ အမှားအယွင်းတစ်ခု ဖြစ်သွားပါတယ်။")

if __name__ == '__main__':
    print("Bot is running in Web App mode...")
    bot.infinity_polling()
    
