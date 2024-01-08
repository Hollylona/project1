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

#Занятие 5 23 ноября

# arr = [] #создали пустой список
# arr2 = list() #создали пустой список
#
# arr = [2 for i in range(7)]
# print(arr)

# import random
# arr = [random.uniform(1, 5) for i in range(7)]
# #создаем список и сразу заполняем его случайными дробными числами
# print(arr)

# import random
# arr = ['Hi', '567', 'Well', 'get', '78645', 'way', '76453', 'mama', 'car', 'cat']
# arr2 = [random.choice(arr) for i in range(5)]
# print(arr2)
#
# arr.append(7465) #добавили элемент в список
# arr.insert(0, 456) #добавили элемент в начало списка
# print(arr)

# rr = ['Hi', '567', 'Well', 'get', '78645', 'way']
# rr.remove('Hi')
# print(rr)

# arr = ['rt', 'adsg', 'rt', 'asdf', 'adsg', 'adsg', 'fg', 'adsg']
# print(arr)
# for i in arr.copy(): #копирует список и потом по нему проверяет
#     print('Проверяемый элемент: '+i)
#     if i == 'adsg': arr.remove(i)
# print(arr)

# arr = ['rt', 'adsg', 'rt', 'asdf']
# arr2 = arr #копируем ссылку списка, т.е. создаем зависимую копию
# arr2 = arr.copy() #копируем список, т.е. создаем независимую копию списка
# print(arr2)
# arr2.remove('rt')
# print(arr)

# arr = ['rt', 'adsg', 'rt', 'asdf']
# print(arr)
# del arr[2]
# print(arr)


# arr = ['rt', 'adsg',['mo',[[['ko']],77, 88]], 'rt', 'asdf']
# #создаем вложенный список (список со списками)
# print(arr)
# print(arr[2][1][0][0][0])
# #выводим значение первого элемента самого последнего по вложенности списка

# arr = ['rt',(4,[(2,1), (2,33)],4,2), 'adsg',['mo',[[['ko']],77, 88]], 'rt', 'asdf']
# #создаем вложенный список со списками и кортежами
# print(arr)
# print(arr[1][1][1][1])

# arr = ['rt',(4,[(2,1), (2,33)],4,2), 'adsg',['mo',[[['ko']],77, 88]], 'rt', 'asdf']
# #создаем вложенный список со списками и кортежами
# print(arr)
# for i in arr:
#     if type(i) == tuple or type(i) == list:
#         for j in i:
#             if type(j) == tuple or type(j) == list:
#                 for k in j:
#                     if type(k) == tuple or type(k) == list:
#                         for m in k: print(m)
#                     else:
#                         print(k)
#             else:
#                 print(j)
#     else: print(i)

# arr = [1,2,[3], 'hi']
# if [3] in arr: print('список с тройкой находиться в нашем списке')
# else:print('список с тройкой не находиться в нашем списке')


# arr = [1,2,[3], 'hi']
# arr2 = [7,8]
# arr3 = [47, 87, 13]
# print(arr+arr2) #соединяем списки и выводим результат в консоль
# print(arr+arr2+arr3)
# arr.extend(arr2) #дополняем список arr списком arr2
# arr.extend(arr3)
# print(arr)
#
# arr = ['a', 'sad', 'aaa', 'sadgf', 'b', 'df']
# arr.sort() #сортируем список по алфавиту
# arr.sort(key=len) #сортируем список по длине строк
# print(arr)


# tup = (1,6,5,4,'df') #создаем кортеж
# print(tup)
# tup = list(tup) #преобразуем кортеж в список
# tup.reverse() #переворачиваем список
# tup = tuple(tup) #преобразуем список в кортеж
# print(tup)

# tup = (1,6,5,4, [2,3,5, 'fg'],'df') #создаем кортеж
# print(tup)
# tup[4].insert(0, 'hello world') #изменяем список внутри кортежа
# print(tup[4])
# print(tup)

# tup = tuple([1 for i in range(5)])
#создаем список с помощью генератора и потом делаем из него кортеж

# import random
# tup = tuple([random.randint(1, 10) for i in range(5)])
# #создаем список с помощью генератора и потом делаем из него кортеж
# print(tup)
# print(f'Минимальный элемент в кортеже tup: {min(tup)}\nМаксимальный элемент в кортеже tup: {max(tup)}')
# print(sum(tup))

# import random
# tup = tuple([random.randint(0, 5) for i in range(10)])
# tup2 = tuple([random.randint(-5, 0) for i in range(10)])
# tup3 = tup+tup2
# print(tup)
# print(tup2)
# print(tup3)
# print(tup3.count(0))

# print(list(range(20))) #создаем список на основе range

# Задание 1
# s = 'Hello Ilona How are you'
# print(s)
# t = tuple(s.split(' '))
# print('Самое длинное слово в строке:', max(t, key=len))

#Задание 2
# s = 'Hello, Ilona. How are you?'
# s1 = s.replace(',', '')
# s2 = s1.replace('.', '')
# s3 = s2.replace('?', '')
#
# l = s3.split(' ')
# t = tuple(l)
# print(t)



# Задача №1
# arr = [15,48,'hello',6,19,'world']
# sch = 0
# for i in arr:
#     if type(i) is int:
#         if i%2==0:
#             for z in str(i):
#                 sch += int(z)
#             print(i, 'Summa', sch)
#             sch = 0
#         else:
#             ind = arr.index(i)
#             arr[ind] = 1
# print(arr)


