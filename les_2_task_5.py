my_list = [7, 5, 3, 3, 2]
print(my_list)
elem = float(input('Введите новый элемент рейтинга: '))
if elem > my_list[0]:
    my_list.insert(0, elem)
elif elem < my_list[-1]:
    my_list.append(elem)
elif elem in my_list:
    index = my_list.index(elem) + my_list.count(elem)
    my_list.insert(index, elem)
elif elem < my_list[0] and elem > my_list[-1]:
    for i in my_list:
        if elem > i:
            my_list.insert(my_list.index(i), elem)
            break
print(my_list)
