"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за четыре квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import defaultdict


def func(quantity=0, companies=0):
    if not companies:
        companies = defaultdict(float)
    try:
        if not quantity:
            quantity = int(
                input("Введите количество предприятий для расчета прибыли: "))
        while quantity:
            name = input("Введите название предприятия: ")
            profit = list(map(float,
                              input("через пробел введите прибыль данного предприятия "
                                    "\nза каждый квартал(Всего 4 квартала): ").split(' ')))
            if len(profit) != 4:
                print("Количество кварталов должно равняться 4! Повторите ввод данных")
                func(quantity, companies)
            companies[name] = (sum(profit))
            quantity -= 1
    except ValueError as exception:
        print(
            f"Необходимо вводить количество, прибыли в цифрах, в конце пробел недопустим."
            f"\n{exception}\nПовторите ввод данных")
        func(quantity, companies)
    average_all_company_profit = sum(
        [item[1] for item in companies.items()]) / len(companies)
    print(
        f"Средняя годовая прибыль всех предприятий: {average_all_company_profit:.2f}")

    above_average = []
    below_average = []
    for item in companies.items():
        if item[1] > average_all_company_profit:
            above_average.append(item[0])
        elif item[1] < average_all_company_profit:
            below_average.append(item[0])
    print("Предприятия, с прибылью выше среднего значения: ", *above_average)
    print("Предприятия, с прибылью ниже среднего значения: ", *below_average)


func()