import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# ضع التوكن الخاص بك هنا
TOKEN = "7904303309:AAEEi663Ce43Rxnq25EsAb1BJsEnvgbJ17I"

# إعداد اللوج
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# دالة البدء
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("عن الجامعة", callback_data="about")],
        [InlineKeyboardButton("الكليات", callback_data="colleges")],
        [InlineKeyboardButton("الأخبار", callback_data="news")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("مرحبًا بك في جامعة السراج 👋\nاختر من القائمة:", reply_markup=reply_markup)

# دالة الضغط على الأزرار
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "about":
        await query.edit_message_text("📖 جامعة السراج: جامعة أهلية تهدف إلى تقديم تعليم متميز وحديث.")
    elif query.data == "colleges":
        await query.edit_message_text("🏫 الكليات:\n- كلية تقنيات الأمن السيبراني\n- كلية تقنيات الذكاء الاصطناعي\n- كلية تقنيات البناء والإنشاءات\n- كلية تقنيات هندسة النفط والغاز\n- كلية تقنيات الهندسة الطبية")
    elif query.data == "news":
        await query.edit_message_text("📰 لا توجد أخبار حالياً. ترقبوا التحديثات.")

# دالة المساعدة
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("استخدم /start للبدء 🚀")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CallbackQueryHandler(button))

    app.run_polling(allowed_updates=Update.ALL_TYPES)
if __name__ == "__main__":
    main()
