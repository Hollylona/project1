# ЗАНЯТИЕ 6

# sa = 'asfghj'
# arr = list(sa)
# print(arr)
# arr += arr #копируем список
# print(arr)

# arr = {False: 'hello', True: 'world'} #создаем словарь
# print(arr[int(input('Введите число: ')) > 66]) #получаем значение словаря по ключу-условию
# print(arr[False]) #получаем значение словаря по ключу False

# a = int(input('Введеите число: '))
# b = int(input('Введеите число: '))
# d = {True: a, False: b}
# if a > b:
#     print('Больше: ', d[True])
# elif b>a:
#     print('Больше: ', d[False])

# arr = {True: 'Первое число больше второго', False: 'Второе число больше первого'} #создаем словарь
# n1 = int(input('Введите число 1: '))
# n2 = int(input('Введите число 2: '))
# if n1 != n2: print(arr[n1>n2]) #получаем значение словаря по ключу-условию

# dd = {'fg': 22}
# dd[90] = '90' #добавляем новую пару в словарь
# print(dd)
# dd[90] = 'vc' #меняем значение у ключа 90
# print(dd)

# dd = dict.fromkeys([1,3, 'huiluh', 999], 'koko') #создаем словарь с помощью fromkeys
# print(dd)

# import random
# dd = {b+1: random.randint(1, 10) for b in range(6)} #создаем словарь с помощью генератора
# print(dd)

# import random
# a = ['hf', 'jfj', 'jffiyg', 'gyj']
# dd = {random.choice(a): random.randint(1, 100) for i in range(5)}
# print(dd)


# for key, value in dd.items(): #проходимся циклом по словарю
#     print(key, value)

# for k, i in enumerate(dd.values()): print(k, i)


# import random
# words = ['asd', 'gf', 'dgf', 'wer']
# dd = {random.choice(words): random.randint(0, 10) for b in range(4)} #создаем словарь с помощью генератора
# print(dd)
# print(dd.pop('gf')) #удаляем пару и возвращаем значение удаляемого ключа
# print(dd)


# d = {1:2, "dfg": 'sfd'}
# print(d)
# del d[1] #удаляем пару по ключу
# print(d)


# d = {1:2, ("dfg", 44): ['sfd', 32, 'sf']}

# d = {11:2, ("dfg", 44): ['sfd', 32, 'sf']}
# print(d)
# if 1 in d: print("ключ 1 найден")
# if ("dfg", 44) in d: print("ключ-кортеж найден")

# d = dict(zip([1,2, 'momo', 'mo'], ["odin", 'dwa', 'momo']))
# #создаем словарь с помощью встроенной функции zip
# print(d)

# ll = [1,23,5,5, 'f', 'f']
# print(ll)
# ll = list(set(ll))
# #преобразуем список в множество, а затем обратно в список, чтоб удалить повторяющиеся элементы
# print(ll)


# s = {1,2,3,5}
# print(s)
# s.add('dfghj') #добавляем элемент в множество
# print(s)
# s.remove(5) #удаляем элемент из множества по значению
# #в случае не нахождения удаляемого элемента ошибкa будет
# s.discard(50) #удаляем элемент из множества по значению
# #в случае не нахождения удаляемого элемента ошибки не будет
# print(s)

# s = {1,2,3,5}
# print(s)
# if 5 in s: print("5 было найдено!") #проверяем, есть ли число 5 в нашем множестве


# s = {"mo", 'as', 'asfd'}
# print(s)
# print(f"была удалена строка {s.pop()}")
# print(s)

# s = {"mo", 'as', 'asfd'}
# print(s)
# s.clear() #очищаем множество
# print(s)


# s1 = {"mo", 'as', 'asfd'}
# s2 = {"mok", 'mas', 'as'}
# print(s1, s2, sep='\n')
# s3 = s1.union(s2) #объединяем множества
# print(s3)

# s3 = s1 | s2 #объединяем множества

# s3 = s1 | s2 | {55,32} #объединяем множества

# s1 = {"mo", 'as', 'asfd'}
# s2 = {"mok", 'mas', 'as'}
# print(s1, s2, sep='\n')
# s3 = s1 & s2 & {55,32, 'as'} #пересечение множеств

# s1 = {"mo", 'as', 'asfd'}
# s2 = frozenset({"mok", 'mas', 'as'})
# s3 = s1|s2
# print(s1)
# print(s2)
# print(s1|s2)
# print(s1&s2)

#Домашнее задание

#import random
# s1 = set(random.randint(1, 100) for b in range(10))
# print(s1)
# s2 = set(int(input('Введите число в диапозоне от 1 до 100: ')) for i in range(10))
# s3 = s1&s2
# print(s3)
# values = (list(s3))
# key = []
# for i in range(len(values)):
#     key.append(i)
# dd = dict(zip(key, values))
# print('Словарь: ', dd)


# k = print
# print = 'k'
# k(print)

#Задача 1

# import random
# s1 = list(random.randint(1, 10) for b in range(3))

#Задача 2

# s = ['hi', 'bye', 'good']
# s1 = list(''.join(s))
# st = input('Введите строку: ')
# l= []
# for i in s1:
#     if i in st:
#         l.append(i)
# print('Все элементы есть') if len(s1) == len(l) else print('Нет полного совпадения')

#Задача 3

# l = []
# i=0
# while i<5:
#     b = input('Введите значение: ')
#     l.append(b)
#     i+=1
# print(l)
# l.sort(key=len)
# print(l)












