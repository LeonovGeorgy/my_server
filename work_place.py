from datetime import datetime

all_messages = [] # Здесь будем хранить сообщения

def add_message(author, text):  # обьявляем функцию,
                                # в которой параметризуем сообщение
    message = {
        "author": author,
        "text": text,
        "time": datetime.now().strftime("%H:%M:%S")
    }
    all_messages.append(message)  # добавляем в список сообщение

add_message("Сергей", "Привет народ")
add_message("Max", "Как дела?")
add_message(text="какие цветочки!", author="Кирилл")

def print_message(msg):  # форматирование сообщения
    print(f"[{msg['author']}]: {msg['text']} {msg['time']}")

def print_all_messages():  # вывод отформатированных сообщений
    for messege in all_messages:
        print_message(messege)

print_all_messages()