
user_list = input('Введите некоторое количество целых чисел через пробел: ').split()
for i in range(len(user_list)):
    user_list[i] = int(user_list[i])
print(user_list)

n = 0
for i in range(len(user_list)//2):
    user_list[n], user_list[n+1] = user_list[n+1], user_list[n]
    n += 2
print(user_list)