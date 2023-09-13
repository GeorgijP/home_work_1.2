#task_1
f_temperature = int(input("Введите темературу по фаренгейту: "))

c_temperature = (f_temperature - 32) * 5/9

print(c_temperature)


# #task_2
one_dollar = 70.38 #rub
one_hundred_rub = 1.22 #eur

dollars = int(input("Введите сумму долларов: "))

rub = dollars * one_dollar
eur = rub/100 * one_hundred_rub

print(eur)


#task_3
answer = str(input("Какая сегодня погода? "))



#task_4
total_amount = 0
index = 0

while index < 12:
    summ = int(input("Сколько вы отложили в этом месяце? "))
    total_amount += summ
    index += 1

print(total_amount)


#task_5
correct_answers = 0

while correct_answers == 0:

    print('Привет! Предлагаю проверить свои знания английского! Набери "ready", чтобы начать!')
    activation = str(input(""))

    if activation == "ready":
        print("My name ___ Vova")
        one_answer = str(input())
        if one_answer == "is":
            correct_answers += 1
            print("Ответ верный!")
        else:
            print("Неправильно. Правильный ответ: is")

        print("I ___ a coder")
        two_answer = str(input())
        if two_answer == "am":
            correct_answers += 1
            print("Ответ верный!")
        else:
            print("Неправильно. Правильный ответ: am")

        print("I live ___ Moscow")
        three_answer = str(input())
        if three_answer == "in":
            correct_answers += 1
            print("Ответ верный!")
        else:
            print("Неправильно. Правильный ответ: in")

        print(f"Вот и всё! Вы ответили на {correct_answers} вопросов из 3 верно, это {correct_answers/0.03} процентов")

