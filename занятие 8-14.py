# Занятие 8

# import random
# s = 'jdhfg'
# l = list(random.randint(1, 10) for b in range(3))
# k = (1,'fhfk', 903)
# sl = dict(zip(l, k))
# m = set(i for i in range(5))
# fs = {a for a in range(5)}
# print(s)
# print(l)
# print(k)
# print(sl)
# print(m)
# print(fs)


# t = type
# def type(s):print(t(s))
# type('dsfg')


# Домашнее задание

# import random
# l = list(random.randint(1, 100) for b in range(10))
# s = set()
# i = 0
# while i < len(l):
#     if l[i]%2==0:
#         s.add(l[i])
#     i +=1
# s1 = frozenset(s)
# dd = {s1: l}
# print('Словарь: ', dd)


# Занятие 9 (7 декабря)

# i, f, d= [1,2, 5] #создаем переменные и даем им значения из коллекции
# print(i, f, d)
# k = m = 'hi' #создаем две переменные с одинаковым значением
# print(k, m)


# import sys
#
# print('dtgjh')
# sys.exit(0) #завершаем выполнение программы с кодом 0
# print(4/0)


# try:
#     print(khlhl)
# except:
#     print('произошла ошибка')
# print("hi")
#
# try:
#     print(3/0)
#     print('iojipo')
# except:
#     print('Произошла ошибка')
# print('hello world')

# try: print(3/0)
# except: pass
# print('hello world')


# try:
#     #print(3/0)
#     int('dfsgh')
# except ZeroDivisionError as err:
#     print(err)
# except ValueError as err:
#     print('VALUE ERROR')

#
# try:
#     #print(3/0)
#     input()
# except: #отлавливает абсолютно все исключения
#     print('ошибка поймана')


# j = int(input("Введите число: "))
# if j == 5:
#     print('Мне не нравится число 5, поэтому ошибка: ')
#     raise Exception


# j = int(input("Введите число: "))
# i = int(input("Введите число: "))
# if j+i < 15:
#     print('сумма меньше 15, поэтому ошибка: ')
#     raise ValueError
# elif i+j>30:
#     print('сумма больше 30, поэтому ошибка')
#     raise ZeroDivisionError('na 0 delit nelzia')

#
# try:
#     print(1/0)
#     int('afd')
# except (ValueError, ZeroDivisionError) as err: #отлавливаем два разных исключения
#     print(err)

# s = (ValueError, ZeroDivisionError)
# print(type(s))
# try:
#     print(1/0)
#     int('afd')
# except s as err: #отлавливаем два разных исключения из переменной-кортежа
#     print(err)


# s = (ValueError, ZeroDivisionError)
# print(type(s))
# try:
#     #print(1/0)
#     int('afd')
#     print('TRY')
# except s as err: #отлавливаем два разных исключения из переменной-кортежа
#     print(err)
# else:
#     print('Ошибок не было')
# finally:
#     print("saf")


# j = int(input("Введите число: "))
# i = int(input("Введите число: "))
# try:
#     d = j/i
# except ZeroDivisionError:
#     print('ошибка')
# else:
#     print(d**2)
# finally:
#     print("программа выполнена")


# try: input()
# except KeyboardInterrupt:
#     print('стоп программы')


# while True:
#     try:
#         a = int(input("Введите первое число: "))
#         b = int(input("Введите второе число: "))
#         print(a / b)
#         break
#     except ZeroDivisionError as err:
#         print('Ошибка, деление на ноль недопустимо, введите корректное число :')
#     except ValueError as err:
#         print('Буквы не допускаются, введите число :')


# Занятие 10 (11 декабря)

# f = open('Ilona.py', encoding='utf-8')
# print(f.readlines())
#
# f = open('hihi.txt', 'a+', encoding='utf-8') #открываем файл в режиме дозаписывания и ставим кодировку utf-8
# for i in range(5):
#     f.write(f'Hello world number {i+1}\n') #записываем в файл строки с помощью цикла
# f.close() #закрываем файл


# f = open('hihi.txt', 'a+', encoding='utf-8') #открываем файл в режиме дозаписывания и ставим кодировку utf-8
# for i in range(3):
#     f.write(input('введите стоку:\n'))
# f.close() #закрываем файл
#
# f = open('hihi1.py', 'w', encoding='utf-8') #открываем файл в режиме дозаписывания и ставим кодировку utf-8
# for i in range(3):
#     f.write("input('введите стоку:')\n")
# f.close() #закрываем файл
#
# f = open('hihi.py', 'w', encoding='utf-8') #открываем файл в режиме перезаписи и ставим кодировку utf-8
# s1 = input('Введите значение: ')
# s2 = input('Введите значение: ')
# f.write(f"""print(f'Значение 1: {s1}\\nЗначение 2: {s2}')""") #записываем в файл строки
# f.close() #закрываем файл


# f = open('img.jpg', 'rb+') #открываем файл в режиме бинарного чтения
# f2 = open('new_img.jpg', 'wb+') #открываем файл в режиме бинарной перезаписи
# f2.write(f.read()) #записываем в файл содержимое из переменной f
# f.close() #закрываем файлы
# f2.close()


# import os


# os.rename('hihi.txt', 'hihi') #переименовываем файл
# print(os.getcwd()) #выводим путь до текущего файла
# os.mkdir('KOMO') #создаем пустую папку
# os.chdir('KOMO') #переходим в папку KOMO

# print(os.getcwd()) #выводим текущий путь
# os.makedirs('kфывodf/ko/ko') #создаем несколько вложенных папок
# os.remove('img2.jpg') #удаляем файл
# os.removedirs('KOMO/ko/ko/ko') удаляем несколько пустых папок, которые вложенны друг в друга
# os.rmdir('MO') удаляем пустую папку


# f = open('hihi.txt', 'w', encoding='utf-8')
# f.write('45 34564 233 33 3_32 4_432 sdfg v3 32')
# f.close()
#
# f = open('hihi.txt')
# s = f.read()
# s = s.replace("_", " ").split(' ')
# print(s)
# summ = 0
# for i in s:
#     if i.isdigit(): summ += int(i)
#     else:
#         for j in i:
#             if j.isdigit(): summ+=int(j)
# f2 = open('hihi1.txt', 'w')
# f2.write(str(summ))

# import os
# import time
# l = [1305, 'yo', 'love', 'cat', 59, 312, 'workspace']
# a = []
# b = []
# for i in l:
#     if type(i) is int:
#         a.append(i)
#     elif type(i) is str:
#         b.append(i)
# a.sort()
# b.sort(key=len)
# c = b + a
# print(a)
# print(b)
# print(c)
# f = open('hihi1.txt', 'w')
# f.write(str(c))
# f.close()
# os.mkdir(str(b[-1]))
# time.sleep(10)
# os.rmdir(str(b[-1]))


# Занятие 11 (14 декабря)

# with open('msg.txt', 'r', encoding='utf-8') as f:
#     print(f.read())


# import os
# os.system('test.py') #запускаем другой пайтон-файл

# def sayHi(m): print('Hi', m) #функция, которая принимает один параметр и выводит Hi и этот параметр
# def sayHi2(): pass #пустая функция
#
# sayHi('gvjhkl')

# def sayHi(m): print('Vashkevich', m)
#
# sayHi('Ilona')

# def sayHi(m, p, v):
#     print(f"m = {m}, p = {p}, v = {v}")
#
#
# sayHi(v='gvjhkl', m=5, p=6)


# def sayHi(m, p=4):
#     print(f"m = {m}, p = {p}")
#
#
# sayHi(m='gvjhkl')


# def kguyhkghkk(*args, **kwargs): #функция, которая принимает неогранниченное количество
#     #именованных параметров и ключевых
#     print(args,kwargs)
#
#
#
# kguyhkghkk(55, 'df',8998, 'kokl', s = 'gvjhkl',k9lklmkl = 5)


# k = 7
# def hoho(*args, **kwargs):
#     global k, ko, mo #помечаем переменные которые будут являтся глобальными
#     k = 'kkkk'
#     ko = 99
#     mo = 'kguhy'
#
# hoho()
# print(k, mo)


# k = 7
# def hoho(*args, **kwargs): #создаем функцию с вложенными функциями
#     def jo1():
#         print('JO1')
#         def jo2():
#             print('JO2')
#             def jo3():
#                 print('JO3')
#             jo3()
#         jo2()
#     jo1()
#
# hoho()


# def hoho(a):
#     if (a):
#         return 9
#     print('iuilku')
#     return 'Непонятная строка была выведена и значение парамтера a оказалось false'
#
#
# print(hoho(False))


# m = int(input('Введите номер месяца: '))
# def season(m):
#     if m ==12 or m==1 or m==2:
#         print("winter")
#     elif m==3 or m==4 or m==5:
#         print("spring")
#     elif m==6 or m==7 or m==8:
#         print("summer")
#     elif m==9 or m==10 or m==11:
#         print('autumn')
#     else: print("error")
# (season(m))
#
# month = int(input('Введите месяц от 1 до 12: '))
# def season(month):
#     ssn = ("Зима","Весна","Лето","Осень")
#     if 0 < month < 3 or month == 12: return(ssn[0])
#     if 3 <= month < 6: return(ssn[1])
#     if 6 <= month < 9: return(ssn[2])
#     if 9 <= month < 12: return(ssn[3])
#
# print(season(month))


# a = int(input('Введите число: '))
# b = int(input('Введите число: '))
# def f(a,b):
#     def fu(a: int, b: int):
#         print('Вывод чисел:', a, b)
#     fu(a,b)
# f(a,b)

# def season():
#     global b
#     def b(): print('lklkkl')
#
#
# season()
# b()

# import time
# def s(x, y):
#     for i in range(x, y+1):
#         print(i)
#         time.sleep(1)
# s(1,6)


# Занятие 12 (18 декабря)


# with open("s.txt", "w+", encoding="utf-8") as f:
#     f.write("Hello world!\nIt's me\nGlad to see you")
# with open("s.txt", encoding="utf-8") as f:
#     strr = f.readline()
# def prodstr(a: int, b="Изменение глобальной переменной:"):
#     global strr
#     strr *= a
#     print(b)
# prodstr(int(input("Введите количество повторов: ")))
# print(strr)
# def ftest(*args, **kwargs):
#     for el in args + tuple(kwargs.values()):
#         print(el, sep='', end='')
#
# ftest("5*", 5, "=", k1=25, k2="!")


# def hi(a):
#     print(a)
#     if a < 20:
#         return hi(a+1)
#     return a
#
# print(hi(6))


# def hi(a):
#     print(a)
#     if a > 20:
#         return hi(a-1)
#     return a
#
# print(hi(6))



# def hi(a):
#     if a > 20:
#         return hi(a-1)
#     return a
# ko = hi
# mo = ko(90)
# print(mo)


# lam = lambda a, b: print(a)
# lam(5, 3)
#
#
# lam = lambda a, b: a+b
# print(lam(5, 3))


# def mo():
#     print("kol")
#     global no
#     def no():
#         print("JOK")
# mo()
# no()



# def mo():
#     print("kol")
#     ko = 8
#
#     def no():
#         def no2():
#             nonlocal ko
#             ko = 7
#             print("JOK")
#
#         no2()
#     no()
#     print(ko)
#
# mo()



# def decor1(fn):
#     def wrap():
#         print('Дополнение 1')
#         fn()
#         print('Дополнение 2')
#     return wrap
#
#
# @decor1
# def momo(): print('momo')
#
#
# momo()




# def decor1(fn):
#     def wrap(*a):
#         print('Дополнение 1')
#         fn()
#         print(a)
#         print('Дополнение 2')
#         return 8
#     return wrap
#
#
# @decor1
# def momo(): print('momo')
#
#
# @decor1
# def bobo(): print('bobo')
#
# momo(7)
# bobo(9)



# def decor1(fn):
#     def wrap(a=9):
#         print('Дополнение 1')
#         fn()
#         print(a)
#         print('Дополнение 2')
#         return 8
#     return wrap
#
# def decor2(fn):
#     def wrap(*a):
#         print('fgfggfh')
#         fn()
#         print(a)
#         print('fddffg')
#         return 8
#     return wrap
#
# @decor1
# @decor2
# def momo(): print('momo')
#
#
# momo(7)



# def fn():
#     a = 5
#     def fn(n):
#         print(n)
#     fn(a)

#
# def function1():
#     local_value = 10
#     function2(local_value)
#
#
# def function2(value):
#     print(f"Получено значение: {value}")
#
#
# function1()

#
# name = "Ilona"
# def decor1(fn):
#     def wrap():
#         print('Привет,', name)
#     return wrap
#
#
# @decor1
# def momo(): print(name)
#
#
# momo()


# def hard_decorator(name):
#     def inner(fn):
#         def wrapper():
#             print("Привет,", name)
#             fn()
#         return wrapper
#     return inner
#
# @hard_decorator('Egor')
# def say_name():
#     print('name')
#
# say_name()


# Занятие 13 (21 декабря)


# def dec1(fn):
#     def wrapper(a):
#         months = ['Декабрь', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
#                   'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь']
#         print(months[a % 12] + ' - ' + fn(a))
#         if a > 1:
#             return wrapper(a - 1)
#         else:
#             return 0
#     return wrapper
#
# @dec1
# def season(mon: int):
#     ssn = ['Зима', 'Весна', 'Лето', 'Осень']
#     return ssn[mon % 12 // 3]
#
#
# season(12)


# class Koko:
#     pass
#
# n = Koko()
# print(n)


# class Koko:
#     def __str__(self):
#         return "Hello"
#
# n = Koko()
# b = str(n)
# print(b)


# class Koko:
#     def __str__(self):
#         print('none')
#         return 'Hello world'
#
# n = Koko()
# b = str(n)
# print(n)

#
# class Car:
#     def run(self): pass
#
#
# class BMW(Car):
#     def run(self):
#         print('запуск')
#
#
# class Hyundai(Car):
#     def run(self):
#         print('run')
#
# h1 = Hyundai()
# h1.run()


# class Car:
#     def run(self): pass
#
#     def say_hi(self): print('hi')
#
#
# class BMW(Car):
#     def run(self):
#         print('запуск')
#
#
# class BMW2():
#     def run(self):
#         print('запуск')
#
#
# class Hyundai(BMW2, Car):
#     pass
#
# h1 = Hyundai()
# h1.run()
# h1.say_hi()





# class CLS1:
#     def say(self):
#         print('Hello world')
#
#
# class CLS2:
#     def say(self):
#         print('Hi')
#
#
# class CLS3:
#     def say(self):
#         print('Привет!')
#
#
# for i in [CLS1, CLS2, CLS3]:
#     i().say()



# class CLS2:
#     say = 'hi'
#
#
# print(CLS2.say)
# print(CLS2().say)





# class CLS2:
#     say = 'hi'
#     def __init__(self):
#         self.say = 777
#         self.say = 'fg'
#
#
# print(CLS2.say)
# print(CLS2().say)




#
# class CLS2:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def __str__(self): return self.name+" "+self.surname
#
# print(CLS2('Egor', 'Ralovich'))



# class CLS2:
#     def new(cls, name):
#         return name
#
#
# print(CLS2('Egor'))



# class CLS2:
#     def __new__(cls, *args, **kwargs):
#         return "name"
#
#
# print(CLS2())
# print(dir(CLS2))



# class CLS2:
#     def str(self):pass
#     def init(self):
#         self.co = 'komo'
#
#     def say(self): return 'ho'
#
# print(CLS2().say())




# class CLS2:
#     name = 'Egor'
#
# print(CLS2.name) #Вывод: Egor
# CLS2.name = 'hi'
# print(CLS2.name) #Вывод: hi
# obj1 = CLS2()
# obj1.name = 'Jojo'
# print(obj1.name) #Вывод: Jojo
# print(CLS2.name) #Вывод: hi
# print(CLS2().name) #Вывод: hi





# class CAR:
#     def __init__(self):
#         self.colour = 'blue'
#         self.typee = 'jeep'
#         self.year = 2023
#     def say1(self): print('Автомобиль заведен')
#     def say2(self): print('Автомобиль заглушен')
#     def say3(self): print('Год выпуска:', self.year)
#
# CAR().say1()
# CAR().say2()
# CAR().say3()



# class Phone:
#     year = 2023
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model
#
#
# class Apple(Phone):
#     def run(self):
#         print("Телефон Apple: ", self.color, self.model)
#
#
# class Samsung(Phone):
#     pass
#
# phone_object = Phone('green', 4)
# iPhone15ProMax = Apple('black', 15)
# galaxyZ = Samsung('white', 'z')
#
# Phone(color='green', model=4)
# Apple(color="black", model=15).run()
# Samsung(color='white', model="z")


# class Oborot:
#     y = str(input('Введите число: '))
#     def m(self):
#         o = int(self.y)
#         if o is int:
#             print("У вас число")
#
# Oborot().m()


# Занятие 14 (28 декабря)

# class ttt:
#     def __int__(self):
#         self.k = 'hello'
#         return 767676
#
#
# a = ttt()
# int(a)
# print(a.k)



# class ttt:
#
#     m = 'world'
#     def __int__(self):
#         self.k = 'hello'
#         return 767676
#
#
# a = ttt()
# int(a)
# print(ttt.m)
# b = ttt()
# ttt.m = 'rdtfy'
# int(b)
#print(b.m)


# class ttt:
#
#     def mm(self):
#         return 'mm'
#
#     @staticmethod
#     def m(n):
#         n.kk = 'l'
#         return 'mm'
#
# a = ttt()
# a.m(a)
# print(a.kk)


# class Dok:
#
#     #создаем динамический метод
#     def y(self):
#         return 'momo'
#
#     # создаем статический метод
#     @staticmethod
#     def yl():
#         return 'static momo'
#
#
# a = Dok() #создаем объект
# print(a.y()) #вызываем динамический метод
# print(Dok.yl()) #вызываем статический метод через класс
# print(a.yl()) #вызываем статический метод через объект


# class Dok:
#     #создаем динамический метод
#     def y(self):
#         return Dok.yl()
#     # создаем статический метод
#     @staticmethod
#     def yl():
#         return 'static momo'
# a = Dok() #создаем объект
# print(a.y()) #вызываем динамический метод, который возвращает результат




# class Dok:
#
#     # создаем классовый метод, который создает объект от класса и возвращает его
#     @classmethod
#     def yl(cls):
#         return cls()
#
#
# print(Dok.yl()) #вызываем классовый метод и выводим его результат в консоль



#
# class A:
#     def init(self):
#         self.k1 = 'public'
#         self._k2 = 'protected'
#         self.__k3 = 'private'
#
# a = A()
# print(a.k1)
# print(a._k2)
# print(a.__k3)
#
#
# class A:
#     def init(self):
#         self.k1 = 'public'
#         self._k2 = 'protected'
#         self.__k3 = 'private'
#
#     def get_k3(self):
#         return self.__k3
#
# a = A()
# print(a.k1)
# print(a._k2)
# print(a.get_k3())



# class A:
#     def init(self):
#         self.k1 = 'public'
#         self._k2 = 'protected'
#         self.__k3 = 'private'
#
#     def get_k3(self):
#         self.__k3 = 'adsfgfd'
#         return self.__k3
#
# a = A()
#
# class B(A):
#     def ko(self):
#         return A().get_k3()
#
# print(B().ko())


# class A:
#     def __init__(self):
#         self.k1 = 'public'
#         self._k2 = 'protected'
#         self.__k3 = 'private'
#
#     def get_k3(self):
#         return self.__k3
#
#     def set_k3(self, h): # позволяет поменять значение
#         self.__k3 = h
#
#
# a = A()
# print(a.k1)
# print(a._k2)
# print(a.get_k3())
# a.set_k3(h='private2')
# print(a.get_k3())



# class A:
#     m = 'hi'
#     def __init__(self):
#         self.n = 'nn'
# class B(A):
#     def __init__(self, n):
#         # вызываем старую реализацию init у класса-родителя и потом дополняем ее новой
#         super().__init__()
#         self.k = n
#
# class C(B):
#     def __init__(self, k):
#         super().__init__(23)
#         self.m = k
#
# a = C('lll')
# print(a.m)
# print(a.n)



# class A:
#     def init(self):
#         self.n = 'nn'
# class A2:
#     def init(self):
#         self.b = 'bb'
# class B(A):
#     def init(self, n):
#         # вызываем старую реализацию init у класса-родителя и потом дополняем ее новой
#         super().init()
#         self.k = n
# class C(A, A2):
#     def init(self):
#         A2.init(self) #используем реализацию второго класса-родителя
#
# print(C().b)



# class A:
#     def dynm(self, a=None, b=None, c=None):
#         if a != None and b == None and c == None:
#             return a
#         if b != None and c == None:
#             return {a, b}
#         elif c != None:
#             return [a,b,c]
#         return 'параметры отсутствуют'
#
# print(A().dynm())
# print(A().dynm(34))
# print(A().dynm('gfh', 'df'))
# print(A().dynm(6666,66,66))





# class T:
#     def sub(self, other): #когда от объекта отнимают что-то
#         return other+2
#     def rsub(self, other): #когда от чего-либо отнимаем объект
#         return other+5
#
# print(T()-1)
# print(1-T())
#
# class T:
#     def sub(self, other): #когда от объекта отнимают что-то
#         return other+" "+other
#
# print(T()-'kljkklj')



# Задачи экзамена
# import os
# os.mkdir('KOMO') #создаем пустую папку
# os.chdir('KOMO') #переходим в папку
# f = open('hihi1.py', 'w+', encoding='utf-8')
# f.write('print("Ilona")')
# f.close()


# def decore(fn):
#     def wrapper():
#         print('!!!!')
#         fn()
#         print('@')
#     return wrapper
#
# @decore
# def ilona():
#     print("Ilona")
# ilona()
#
#
# @decore
# @decore
# def vashkevich():
#     print("Vashkevich")
# vashkevich()



from abc import ABC

# from abc import ABC, abstractmethod
#
# class Abst(ABC):
#     @abstractmethod
#     def momo(self):
#         pass
#
#     @abstractmethod
#     def momo2(self):
#         pass
#
# class Home(Abst):
#     def momo(self): print('Go home')
#
#     def momo2(self): print('Go home 2')
#
#     @staticmethod
#     def momo3(): print("Go home 3")
#
# home = Home()
# home.momo()
# home.momo2()
# home.momo3()


class SimpleIterator:
    def __iter__(self):
        return self

    def __init__(self, name):
        self.name = name
        self.len = len(self.name)

    def __next__(self):
        i = 0
        if self.name[i] < self.len:
            self.name[i] += 1
            return self.name[i]
        else:
            raise StopIteration


#print('8 january')



