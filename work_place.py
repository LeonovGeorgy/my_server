from flask import Flask, render_template, request  # импортируем Flask
from datetime import datetime
import json

app = Flask(__name__)  # Создаем экземпляр приложения


# json.dump("что", "во что") - загрузка в файл
# json.load("файл") - чтение файла
def load_messages():  # для чтения файла с сообщениями
    try:              # тут еще проверим, вдруг файла еще нет
        with open("s_m.json", "r") as file:
            data = json.load(file)
        return data["messages"]
    except FileNotFoundError:
        print('Чата еще нет, но мы сделаем!')
        data = []
        return data


try:
    all_messages = load_messages()  # Здесь будем хранить сообщения
except FileNotFoundError:
    print('Чата еще нет, но мы сделаем!')


def add_message(author, text):  # обьявляем функцию,
    #                             в которой параметризуем сообщение
    message = {
        "author": author,
        "text": text,
        "time": datetime.now().strftime("%H:%M:%S")
    }
    all_messages.append(message)  # добавляем в список сообщение
    save_message()


def save_message():  # обновляем словарь и записываем его в файл
    all_messages_data = {
        "messages": all_messages
    }
    with open("s_m.json", "w") as file:
        json.dump(all_messages_data, file)


@app.route("/")  # эмпоинт начальной страницы
def main_page():
    return "Hello Egor"


@app.route("/chat")
def chat_page():
    return render_template("form.html")


@app.route("/get_messages")
def get_messages():
    print("Выводим все сообщения")
    return {"messages": all_messages}


@app.route("/send_message")
def send_message():
    name = request.args.get("name")  # здесь храним данные полученые из query параметров
    text = request.args.get("text")  # тех, что вводим на страничке (как input)
    print(f"Пользователь '{name}' пишет '{text}'")
    add_message(name, text)
    return "ok"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # настраиваем парам. запуска приложения
