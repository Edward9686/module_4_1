def divide(first, second):
    try:
        result = first / second
    except ZeroDivisionError:
        print('Ошибка')
    else:
        print(result)
