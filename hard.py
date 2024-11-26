def calculate_structure_sum(data,*args):
    total_sum = 0

    if isinstance(data, int):
        total_sum = total_sum + data
    elif isinstance(data, str):
        total_sum = total_sum + len(data)
    elif isinstance(data, (list, tuple, set,*args)):
        for i in data:
            total_sum += calculate_structure_sum(i)
    elif isinstance(data, dict):
        for key, value in data.items():
            total_sum += calculate_structure_sum(key)
            total_sum += calculate_structure_sum(value)
    return total_sum


data_structure = [

    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)

data_structure = [[1, 2, 3],
                  {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'drum': 8}),
                  "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]
summ = 0
def calculate_structure_sum(data_structure):
    global summ

    for current_element in data_structure:
        if isinstance(current_element, int):
            summ = summ + current_element
        elif isinstance(current_element, str):
            summ = summ + len(current_element)
        elif isinstance(current_element, dict):
             dict_to_list = []
             for key, value in current_element.items():
                 dict_to_list.append(key)
                 dict_to_list.append(value)
             calculate_structure_sum(dict_to_list)

        else:
            calculate_structure_sum(current_element)
    return(summ)

result = calculate_structure_sum(data_structure)
print(result)
#
# def calculate_nested_sum(*args):
#     total_sum = 0
#
#     for arg in args:
#         if isinstance(arg, (list, tuple, set)):
#             total_sum += calculate_nested_sum(*arg)
#         elif isinstance(arg, dict):
#             total_sum += calculate_nested_sum(*arg.items())
#         elif isinstance(arg, str):
#             total_sum += len(arg)
#         elif isinstance(arg, (int, float)):
#             total_sum += arg
#         elif arg is None:
#             pass
#         # Не обязательно, ещё не проходили исключения
#         # raise TypeError("Неизвестный тип данных: {}".format(type(arg)))
#
#     return total_sum
#
#
# print(calculate_nested_sum(nested_data))