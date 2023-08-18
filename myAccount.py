def myAcc():
    balance = 0
    basket = []
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

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
            break
        else:
            print('Неверный пункт меню')