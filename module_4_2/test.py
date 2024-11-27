def test_function():
    def inner_function ():
        print("Я в области видимости функции test_function")
    inner_function()


test_function()

# Ошибка, т.к. inner_function является локальной  и действует исключительно в пределах
# функции test_function()
#inner_function()


