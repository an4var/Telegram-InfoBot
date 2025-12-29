from telebot import types
from config import faq_dict, contacts_dict

user_state = {}  # стан користувача

def show_main_menu(bot, chat_id, message_id=None):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("❓ FAQ", callback_data="faq"))
    keyboard.add(types.InlineKeyboardButton("📞 Контакти", callback_data="contact"))

    if message_id:
        bot.edit_message_text("Обери тему, щоб отримати відповідь ⬇️",
                              chat_id=chat_id,
                              message_id=message_id,
                              reply_markup=keyboard)
    else:
        bot.send_message(chat_id, "Обери тему, щоб отримати відповідь ⬇️", reply_markup=keyboard)
    
    user_state[chat_id] = "main"

def show_faq_menu(bot, chat_id, message_id=None):
    keyboard = types.InlineKeyboardMarkup()
    for question in faq_dict:
        keyboard.add(types.InlineKeyboardButton(question, callback_data=f"faq_{question}"))
    keyboard.add(types.InlineKeyboardButton("⬅️ Назад", callback_data="back_main"))

    if message_id:
        bot.edit_message_text("🔎 Обери питання, на яке хочеш отримати відповідь:", 
                              chat_id=chat_id, message_id=message_id, reply_markup=keyboard)
    else:
        bot.send_message(chat_id, "🔎 Обери питання, на яке хочеш отримати відповідь:", reply_markup=keyboard)
    user_state[chat_id] = "faq"

def show_contact_menu(bot, chat_id, message_id=None):
    keyboard = types.InlineKeyboardMarkup()
    for contact in contacts_dict:
        keyboard.add(types.InlineKeyboardButton(contact, callback_data=f"contact_{contact}"))
    keyboard.add(types.InlineKeyboardButton("⬅️ Назад", callback_data="back_main"))

    if message_id:
        bot.edit_message_text("Оберіть спосіб зв’язку з мною 📬", 
                              chat_id=chat_id, message_id=message_id, reply_markup=keyboard)
    else:
        bot.send_message(chat_id, "Оберіть спосіб зв’язку з мною 📬", reply_markup=keyboard)
    user_state[chat_id] = "contact"

def show_faq_answer(bot, chat_id, question, message_id):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("⬅️ Назад", callback_data="faq"))
    bot.edit_message_text(faq_dict[question], chat_id=chat_id, message_id=message_id, reply_markup=keyboard)
    user_state[chat_id] = "answer"

def show_contact_info(bot, chat_id, contact, message_id):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("⬅️ Назад", callback_data="contact"))
    bot.edit_message_text(contacts_dict[contact], chat_id=chat_id, message_id=message_id, reply_markup=keyboard)
    user_state[chat_id] = "info"