import math


# Реализовать программный продукт решения сравнений первой степени
# с указанием всех промежуточных шагов вычисления. Реализовать возможность того,
# что сравнение не имеет решений или имеет больше одного решения.
#
# ПРИМЕРЫ:
# 111x = 75 (mod 321)
# Решение 1: x1 = 99
# Решение 2: x2 = 206
# Решение 3: x3 = 313
#
# 25x = 3 (mod 35)
# Не имеет решений

# НОД
def gcd(a, b):
    print(f'> Находим НОД({a}, {b}):')
    orig_a = a
    orig_b = b

    r = a % b
    print(f'>>> a={a}, b={b}, r={r}')
    while r:
        a = b
        b = r
        r = a % b
        print(f'>>> a={a}, b={b}, r={r}')

    print(f'> Нашли НОД({orig_a}, {orig_b}) = {b}')
    return b


# Разложение числа на множество простых множителей
def factors(n):
    factors_set = set()
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n //= i
                factors_set.add(i)
                break

    return factors_set


# Функция Эйлера
def eulers_totient(n):
    result = n
    for f in factors(n):
        result *= (1 - (1 / f))

    return round(result)


# Ввод сравнения
def input_congruence():
    a = int(input('a: '))
    b = int(input('b: '))
    m = int(input('m: '))
    return (a, b, m)


def main():
    a, b, m = input_congruence()
    original_m = m
    print(f'Решаем сравнение {a}*x = {b} (mod {m})')

    if b > m:
        while (b > m):
            b = b - m
        print(f'Упростим: {a}*x = {b} (mod {m})')

    temp_gcd_am = gcd(a, m)

    if (b % temp_gcd_am != 0):
        print(f'Сравнение не имеет решений (b={b} не делится на НОД({a}, {m})={temp_gcd_am})')
        return

    print(f'Количество решений сравнения [НОД({a}, {m})]: {temp_gcd_am}')
    gcd_b_am = gcd(temp_gcd_am, b)
    if gcd_b_am > 1:
        a = int(a / gcd_b_am)
        b = int(b / gcd_b_am)
        m = int(m / gcd_b_am)
        print(f'Поделим все на {gcd_b_am}: {a}*x = {b} (mod {m})')

    x0 = int((b * (a ** (eulers_totient(m) - 1))) % m)

    if (original_m > m):
        xi = x0
        i = 1
        while (xi < original_m):
            print(f'Решение {i}: x{i} = {xi}')
            xi += m
            i += 1
    else:
        print(f'Единственное решение: x = {x0}')


if __name__ == '__main__':
    main()