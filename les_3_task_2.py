def personal_data(name, secondname, year_of_birth, city, email, phone):
    return print(f'Имя: {name}, Фамилия: {secondname}, Год рождения: {year_of_birth},'
                 f' Город проживания: {city}, Email: {email}, Телефон: {phone}.s')


personal_data(name=input('Имя: '), secondname=input('Фамилия: '), year_of_birth=input('Год Рождения: '),
              city=input('Город проживания: '), email=input('email: '), phone=input('phone: '))
