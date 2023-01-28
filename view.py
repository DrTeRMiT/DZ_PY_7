import model

def list_all(list_to_display = model.contacts):
    for i in list_to_display:
        print(f'Имя: {i["name"]}, \tтел: {i["phone"]}')


# запрос записи
def get_contact(mode):
    name = get_name()
    phone = input('Введите телефон -> ')
    print(mode)
    print(f'Имя: {name}, \tтел: {phone}')
    return (name, phone)


# вывод результата удаления
def success(yes):
    if yes == 0:
        print('...неуспешно')
    else:
        print('...успешно')
    return


# запрос имени
def get_name():
    name = input('Введите имя -> ')
    return name


# запрос имени файла и режима выгрузки
def get_export_format():
    filename = input('Введите имя файла -> ')
    type = input('Введите тип csv, txt или json -> ')
    return (filename,type)


# запрос имени файла для импорта
def get_import_filename():
    filename = input('Введите имя файла -> ')
    mode = input('0 - очистить справочник, 1 - добавить -> ')
    return (filename,mode)