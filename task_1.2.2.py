# task_1
washing_time = 0

print("Выберите режим стирки: обычный / экспресс/ хлопок.")
washing_mode = str(input())

print("отжим: вкл/выкл?")
spin_mode = str(input())

print("полоскание: вкл/выкл?")
rinse_mode = str(input())

if washing_mode == "обычный":
    washing_time += 90
elif washing_mode == "экспресс":
    washing_time += 20
elif washing_mode == "хлопок":
    washing_time += 20
else:
    print("Не корректный режим")

if spin_mode == "выкл":
    washing_time -= 10

if rinse_mode == "вкл":
    washing_time += 10

print(f"время стирки займет {washing_time} минут")

# task_2
today = int(input("Какое сегодня число? "))

if today < 10:
    print(f'{10 - today} до зарплаты.')
elif today == 10 or today == 25:
    print('Зарплата сегодня.')
elif today > 10 and today < 25:
    print(f'{25 - today} до зарплаты.')
elif today > 25 and today <= 30:
    print(f'{30 - today + 10} до зарплаты.')
else:
    print('Данные не коректны.')

# task_3
salary = int(input('Введите вашу зарплату: '))

nomber_of_books = int(input('Сколько книг вы продали? '))

if nomber_of_books < 1000:
    print('Ваш размер бонуса 0%, это 0 Р.')
elif nomber_of_books >= 1000 and nomber_of_books < 1500:
    print(f'Ваш размер бонуса 10%, это {salary * 0.1} Р.')
elif nomber_of_books >= 1500 and nomber_of_books < 2000:
    print(f'Ваш размер бонуса 15%, это {salary * 0.15} Р.')
elif nomber_of_books >= 2000:
    print(f'Ваш размер бонуса 20%, это {salary * 0.2} Р.')
else:
    print('Данные не коректны.')
