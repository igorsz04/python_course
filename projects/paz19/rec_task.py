# napisac funkcję która z tablicy wybierze wszystkie liczby calkowite, ktore:
# nie sa zerem, nie zawieraja zera z przodu, zawieraja tylko liczby, .... 0 12, 12 0 12. 12, 2a

tab = ['0 12', '12 0', '12.', '12', '2a', '15', '12.45']


def get_numbers(numbers_list):
    valid_number = []
    invalid_number = []
    for x in numbers_list:
        try:
            valid_number.append(int(x))
        #            invalid_number.append(numbers_list.difference(valid_number))
        except ValueError:
            invalid_number.append(x)
    return valid_number, invalid_number


print('get_numbers(tab):')
print(get_numbers(tab))


# napisac funkcje zwracajaca liczby calkowite w list comprehension
def is_int(number):
    try:
        int(number)
        return True
    except ValueError:
        pass


list_comp = [int(number) for number in tab if is_int(number) and int(number) < 13]
print('list_comp:\n',list_comp)

integers = get_numbers(tab)
print('x for x in integers:\n',[x for x in list_comp if x<13])
#print([x if x < 13 else None for x in integers])

print([x for x in range(10)])

print('\nnapisac funckje zwracajaca liczby calkowite w list comprehension:')
list_comp2 = [number for number in tab if is_int(number)]
print(list_comp2)



print('\nzadanko:')
tab = [1, 2, 4, 15, 210, 1000, 10, '10', '13.']
list_comp = [int(number) for number in tab if is_int(number) and int(number) <200]
print(list_comp)






print("\nzadanie abcdedfghij:")
# [A B C    D E F G    H I J]
# [A B C    D E F G    H I J]
# [A B C    D E F G    H I J]
# [A B C    D E F G    H I J]
# [A B C    D E F G    H I J]
# [A B C    D E F G    H I J]