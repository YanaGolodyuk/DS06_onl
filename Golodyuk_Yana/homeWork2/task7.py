# Продуктовый склад и магазин находятся на одной дороге города Н. 
# Склад находится на отметке A км, а магазин — B км. 
# Средняя скорость автомобиля, доставляющего товары, C км/ч. 
# За какое время продукты попадают со склада в магазин?
# Формат ввода Три натуральных числа A, B и C, каждое на отдельной строке.
# Пример:
# Ввод
# 10
# 32
# 5
# Вывод
# 4.40

import math
def func():
    a, b, c = map(int, input().split())
    road_time = abs(b - a) / c
    print('%.2f' % road_time)

if __name__ == "__main__":
    func()