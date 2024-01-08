#
#
# k = int(input('введите значение\n\t'))
# m = int(input('введите значение\n\t'))
# l = int(input('введите значение\n\t'))
#
# print(k*m/l)

#
# print(int(input('введите значение\n'))*int(input('введите значение\n'))/int(input('введите значение\n')))
#
#
# print('my name')
# print('ilona', 'vashkevich', end=' maria ')
# print('i am woman')


# import random
# r = random.randint(100, 999)
# print('Случайное число', r)
# s = str(r)
# print('Сумма числа', int(s[0])+int(s[1])+int(s[2]))

# a = 20
# b = 55
# if a < b:
#     print('a < b')
#     print('hi')
# выведет a<b и hi

# a = 200
# b = 55
# if a < b:
#     print('a < b')
#print('hi')
# выведет hi, тк принт hi написаны с новой строки без табуляции при том что а больше б если бы а было меньше б,
# вывело бы еще и сравнение
#
# else: print('иначе')
# # выведет иначе


# a = 200
# b = 55
# if a < b:
#      print('a < b')
# elif True:
#     print('ELIF')
# else: print('иначе')
# выведет Elif

# a = 200
# b = 55
# c = 20
# if a < b:
#       print('a < b')
# elif c < b:
#      print('ELIF')
# else: print('иначе')


# a = '55'
# b = 'hello'
# if a == '55':
#     print('a равно 55')
# elif b != 'hello':
#     print('б не равно hello')
# else:
#     print('не равно')
# if b != 'hello':
#     print('a равно 55')
# elif b != 'hello world':
#     print('б не равно hello world')

# a = '55'
# b = 10
# c = 'kitty'
# if a != '55':
#     print('a равно 55')
# elif b > 155:
#     print('b = 200')
# else:
#     print('все мимо')
# if c == 'hello':
#     print('kitty')
# else:
#     print('провал')

# pass заглушка для пустой команды

# a = 555
# if a <= 55 or input('Введите значение: ') == 'hello':
#     print('hello')
# else:
#     print('false')


# if 440 <= 55 or 6 > 2 or 'as' == 'as':
#     print('Hello world')
# else:
#     print('hello')
#
# if (440 <= 55 and 6 > 2) or 'as' == 'as':
#     print('Hello world')
# else:
#     print('Иначе')

# a = 77
# if str(input("Введите букву: ")) != 'B' and a > 1 and int(input("Введите число: ")) >= 5:
#     print('Hello world')
# else:
#     print('Иначе')


# a = int(input("Введите число: "))
# if a % 2 == 0:
#     print('число четное')
# else:
#     print('число нечетное')

# if int(input("Введите число: ")) % 2 == 0: print('число четное')
# else:
#     print('число нечетное')


# a = input('Введите значение')
# b = input('Введите значение')
# c = input('Введите значение')
# d = input('Введите значение')
# f = input('Введите значение')
# e = input('Введите значение')
# if not (a > b or (c > d and f > e)):
#     print('hiiii')
# else: print('else')



# a = int(input('Введите номер пальца \n'))
# if a == 1: print('Большой палец')
# elif a == 2: print('Указательный палец')
# elif a == 3: print('Средний палец')
# elif a == 4: print('Безымянный палец')
# elif a == 5: print('Мизинец')
# else: print('Нет соотвествий')

# a = int(input('Введеите первое число:'))
# b = int(input('Введеите второе число:'))
# c = int(input('Введеите третье число:'))
# import random
# r = random.randint(1, 99)
# print('Первое число лотереи', r)
# s = random.randint(1, 99)
# print('Второе число лотереи', s)
# m = random.randint(1, 99)
# print('Третье число лотереи', m)
#
# if a == r and b == s and c == m:
#     print('Вы победили!!!!')
# else:
#     print('Вы проиграли')


# a = int(input('DateBirth\n'))
# b = str(input('MonthBirth\n'))
#
# if (b == 'march' and 31>=a>=21) or (b == 'april' and a <21) :
#     print('Zodiac sign:', 'Aries')
# elif (b == 'april' and 30>=a>=21) or (b == 'may' and a <21) :
#     print('Zodiac sign:', 'Taurus')
# elif (b == 'may' and 31>=a>=21) or (b == 'june' and a <22) :
#     print('Zodiac sign:', 'Gemini')
# elif (b == 'june' and 30>=a>=22) or (b == 'july' and a <23) :
#     print('Zodiac sign:', 'Cancer')
# elif (b == 'july' and 31>=a>=23) or (b == 'august' and a <24) :
#     print('Zodiac sign:', 'Leo')
# elif (b == 'august' and 31>=a>=24) or (b == 'september' and a <24) :
#     print('Zodiac sign:', 'Virgo')
# elif (b == 'september' and 30>=a>=24) or (b == 'october' and a <24) :
#     print('Zodiac sign:', 'Libra')
# elif (b == 'october' and 31>=a>=24) or (b == 'november' and a <23) :
#     print('Zodiac sign:', 'Scorpio')
# elif (b == 'november' and 30>=a>=23) or (b == 'december' and a <2) :
#     print('Zodiac sign:', 'Sagittarius')
# elif (b == 'december' and 31>=a>=22) or (b == 'january' and a <21) :
#     print('Zodiac sign:', 'Capricorn')
# elif (b == 'january' and 31>=a>=21) or (b == 'february' and a <21) :
#     print('Zodiac sign:', 'Aquarius')
# elif (b == 'february' and 29>=a>=21) or (b == 'march' and a <21) :
#     print('Zodiac sign:', 'Pisces')
# else:
#     print('Zodiac sign:', 'no matches')


# 3 занятие 16 ноября

# Zodiak = ['Козерог', 'Водолей', 'Рыбы', 'Овен', 'Телец', 'Близнецы', 'Рак', 'Лев', 'Дева', 'Весы', 'Скорпион', 'Стрелец']
# M = int(input('\n\n А сейчас я угадаю ваш знак зодиака.\n   Введите свой месяц рождения (число от 1 до 12): '))
# D = int(input('   Введите день своего рождения (число от 1 до 31): '))
#
# if M < 1 or M > 12:
#     print(' Введенный месяц не входит в указанный диапазон.')
# elif D < 1 or D > 31:
#     print(' Введенный день не входит в указанный диапазон.')
# else:
#     if D < 19 or (D < 20 and (M == 1 or M == 4)) or (D < 21 and (M == 3 or M == 5)) or (D < 22 and (M == 6 or M == 12)) or (D < 23 and M >= 7 and M <= 11):
#         print(f" Вы  {Zodiak[M - 1]}!")
#     else:
#         print(f" Вы  {Zodiak[M % 12]}!")

# count_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
# while (date := input("Введите: (день.месяц): ")):
#     try:
#         day, month = map(int, str.split(date, ".", 1))
#         if (1 <= month <= 12 and 1 <= day <= count_day[month - 1]):
#             days = day + sum(count_day[:month - 1]) - 20
#             if days <= 0:
#                 print("Козерог")
#             elif days <= 29:
#                 print("Водолей")
#             elif days <= 59:
#                 print("Рыбы")
#             elif days <= 89:
#                 print("Овен")
#             elif days <= 120:
#                 print("Телец")
#             elif days <= 152:
#                 print("Близнецы")
#             elif days <= 183:
#                 print("Рак")
#             elif days <= 214:
#                 print("Лев")
#             elif days <= 245:
#                 print("Дева")
#             elif days <= 275:
#                 print("Весы")
#             elif days <= 306:
#                 print("Скорпион")
#             elif days <= 335:
#                 print("Стрелец")
#             else:
#                 print("Козерог")
#         else:
#             print("Некорректная дата!")
#     except ValueError:
#         print("Введите корректную дату рождения!")


# import random
#
# rnd = random.randint(1, 10)
# inp = int(input('Введите число: '))
# if rnd == inp:
#     print("Вы угадали число!")
# else: print(f"Вы не угадали!\nЧисло было: {rnd}")
# #вызов функциональной строки (переменную указываем в фигурных скобках {})
#
# else:print("Вы не угадали!\nЧисло было:, rnd")


# l = '33|'
# print(l*3)
#
# l = '33|'
# print(len(l*3))
#
# print(f"Длина строки составила: {len(input('Введите строку '))}")

#print("asfdghn\"asfghj") #экранирование


# b = input('Как тебя зовут?\n')
# print('Привет, ' + b)
# print(b*3)

# hw = 'hello w orld'
# print(hw.split(" "))
# print(hw.split(" ", 1)) #разделяем строку на список по пробелу один раз

# hw = '8'
# print(hw.isalpha()) #проверяем состоит ли строка только из букв

# print(hw.isdigit()) #проверяем является ли строка числовой

# hw = 'hello world'
# print(hw.replace('l', 'a', 1)) #заменяем в строке hw символ l на символ а 1 раз
# print(hw.replace('ll', 'a')) #заменяем в строке hw подстроку ll на символ а
#print(hw.replace('ll', hw)) #заменяем в строке hw подстроку ll на строку hw

# hw = 'hello'
# print(hw[2:]) #выводим строку начиная со второго индекса и до конца

# hw = 'helloит'
# print(hw[0::2]) #выводим строку пропуская каждый второй


# n = 'kitty'
# print(n[::3])
# print(n.upper())
# print(n[::-1])

# n = input('Введите слово с разными регистрами: ')
# print(n.swapcase())
# print(n.swapcase()*2)


# n = 'burlesque'
# print(n[2])
# print(n[-2])
# print(n[0:5])
# print(n[:-2])
# print(n[0::2])
# print(n[1::2])
# print(n[::-1])
# print(n[::-2])
# print(len(n))


#Занятие №4 20 ноября

# for i in range(int(input())): print(i) #выведет 7 строк с нумерацией 0-5

# spisok = [1, 4, 'fjhg', 'hdfg', 5, 67]
# for i in spisok: print(i) #при задании списка ссылаемся на список

# spisok = [1, 4, 'fjhg', 'hdfg', 5, 67]
# for i in spisok: print(f'Элемент №{spisok.index(i)} ' + str(i))

# arr = [1, 3, 6, 'sf', 'asg', True]
# for i in arr:
#     print('jojo'+str(i))


# arr = [1, 3, 6, 'sf', 'asg', True]
# for index in range(len(arr)):
#     print(f'Номер элемента: {index+1} Значение: {arr[index]}')

# arr = [1, 3, 6, 'sf', 'asg', True]
# for index, value in enumerate(arr):
#     print(f'Номер элемента: {index+1} Значение: {value}')
#     break
# else:
#     print('Цикл завершил совю работу нормально')

# for index, value in enumerate('arr'):
#     print(f'Номер элемента: {index+1} Значение: {value}')
# else:
#     print('Цикл завершил совю работу нормально')


# arr = [1, 3, 6, 'sf', 'asg', True]
# for i, v in enumerate(arr):
#     print(f'Номер элемента: {i}')
#     if i == 3: continue
#     print(f'Значение: {v}')
# else:
#     print('Цикл завершил свою работу нормально!')

# arr = [1, 3, 6, 'sf', 'asg', True]
# for i, v in enumerate(arr):
#     print(f'Номер элемента: {i}')
#     if i == 2: continue
#     if i == 3: continue
#     print(f'Значение: {v}')
# else:
#     print('Цикл завершил свою работу нормально!')

# arr = [1, 3, 6, 'sf', 'asg', True, 22]
# for i, v in enumerate(arr):
#     print(f'Номер элемента: {i}')
#     if i > 3: continue
#     print(f'Значение: {v}')


# while True:
#     print('erfg')
#     break


# i = 0
# while i < 10:
#     i += 1
#     print(i)
#     if i == 5: break
# else: print('Hi')


# spisok = [3, 67, 7, 5, 10]
# summ = 0
# pr = 1
# for i in spisok:
#     summ += i
#     pr *= i
# print('сумма', summ)
# print('произведение', pr)
# print(sum(spisok))


# letters = input('Введите строку: ')
# clean_string = ''
# for letter in letters:
#     if letter.islower():
#         clean_string += letter
# print(clean_string)

# import random
# x1 = random.randint(1,10)
# y1 = random.choice(['красное', 'черное'])
# i=1
# while i < 6:
#     x = int(input('Введите число: '))
#     y = (input('Введите цвет (красное/черное): '))
#     if x==x1 and y==y1:
#         print('\n\tВы выйграли в казино')
#         break
#     elif i < 5: print('\t\nПопробуйте снова')
#     i+=1
# else: print('\t\nВы проиграли','\t\nВыйгрышная комбинация: ', x1, y1)




