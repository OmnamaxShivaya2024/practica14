def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return len(string) , string.upper(),
    string.lower()

def  is_contains(string ,list_search):
    count_calls()
    list_search=[a. lower() for a in list_search]
    if string.lower() in list_search:
        return True
    else:
        return False

calls=0

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)


