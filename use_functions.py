"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
import os

balance = 0

if os.path.isfile("data.txt"):
    file = open("data.txt", "r")
    balance = int(file.read())
    file.close()

basket = []

if os.path.isfile("basket.txt"):
    file = open("basket.txt", "r")

    for line in file:
        basket.append(line)

    file.close()

while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    print('5. тестирование')

    choice = input('Выберите пункт меню')
    if choice == '1':
        amount = int(input('Введите сумму пополнения:'))
        balance = balance + amount
        pass
    elif choice == '2':
        amount = int(input('Введите сумму покупки:'))
        if balance >= amount:
            item = str(input('Введите название покупки:'))
            basket.append(item + ' ' + str(amount))
            balance = balance - amount
        else:
            print('Денег не хватает')
        pass
    elif choice == '3':
        for item in basket:
            print(item)
        pass
    elif choice == '4':
        file = open("data.txt", "w")
        file.write(str(balance))
        file.close()

        file = open("basket.txt", "w")
        for i in basket:
            file.write(i + '\n')
        file.close()
        break
    elif choice == '5':
        file = open("data.txt", "r")

        print(balance == int(file.read()))
        file.close()

        file = open("basket.txt", "r")

        basketf = file.read()

        baskets = ''
        baskets = baskets.join(basket)

        print(baskets == basketf)
        file.close()

        pass
    else:
        print('Неверный пункт меню')
