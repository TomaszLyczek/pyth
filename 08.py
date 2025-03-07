#22
num = []
num.append(int(input('Podaj liczbę: ')))
num.append(int(input('Podaj liczbę: ')))
while num[len(num)-1] != num[len(num)-2]:
    num.append(int(input('Podaj liczbę: ')))
print(num)

#21
# poprzednia = 0
# message = 'rosnące'
# for i in range(5):
#     x = int(input(f'Podaj {i+1} liczbę: '))
#     if i == 0: poprzednia = x
#     else:
#         if x < poprzednia:
#             message = 'nierosnące'
#         poprzednia = x  
# print(message)


#20
# import random
# x = []
# for i in range(21):
#     x.append(random.randint(-100, 100))
# print(x)

# parz = []
# nparz = []
# for i in range(len(x)):
#     if x[i] % 2 == 0:
#         parz.append(x[i])
#     else:
#         nparz.append(x[i])
# parz.extend(nparz)
# print(parz)

# lista = [1, 3, 5, 6, 498, 352, 34, 56, 3]
# l2 = []
# parzyste = lambda a: a % 2 == 0
# nieparzyste = lambda a: a % 2 == 1

# l2 = list(filter(parzyste, lista))
# print(lista)
# print(l2)
# print(set(filter(nieparzyste, lista)))

#19
# liczby = []
# for i in range(1001):
#     if i % 6 == 0:
#         liczby.append(str(i))
# print(*liczby)
# print('Ilość liczb podzielnych przez 6: ', len(liczby))

# liczbyz7 = []
# for i in liczby:
#     if str(i).find('7') != -1: liczbyz7.append(i)
# print(liczbyz7)


#18
# x = 0
# suma = 0
# while(x not in range(1, 11)):
#     x = int(input('Podaj liczbę: '))
#     if (x in range (1, 11)): continue
#     print('Dwukrotność podanej liczby: ', x*2)
#     suma += x
# print('Suma: ', suma)



#17
# limit = 100
# l1 = 6
# l2 = 2
# for i in range(limit):
#     if i % 2 == 0:
#         print(l1, end = ' ')
#         l1 += 2
#     else:
#         print(l2, end = ' ')
#         l2 += 1


#16
# limit = 100
# element = 100
# licznik = 0
# while licznik < limit:
#     element = element - licznik
#     print(element, end = ' ')
#     licznik += 1
#     if licznik == 100: print('Ostatni element: ', element)


#15
# licznik = 1
# element = 1
# limit = 100
# while licznik <= limit:
#     for i in range(element):
#         print(element, end=' ')
#         licznik += 1
#         if licznik > limit: break
#     element += 1


#14
# for i in range(1, 101):
#     if i % 2 == 0:
#         print(1, end=' ')
#     elif (i + 3) % 4 == 0:
#         print(3, end=' ')
#     elif (i + 1) % 4 == 0:
#         print(2, end=' ')


#13
# wysw = 0
# pom = 0
# for i in range (1, 121):
#     if i % 5 == 0 and i % 11 == 0:
#         pom += 1
#         continue
#     print(i, end=' ')
#     wysw += 1
# print(f'wyswietlono {wysw}, pominięto {pom}')


#12
# for i in range(-25, 26):
#     if i == 0:
#         continue
#     print(i, end=' ')


#11
# x = 101
# while x > 11:
#     x -= 1
#     if x % 7 == 0:
#         continue
#     print(x, end=' ')


#10
# for i in range(100):
#     print(i + 1)
# x = 0
# while x < 100:
#     x += 1
#     print(x)


#09
# x = int(input('Podaj liczbę całkowitą: '))
# if x < 0:
#     x -= 1
# elif x > 0:
#     x += 1
# print(f'x = {x}')
# if x % 2 == 0:
#     print(f'liczba {x} jest parzysta')
# elif x % 2 != 0:
#     print(f'liczba {x} jest nieparzysta')


#085
# x1 = float(input("Podaj pierwszą liczbę: "))
# x2 = float(input("Podaj drugą liczbę: "))
# z = input("Wybierz znak działąnia (* + - /): ")
# zm  = ['*', '+', '-', '/']

# def działanie(a, b, y):
#     w1 = 'wynik'
#     w2 = 'wynik'
#     if(y == '/'):
#         if(b != 0):
#             w1 = a / b
#         elif(b == 0):
#             w1 = 'dzielenie przez 0'
#             if(a == 0):
#                 w2 = 'dzielenie przez 0'  
#         if(a != 0):
#             w1 = b / a
#         elif(a ==0):
#             w1 = 'dzielenie przez 0'
#             if(b == 0):
#                 w2 = 'dzielenie przez 0'  
#         return (f'{w1} {w2}')
#     elif(y == '-'):
#         w1 = a - b
#         w2 = b - a
#         return (f'{w1} {w2}')
#     elif(y == '+'):
#         return (f'{a + b}')
#     elif(y == '*'):
#         return (f'{a * b}')

# napis = działanie(x1, x2, z)
# print(napis)
# zm.remove(z)

# for i in range(len(zm)):
#     napis = działanie(x1, x2, zm[i])
#     print(napis)