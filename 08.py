#12
for i in range(-25, 26):
    if i == 0:
        continue
    print(i, end=' ')


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