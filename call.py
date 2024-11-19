calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return len(string),string.upper(),string.lower()


# def is_contains(string, list_to_search):
#     count_calls()
#     return string.lower() in [item.lower() for item in list_to_search]
def is_contains(list_to_search, string):
    count_calls()
    contains = False
    for i in range(len(string)):
        if list_to_search.lower() in string[i].lower():
            contains = True
            break
    return contains

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

