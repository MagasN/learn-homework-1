"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def chek_strings(string1, string2):
    """
    Эта функция сравнивает строки и выводит результат в зависимости от условия
    """
    if not (isinstance(string1, str) and (isinstance(string2, str))):
            return 0
    if string1 == string2:
         return 1
    elif len(string1) > len(string2) and string2 != 'learn':
        return 2
    elif string1 != string2 and string2 == 'learn':
        return 3
    else:
        return 'other'
        


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    result_dict = {0: "Что-то из введеного не является строкой",
                   1: "Эти строки одинаковые",
                   2: "Первая строка длиннее",
                   3: "Эти строки разные и вторая строка 'learn'",
                   'other': "Данные не проходят ни по одному условию"}
    
    test_str1 = "Хорошего настроения"
    test_str2 = "python"
    test_str3 = "learn"
    test_str4 = "hi"
    test_int = 2023

    print("Вы ввели:", test_int, test_str1, sep='\n\t')
    print(result_dict[chek_strings(test_int, test_str1)], end='\n\n')
    

    print("Вы ввели:", test_str2, test_str2, sep='\n\t')
    print(result_dict[chek_strings(test_str2, test_str2)], end='\n\n')

    print("Вы ввели:", test_str1, test_str2, sep='\n\t')
    print(result_dict[chek_strings(test_str1, test_str2)], end='\n\n')

    print("Вы ввели:", test_str2, test_str3, sep='\n\t')
    print(result_dict[chek_strings(test_str2, test_str3)], end='\n\n')

    print("Вы ввели:", test_str4, test_str2, sep='\n\t')
    print(result_dict[chek_strings(test_str4, test_str2)], end='\n\n')


    
if __name__ == "__main__":
    main()
