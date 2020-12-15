from math import sqrt

a, b, c = list(map(int, input().split()))
D = b ** 2 - 4 * a * c


if D < 0:
    print("Нет решений")


elif D == 0:
    x = (-1 * b + sqrt(D)) / (2 * a)
    print("Уравнение имеет одно решение:", x)

else:
    x1 = (-1 * b + sqrt(D)) / (2 * a)
    x2 = (-1 * b - sqrt(D)) / (2 * a)
    print("Уравнение имеет два решения:", x1, "и", x2)