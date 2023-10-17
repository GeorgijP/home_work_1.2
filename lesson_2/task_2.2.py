user_points = 0
right_answers = 0

user_name = str(input('Привет! Предлагаю проверить свои знания английского!\nРасскажи, как тебя зовут!\n'))

print(f'Привет, {user_name}, начинаем тренировку!')

print('Вопрос: My name ___ Vova')
user_response_1 = str(input('Введите ответ: '))
if user_response_1 == 'is':
    user_points += 10
    right_answers += 1
    print('Ответ верный!\nВы получаете 10 баллов!')
else:
    print('Неправильно.\nПравильный ответ: is')

print('Вопрос: I ___ a coder')
user_response_2 = str(input('Введите ответ: '))
if user_response_2 == 'an':
    user_points += 10
    right_answers += 1
    print('Ответ верный!\nВы получаете 10 баллов!')
else:
    print('Неправильно.\nПравильный ответ: am')

print('Вопрос: I live ___ Moscow')
user_response_3 = str(input('Введите ответ: '))
if user_response_3 == 'in':
    user_points += 10
    right_answers += 1
    print('Ответ верный!\nВы получаете 10 баллов!')
else:
    print('Неправильно.\nПравильный ответ: in')


score = right_answers // (3 / 100)

print(f'Вот и все, {user_name}!\n'
      f'Вы ответили на {right_answers} вопросов из 3 верно.\n'
      f'Вы заработали {user_points} баллов.\n'
      f'Это {score} процентов.')
