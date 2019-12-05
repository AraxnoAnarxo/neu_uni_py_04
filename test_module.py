from main import name_n


def test_function_name_n():

    # тест 1 - подается одноэлементный список
    n_list = ['Sarah']
    list_out = name_n(n_list, 2)  # ('Sarah', 'Sarah')
    if list_out == ['Sarah', 'Sarah']:
        print('Test 1 is OK')
    else:
        print('Test 1 is failed')

    #тест 2 - если на вход подается число
    n_list = [0]
    list_out = name_n(n_list, 2) # [0, 0]
    if list_out == [0, 0]:
        print('Test 2 is OK')
    else:
        print('Test 2 is failed')


test_function_name_n()


