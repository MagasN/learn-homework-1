"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    """
    Замените pass на ваш код
    """
    message = ' '
    while "хорошо" not in message:
        message = input("Как дела?\n").lower()
    print("Так держать!")
    
if __name__ == "__main__":
    hello_user()
