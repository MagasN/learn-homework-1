"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""
from random import choice
from re import sub

questions_and_answers = {"привет":["Привет!", "Добрый день!", "Здравствуйте."],
                         "как дела": ["Хорошо!", "Замечательно!", "Бывало и лучше."], 
                         "что делаешь": ["Программирую.", "Пью свой двоичный чай.", "Медитирую."],
                         "погода":["Облачно, возможны осадки.", "Сегодня прекрасный день для прогулки.", "Поздравляю с первым снегом!"],
                         "настроение":["Мне слегка грустно.", "Как и сегодняшний день, прекрасное!", "Готова весь день программировать."]
                        }

def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    while True:
        user_say = input("Скажи что-нибудь. (exit для выхода)\nПользователь: ").lower()
        user_say = sub(r'[.!?]', '', user_say)
        if user_say in answers_dict:
            print(f"Программа: {choice(answers_dict[user_say])}\n")
        elif user_say == "exit":
            print("Программа: Пока.")
            break
        else:
            print("Я пока не придумала ответ.\n")
    
if __name__ == "__main__":
    ask_user(questions_and_answers)
