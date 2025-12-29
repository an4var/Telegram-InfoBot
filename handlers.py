from menus import show_main_menu, show_faq_menu, show_contact_menu, show_faq_answer, show_contact_info

def register_handlers(bot):
    @bot.callback_query_handler(func=lambda call: True)
    def callback_handler(call):
        chat_id = call.message.chat.id
        message_id = call.message.message_id
        data = call.data

        if data == "faq":
            show_faq_menu(bot, chat_id, message_id)
        elif data.startswith("faq_"):
            question = data[4:]
            show_faq_answer(bot, chat_id, question, message_id)
        elif data == "contact":
            show_contact_menu(bot, chat_id, message_id)
        elif data.startswith("contact_"):
            contact = data[8:]
            show_contact_info(bot, chat_id, contact, message_id)
        elif data == "back_main":
            show_main_menu(bot, chat_id, message_id)