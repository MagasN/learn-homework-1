"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
items_sale = [
                {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
                {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
                {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
             ]

def count_sold_avg(sold):
    sum_sold = 0
    for item in sold:
        sum_sold += item
    return [sum_sold, sum_sold / len(sold)]



def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    sum_sold_all = 0
    for item in items_sale:
        sold_avg = round(count_sold_avg(item['items_sold'])[1])
        print(f"{item['product']}")
        print(f"Cуммарное количество продаж: {count_sold_avg(item['items_sold'])[0]}")
        print(f"Среднее количество продаж: {sold_avg}\n")
        sum_sold_all += count_sold_avg(item['items_sold'])[0]

# Выриант решения без функции count_sold_avg()
    # sum_sold_all = 0 
    # for item in items_sale:
    #     sold_sum = sum(item['items_sold'])
    #     sold_avg = round(sold_sum / len(item['items_sold']))
    #     print(f"{item['product']}")
    #     print(f"Cуммарное количество продаж: {sold_sum}")
    #     print(f"Среднее количество продаж: {sold_avg}\n")
    #     sum_sold_all += sold_sum 

    sold_avg_all = round(sum_sold_all / len(items_sale))

    print(f"Общее количество продаж всех товаров: {sum_sold_all}")
    print(f"Cреднее количество продаж всех товаров: {sold_avg_all}\n")

    
    
if __name__ == "__main__":
    main()
