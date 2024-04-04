import itertools


# НОД
def gcd(a, b):
    r = a % b

    while r:
        a = b
        b = r
        r = a % b

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


# Ввести систему из <congruence_count> шт. уравнений.
def input_system(congruence_count):
    result = []
    for i in range(congruence_count):
        a = 1
        b = int(input(f'b{i + 1}: '))
        m = int(input(f'm{i + 1}: '))
        result.append((a, b, m))

    return result


# Обратный к <x> элемент в кольце по модулю <m>
def inverse_element(x, m):
    return (x ** (eulers_totient(m) - 1)) % m


def main():
    congruence_count = int(input('Количество сравнений: '))
    congruence_system = input_system(congruence_count)

    sub_trans = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

    print('Решаем систему уравнений:')
    print('┌')
    for cong in congruence_system:
        print(f'│ x = {cong[1]} (mod {cong[2]})')
    print('└')

    m_list = [congruence[2] for congruence in congruence_system]
    for pair in itertools.combinations(m_list, 2):
        if gcd(pair[0], pair[1]) != 1:
            print(f'Модули {pair[0]} и {pair[1]} не взаимно простые, КТО не применима')
            return

    M_list = []
    N_list = []
    for i in range(congruence_count):
        M_i = 1
        for cong_idx in range(congruence_count):
            if cong_idx != i:
                M_i *= m_list[cong_idx]
        M_list.append(M_i)

        print(f'M{str(i + 1).translate(sub_trans)} = {M_i}')
    print()

    for i in range(congruence_count):
        N_i = inverse_element(M_list[i], m_list[i])
        N_list.append(N_i)

        print(f'N{str(i + 1).translate(sub_trans)} = {N_i}')
    print()

    result_mod = 1
    for m_i in m_list:
        result_mod *= m_i

    result = 0
    for i in range(congruence_count):
        result += congruence_system[i][1] * M_list[i] * N_list[i]

    result = result % result_mod

    print(f'Ответ: x = {result} (mod {result_mod})')


if __name__ == '__main__':
    main()
