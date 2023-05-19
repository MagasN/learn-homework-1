"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def type_activity(age_user):
    """
    Эта функция, определяющая по возрасту, чем должен заниматься пользователь
    """
    if 3 <= age_user <= 6:
        return "Вы должны ходить в детский сад."
    elif 7 <= age_user < 18:
        return "Вы должны учиться в школе."
    elif 18 <= age_user <= 35:
        return "Вы можете пойти в ВУЗ. А вообще, go на работу, заводик ждёт ^-^."
    elif 35 < age_user <= 65:
        return "Вы скорее всего уже работаете, но никто мешает пойти в ВУЗ."
    else:
        return "Сидим дома, наслаждаемся жизнью."

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    age_user = int(input("Укажите свой возраст: "))
    result_func = type_activity(age_user)
    print(result_func)   

if __name__ == "__main__":
    main()
