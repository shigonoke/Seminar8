# Seminar8 Работа с файлами
# Задача №49. Решение в группах 
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя,
# отчество, номер телефона - данные, которые должны находиться в файле. 1.Программа должна выводить данные 
# 2.Программа должна сохранять данные в текстовом файле 
# 3.Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию 
# человека) 
# 4.Использование функций. Ваша программа не должна быть линейной 
with open('task1.txt', 'w') as f:
    f.write("Ivanov, Ivan, +123")
    f.write("\nPetrov,Petr,+456 ")
    f.write("\nSidorov,Sidr, +789")
def add_user():
    with open('task1.txt', 'a') as f:
        f.write('\n')
        f.write(input('введите Фамилия,Имя,Телефон - '))
def read_all_users():
    with open('task1.txt', 'r') as f:
        for line in f:
            print(line.strip())
def search_user():
    with open('task1.txt', 'r') as f:
        search = input("Что ищем? - ")
        for line in f:
            if search in line:
                print(line.strip())
# else:
#
print("Таких нет")
def info_func():
    print("\n1. Показать весь справочник ")
    print("2. Добавить пользователя ")
    print("3. Поиск пользователя ")
    print("4. Выход")
info_func()
while (user_action := int(input("Выберите функцию, через цифру -"))) != 4:
    match user_action:
        case 1:
            read_all_users()
            info_func()
        case 2:
            add_user()
            info_func()
        case 3:
            search_user()
            info_func()
        case 4:
            break
        case _:
            print("Нет такой функции")