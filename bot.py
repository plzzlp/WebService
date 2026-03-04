import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Bot Token ကို ဒီနေရာမှာ ထည့်ပါ
BOT_TOKEN = '8725144078:AAGjdSgr_detzhsVgPGC4h8RT6V9S8x8LSg'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    # Game Link (ဖုန်းနံပါတ် တစ်ခါတည်း ထည့်ထားချင်ရင် mobile=96xxxxxx ဆိုပြီး ပေါင်းထည့်နိုင်ပါတယ်)
    game_url = "https://sheepblock.com/index/land?channelId=myid"

    # ခလုတ်ဖန်တီးခြင်း
    markup = InlineKeyboardMarkup()
    
    # Telegram Web App ကိုသုံးပြီး Telegram ထဲမှာပဲ ပွင့်စေမယ့် ခလုတ်
    button = InlineKeyboardButton(
        text="🎮 ကစားရန်", 
        web_app=WebAppInfo(url=game_url)
    )
    markup.add(button)

    # Bot မှ ပြန်ပို့မည့် စာသား
    bot.reply_to(message, "မင်္ဂလာပါ။ 🕹️\nအောက်ပါ **ကစားရန်** ခလုတ်ကို နှိပ်ပြီး Telegram ထဲမှာတင် တိုက်ရိုက် ကစားနိုင်ပါတယ်။", reply_markup=markup)

if __name__ == '__main__':
    print("Bot is running...")
    bot.infinity_polling()

