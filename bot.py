import telebot
import re
import os
from telebot import types

bot = telebot.TeleBot(token='8792774006:AAFEFoiURdV6STK52VCb_KopSFmMrPPIrqA')

# --- НАСТРОЙКИ ССЫЛКИ НА КАНАЛ ---
BEST_CHANNEL_LINK = "https://t.me/+khaTEBu3P-pjNzB1"
BEST_CHANNEL_NAME = "@KLICHAAAAA"

# --- НАСТРОЙКИ ФАЙЛОВ ---
# Фото (3 штуки)
PHOTO1_PATH = os.path.join(os.path.dirname(__file__), "krasotka1.jpg")
PHOTO2_PATH = os.path.join(os.path.dirname(__file__), "krasotka2.jpg")
PHOTO3_PATH = os.path.join(os.path.dirname(__file__), "krasotka3.jpg")

# Видео (1 штука)
VIDEO1_PATH = os.path.join(os.path.dirname(__file__), "video1.mp4")

# Музыка/Аудио (2 штуки)
AUDIO1_PATH = os.path.join(os.path.dirname(__file__), "music1.m4a")
AUDIO2_PATH = os.path.join(os.path.dirname(__file__), "music2.m4a")

def clean_text(text: str) -> str:
    """Удаляет знаки препинания и приводит к нижнему регистру"""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s]', '', text)
    return text

# --- ГЛАВНОЕ МЕНЮ С КНОПКАМИ ---
def main_menu_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("👤 Кто такая Ксюня?", callback_data="ksyuna")
    btn2 = types.InlineKeyboardButton("👀 Видел махнатку?", callback_data="mahnatka")
    btn3 = types.InlineKeyboardButton("⭐ Главная способность", callback_data="ability")
    btn4 = types.InlineKeyboardButton("🔥 Лучший ТГК", callback_data="best_channel")
    btn5 = types.InlineKeyboardButton("💃 Красотка (3 фото + видео)", callback_data="krasotka")
    btn6 = types.InlineKeyboardButton("🎵 Любимая музыка", callback_data="music")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    return markup

@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(
        message.chat.id, 
        "👋 Привет! Я бот с ответами на разные запросы.\n\nНажми на кнопку ниже, чтобы выбрать действие:",
        reply_markup=main_menu_keyboard()
    )

# --- ОБРАБОТЧИК НАЖАТИЙ НА КНОПКИ ---
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "ksyuna":
        bot.send_message(call.message.chat.id, "Это повелительница галактик которая высмаркивает маслины и черные арбузы с икрой")
    
    elif call.data == "mahnatka":
        bot.send_message(call.message.chat.id, "да")
    
    elif call.data == "ability":
        bot.send_message(call.message.chat.id, "вешалка")
    
    elif call.data == "best_channel":
        bot.send_message(call.message.chat.id, f"🔥 Лучший Telegram-канал: {BEST_CHANNEL_NAME}\n👉 {BEST_CHANNEL_LINK}")
    
    elif call.data == "krasotka":
        # Отправляем 3 фото + 1 видео
        # Фото 1
        if os.path.exists(PHOTO1_PATH):
            try:
                with open(PHOTO1_PATH, 'rb') as f:
                    bot.send_photo(call.message.chat.id, f, caption="💃 Первое фото!")
            except Exception as e:
                bot.send_message(call.message.chat.id, f"❌ Ошибка фото1: {e}")
        else:
            bot.send_message(call.message.chat.id, f"❌ Нет файла: {PHOTO1_PATH}")
        
        # Фото 2
        if os.path.exists(PHOTO2_PATH):
            try:
                with open(PHOTO2_PATH, 'rb') as f:
                    bot.send_photo(call.message.chat.id, f, caption="🌸 Второе фото!")
            except Exception as e:
                bot.send_message(call.message.chat.id, f"❌ Ошибка фото2: {e}")
        else:
            bot.send_message(call.message.chat.id, f"❌ Нет файла: {PHOTO2_PATH}")
        
        # Фото 3
        if os.path.exists(PHOTO3_PATH):
            try:
                with open(PHOTO3_PATH, 'rb') as f:
                    bot.send_photo(call.message.chat.id, f, caption="✨ Третье фото!")
            except Exception as e:
                bot.send_message(call.message.chat.id, f"❌ Ошибка фото3: {e}")
            
        
        # Видео
        if os.path.exists(VIDEO1_PATH):
            try:
                with open(VIDEO1_PATH, 'rb') as f:
                    bot.send_video(call.message.chat.id, f, caption="🎬 Видео!")
            except Exception as e:
                bot.send_message(call.message.chat.id, f"❌ Ошибка видео: {e}")
        else:
            bot.send_message(call.message.chat.id, f"❌ Нет файла: {VIDEO1_PATH}")
    
    elif call.data == "music":
        # Отправляем 2 аудио
        if os.path.exists(AUDIO1_PATH):
            try:
                with open(AUDIO1_PATH, 'rb') as f:
                    bot.send_audio(call.message.chat.id, f, caption="🎵 Первая любимая песня!")
            except Exception as e:
                bot.send_message(call.message.chat.id, f"❌ Ошибка аудио1: {e}")
        else:
            bot.send_message(call.message.chat.id, f"❌ Нет файла: {AUDIO1_PATH}")
        
        if os.path.exists(AUDIO2_PATH):
            try:
                with open(AUDIO2_PATH, 'rb') as f:
                    bot.send_audio(call.message.chat.id, f, caption="🎶 Вторая любимая песня!")
            except Exception as e:
                bot.send_message(call.message.chat.id, f"❌ Ошибка аудио2: {e}")
        else:
            bot.send_message(call.message.chat.id, f"❌ Нет файла: {AUDIO2_PATH}")
    
    # Убираем "часики" на кнопке после нажатия
    bot.answer_callback_query(call.id)

# --- ОБРАБОТЧИК ТЕКСТОВЫХ СООБЩЕНИЙ (для обратной совместимости) ---
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    raw_text = message.text
    text = clean_text(raw_text)
    
    print(f"Получено: {raw_text} -> Очищено: {text}")
    
    # Если пользователь пишет текст, тоже отвечаем (дублируем кнопки)
    if text in ["кто такая ксюня", "кто такая ксюна"]:
        bot.send_message(message.chat.id, "Это повелительница галактик которая высмаркивает маслины и черные арбузы с икрой")
    elif text in ["видел ли он махнатку она услышала", "видел ли он махнатку"]:
        bot.send_message(message.chat.id, "да")
    elif text == "главная способность":
        bot.send_message(message.chat.id, "вешалка")
    elif text in ["лучший тгк", "лучший телеграм канал", "топ тгк", "лучший тг"]:
        bot.send_message(message.chat.id, f"🔥 Лучший Telegram-канал: {BEST_CHANNEL_NAME}\n👉 {BEST_CHANNEL_LINK}")
    elif text in ["красотка", "красотка фото", "скинь красотку"]:
        # Тот же код для красотки что и выше (можно вынести в отдельную функцию)
        if os.path.exists(PHOTO1_PATH):
            with open(PHOTO1_PATH, 'rb') as f:
                bot.send_photo(message.chat.id, f, caption="💃 Первое фото!")
        if os.path.exists(PHOTO2_PATH):
            with open(PHOTO2_PATH, 'rb') as f:
                bot.send_photo(message.chat.id, f, caption="🌸 Второе фото!")
        if os.path.exists(PHOTO3_PATH):
            with open(PHOTO3_PATH, 'rb') as f:
                bot.send_photo(message.chat.id, f, caption="✨ Третье фото!")
        if os.path.exists(VIDEO1_PATH):
            with open(VIDEO1_PATH, 'rb') as f:
                bot.send_video(message.chat.id, f, caption="🎬 Видео!")
    elif text in ["любимая музыка", "музыка", "песня", "моя музыка"]:
        if os.path.exists(AUDIO1_PATH):
            with open(AUDIO1_PATH, 'rb') as f:
                bot.send_audio(message.chat.id, f, caption="🎵 Первая любимая песня!")
        if os.path.exists(AUDIO2_PATH):
            with open(AUDIO2_PATH, 'rb') as f:
                bot.send_audio(message.chat.id, f, caption="🎶 Вторая любимая песня!")
    else:
        bot.send_message(message.chat.id, 
            "❓ Не понял запрос.\n\nНажми /start, чтобы открыть меню с кнопками!",
            reply_markup=main_menu_keyboard()
        )

print("✅ Бот запущен с кнопками!")
bot.polling()