calls = 0
def count_calls(*args):
    global calls
    calls += 1
def string_info(string):
    my_tuple = (len(string), string.upper(), string.lower())
    global count_calls
    count_calls(1)
    return my_tuple

def is_contains(string, list_to_search):
    string_lower = string.lower()
    list_to_search1 = [x.lower()for x in list_to_search]
    flag = False
    if string_lower in list_to_search1:
        flag = True
    count_calls(1)
    return flag
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)