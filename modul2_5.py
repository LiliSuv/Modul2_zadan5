print('ВАРИАНТ 1')
def get_matrix(a, b, value):
    matrix = [[]]
    for n in matrix * b:
        n.append (value)
        rez = matrix * a
    print (rez)


a = int (input ('Введите число строк '))
b = int (input ('Введите число столбцов '))
value = int (input ('Введите значение '))
get_matrix(a, b, value)
print('ВАРИАНТ 2')
def get_matrix(a,b,value):
    m = []
    for i in range (b):
        m.append (value)
        n = []
        for i in range (a):
            n.append (m)
    print (n)
a = int (input ('Введите число строк '))
b = int (input ('Введите число столбцов '))
value = int (input ('Введите значение '))
get_matrix(a, b, value)