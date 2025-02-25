x1 = float(input("Podaj pierwszą liczbę: "))
x2 = float(input("Podaj drugą liczbę: "))
z = input("Wybierz znak działąnia (* + - /): ")
zm  = ['*', '+', '-', '/']

def działanie(a, b, y):
    w1 = 'wynik'
    w2 = 'wynik'
    if(y == '/'):
        if(b != 0):
            w1 = a / b
        elif(b == 0):
            w1 = 'dzielenie przez 0'
            if(a == 0):
                w2 = 'dzielenie przez 0'  
        if(a != 0):
            w1 = b / a
        elif(a ==0):
            w1 = 'dzielenie przez 0'
            if(b == 0):
                w2 = 'dzielenie przez 0'  
        return (f'{w1} {w2}')
    elif(y == '-'):
        w1 = a - b
        w2 = b - a
        return (f'{w1} {w2}')
    elif(y == '+'):
        return (f'{a + b}')
    elif(y == '*'):
        return (f'{a * b}')

napis = działanie(x1, x2, z)
print(napis)
zm.remove(z)

for i in range(len(zm)):
    napis = działanie(x1, x2, zm[i])
    print(napis)