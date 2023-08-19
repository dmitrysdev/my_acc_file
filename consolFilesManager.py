import os
import shutil
import pathlib
import platform
from myAccount import myAcc
from victory import vic

def getListDir():
    folder = os.getcwd()

    dir = pathlib.Path(folder)
    files = [file.name for file in dir.iterdir() if file.is_file()]

    ret = 'files:'

    for f in files:
        ret = ret + f
        if f != files[-1]:
            ret = ret + ', '

    ret = ret + '\n'

    subdir = []
    with os.scandir(folder) as files:
        subdir = [file.name for file in files if file.is_dir()]

    ret = ret + 'dirs:'

    for f in subdir:
        ret = ret + f
        if f != subdir[-1]:
            ret = ret + ', '

    fileO = open("listdir.txt", "w")
    fileO.write(ret)
    fileO.close()

    return ret

while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории (*необязательный пункт)')
    print('12. выход')
    print('13. сохранить содержимое рабочей директории в файл')
    print('14. тестировать п.13')

    choice = input('Выберите пункт меню')

    if choice == '1':
        folder = str(input('введите название папки:'))

        if os.path.isdir(folder) == False:
            os.mkdir(folder)
        pass
    elif choice == '2':
        folder = str(input('введите название папки:'))

        if os.path.isdir(folder) == True:
            os.rmdir(folder)
        pass
    elif choice == '3':
        folder = str(input('введите название папки:'))
        newfolder = str(input('введите новое название папки:'))

        if os.path.isdir(folder) == True:
            shutil.copytree(folder, newfolder)
        pass
    elif choice == '4':
        folder = str(input('введите название папки:'))

        with os.scandir(folder) as files:
            for file in files:
                print(file.name)
        pass
    elif choice == '5':
        folder = str(input('введите название папки:'))

        with os.scandir(folder) as files:
            subdir = [file.name for file in files if file.is_dir()]

        print(subdir)
        pass
    elif choice == '6':
        folder = str(input('введите название папки:'))

        dir = pathlib.Path(folder)
        files = [file.name for file in dir.iterdir() if file.is_file()]

        print(files)
        pass
    elif choice == '7':

        print(platform.platform())
        pass
    elif choice == '8':

        print('Дмитрий С.')
        pass
    elif choice == '9':
        vic()
        pass
    elif choice == '10':
        myAcc()
        pass
    elif choice == '11':
        folder = str(input('введите название рабочей директории:'))

        os.chdir(folder)
        pass
    elif choice == '12':
        break
    elif choice == '13':
        getListDir()
        pass
    elif choice == '14':
        os.mkdir('test1')
        os.mkdir('test2')
        os.mkdir('test3')

        ld = getListDir()

        file = open("listdir.txt", "r")

        ldf = file.read()

        file.close()

        print(ld == ldf)

        pass
    else:
        print('Неверный пункт меню')