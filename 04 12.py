##import random
##
##def power_a3(a):
##    cube = a*a*a
##    return cube
##for i in range(5):
##    x = random.randint(-5,5)
##    print('x=', str(x), 'x^3' str(power_a3(x)))
#Proc2. Описать 2 функции PowerA2(А), PowerA4(A),
#вычисляющие вторую и четвертую степень
#числа A и возвращающие эти степени (параметры являются вещественными).
#С помощью этих функций найти вторую и четвертую степень пяти случайных чисел
##import random
##
##def power_a2(a):
##    cfadrat = a*a
##    return cfadrat
##for i in range(5):
##    x=random.randint(-5,5)
##    print(power_a2(x))
##def power_a4(a):
##    stepen = a*a*a*a
##    return stepen
##for i in range(5):
##    x=random.randint(-5,5)
##    print(power_a4(x))
#Proc3. Описать 2 функции aMean(X, Y), gMean(X,Y), вычисляющие
#среднее арифметическое aMean = (X+Y)/2 и среднее геометрическое
#gMean = √ X·Y двух положительных чисел X и Y (X и Y — входны
#параметры вещественного типа). С помощью этих функций найти
#среднее арифметическое и среднее геометрическое для 10 пар случайных чисел
##import random
##import math
##
##def aMean(x, y):
##    srednee_arifm= (x+y)/2
##    return srednee_arifm
##for i in range(10):
##    a=random.randint(1,11)
##    b=random.randint(1,11)
##    print(aMean(x,y))
##def gMean(x, y):
##    srednee_geometr= sqrt (x*y)
##    return srednee_geometr
##for i in range(10):
##    a=random.randint(1,11)
##    b=random.randint(1,11)
##    print(gMean(x,y))
#Proc4. Описать 2 функции triangleP(a) и triangleS(a),
#вычисляющие по стороне a равностороннего треугольника его периметр P = 3·a
#и площадь S = a 2 · √ 3/4 (параметры являются вещественными).
#С помощью этих функций найти периметры и площади трех равносторонних
#треугольников с данными сторонами (стороны ввести с клавиатуры).
##import random
##import math
##def triangleP(a):
##    perimetr= 3 * a
##    return perimetr
##for i in range(3):
##    x=random.randint(1,11)
##    print(triangleP(x))
##def triangleS(a):
##    s= a *2 * sqrt(3/4)
##for i in range(3):
##    x=random.randint(1,11)
##    print(trianglep(x))
#Proc5. Описать 2 функции rectP(x1, y1, x2, y2) и rectS(x1, y1, x2, y2),
#вычисляющие периметр P и площадь S прямоугольника со сторонами,
#параллельными осям координат, по координатам (x1, y1), (x2, y2)
#его противоположных вершин. С помощью этих функций найти периметры
#и площади трех прямоугольников с данными противоположными вершинами
##import random
##import math
##def rectP(x1,x2,y1,y2):
##    p= abs(x2-x1) *2 + abs(y2-y1) *2
##    return p
##for i in range(3):
##    a=random.randint(1,11)
##    b=random.randint(1,11)
##    print(rectP(a, b))
##    def rectS(x1,y1,x2,y2):
##        s = abs(x2-x1) *2 * abs(y2-y1) * 2
##        return s
##for i in range(3):
##    a=random.randint(1,11)
##    b=random.randint(1,11)
##    print(rectS(a,b))






















#Proc6. Описать функцию digitSum(K),
#находящую сумму цифр целого
#положительного числа K (K входной параметр целого типа).
#С помощью этой функции найти сумму цифр для каждого из пяти данных целых чисел
import math
import random
def digitSum(K)
sum=
















