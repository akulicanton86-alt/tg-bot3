import telebot
import re
import threading
import requests
import time
import os
from telebot import types

# Добавьте это в САМОМ НАЧАЛЕ для отладки
print("🚀 Бот запускается...")
print(f"📁 Текущая директория: {os.getcwd()}")
print(f"📂 Файлы в директории: {os.listdir('.')}")

try:
    bot = telebot.TeleBot(token='8792774006:AAFEFoiURdV6STK52VCb_KopSFmMrPPIrqA')
    print("✅ Токен загружен")
except Exception as e:
    print(f"❌ Ошибка токена: {e}")
    exit(1)

# --- НАСТРОЙКИ ---
BEST_CHANNEL_LINK = "https://t.me/+khaTEBu3P-pjNzB1"
BEST_CHANNEL_NAME = "@KLICHAAAAA"

# --- НАСТРОЙКИ ФАЙЛОВ ---
# ВАЖНО: Проверяем существование файлов
print("\n📁 Проверка файлов:")

PHOTO1_PATH = "krasotka1.jpg"  # Упрощаем путь
PHOTO2_PATH = "krasotka2.jpg"
PHOTO3_PATH = "krasotka3.jpg"
VIDEO1_PATH = "video1.mp4"
AUDIO1_PATH = "music1.m4a"
AUDIO2_PATH = "music2.m4a"

# Проверяем каждый файл
files_to_check = [PHOTO1_PATH, PHOTO2_PATH, PHOTO3_PATH, VIDEO1_PATH, AUDIO1_PATH, AUDIO2_PATH]
for file_path in files_to_check:
    if os.path.exists(file_path):
        print(f"✅ Найден: {file_path}")
    else:
        print(f"❌ НЕ НАЙДЕН: {file_path}")

# --- ФУНКЦИЯ ПИНГА (упрощенная) ---
def keep_alive():
    """Простой пинг чтобы бот не засыпал"""
    while True:
        try:
            # Пинг через Telegram API (не требует URL)
            bot.get_me()
            print(f"💓 Пинг в {time.strftime('%H:%M:%S')}")
        except Exception as e:
            print(f"⚠️ Ошибка пинга: {e}")
        time.sleep(40)

# --- ОСТАЛЬНОЙ ВАШ КОД (clean_text, main_menu_keyboard и т.д.) ---
def clean_text(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'[^\w\s]', '', text)
    return text

def main_menu_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("👤 Кто такая Ксюня?", callback_data="ksyuna")
    btn2 = types.InlineKeyboardButton("👀 Видел махнатку?", callback_data="mahnatka")
    btn3 = types.InlineKeyboardButton("⭐️ Главная способность", callback_data="ability")
    btn4 = types.InlineKeyboardButton("🔥 Лучший ТГК", callback_data="best_channel")
    btn5 = types.InlineKeyboardButton("💃 Красотка (3 фото + видео)", callback_data="krasotka")
    btn6 = types.InlineKeyboardButton("🎵 Любимая музыка", callback_data="music")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    return markup

@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "👋 Привет! Я бот с ответами на разные запросы.\n\nНажми на кнопку ниже, чтобы выбрать действие:", reply_markup=main_menu_keyboard())

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
        # Отправляем файлы с проверкой
        for i, (path, caption) in enumerate([
            (PHOTO1_PATH, "💃 Первое фото!"),
            (PHOTO2_PATH, "🌸 Второе фото!"),
            (PHOTO3_PATH, "✨ Третье фото!"),
        ], 1):
            if os.path.exists(path):
                try:
                    with open(path, 'rb') as f:
                        bot.send_photo(call.message.chat.id, f, caption=caption)
                except Exception as e:
                    bot.send_message(call.message.chat.id, f"❌ Ошибка фото{i}: {e}")
            else:
                bot.send_message(call.message.chat.id, f"❌ Нет файла: {path}")
                if os.path.exists(VIDEO1_PATH):
            try:
                with open(VIDEO1_PATH, 'rb') as f:
                    bot.send_video(call.message.chat.id, f, caption="🎬 Видео!")
            except Exception as e:
                bot.send_message(call.message.chat.id, f"❌ Ошибка видео: {e}")
        else:
            bot.send_message(call.message.chat.id, f"❌ Нет файла: {VIDEO1_PATH}")
    
    elif call.data == "music":
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
    
    bot.answer_callback_query(call.id)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = clean_text(message.text)
    
    if text in ["кто такая ксюня", "кто такая ксюна"]:
        bot.send_message(message.chat.id, "Это повелительница галактик которая высмаркивает маслины и черные арбузы с икрой")
    elif text in ["видел ли он махнатку она услышала", "видел ли он махнатку"]:
        bot.send_message(message.chat.id, "да")
    elif text == "главная способность":
        bot.send_message(message.chat.id, "вешалка")
    elif text in ["лучший тгк", "лучший телеграм канал", "топ тгк", "лучший тг"]:
        bot.send_message(message.chat.id, f"🔥 Лучший Telegram-канал: {BEST_CHANNEL_NAME}\n👉 {BEST_CHANNEL_LINK}")
    elif text in ["красотка", "красотка фото", "скинь красотку"]:
        # Аналогично отправке из callback
        for path, caption in [(PHOTO1_PATH, "💃 Первое фото!"), (PHOTO2_PATH, "🌸 Второе фото!"), (PHOTO3_PATH, "✨ Третье фото!")]:
            if os.path.exists(path):
                with open(path, 'rb') as f:
                    bot.send_photo(message.chat.id, f, caption=caption)
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
        bot.send_message(message.chat.id, "❓ Не понял запрос.\n\nНажми /start, чтобы открыть меню с кнопками!", reply_markup=main_menu_keyboard())

# --- ЗАПУСК ---
if name == "main":
    print("\n🎯 Запускаем бота...")
    
    # Запускаем пинг в отдельном потоке
    ping_thread = threading.Thread(target=keep_alive, daemon=True)
    ping_thread.start()
    print("🔄 Пинг-сервис запущен")
    
    print("✅ Бот готов к работе!")
    
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"❌ Критическая ошибка: {e}")
        exit(1)
