import controller as c

# точка запуска программы
print('Программа работы с телефонным справочником')
# загрузка справочника из файла contacts.csv
c.load_contacts()

while True:
    print('Инструкция:')
    print('1 - вывод справочника')
    print('2 - добавление контакта')
    print('3 - удаление контакта')
    print('4 - поиск контакта по имени')
    print('5 - Редактирование контакта')
    print('6 - Выгрузка в формате CSV, txt или JSON')
    print('7 - Загрузка списка контактов из файла CSV')
    print('0 - Завершение работы')
    select = int(input(f'--- введите команду ---> '))
    if select == 0:
        break
    elif select == 1:
        c.list_all()
    elif select == 2:
        c.add_contact()
    elif select == 3:
        c.del_contact()
    elif select == 4:
        c.find_by_name()
    elif select == 5:
        c.edit_contact()
    elif select == 6:
        c.export_contacts()
    elif select == 7:
        c.import_contacts()
    
    else:
        print('Некорретный ввод')