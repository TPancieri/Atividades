def factorial(number: int) -> int:
    """Da o fatorial de um 'number'

    :param number: Numero para calcular fatorial
    :return: O produto de todos os valores de 1 ate o numero, inclusivo
    """

    if number == 0:
        return 1

    value = 1
    for i in range(1, number + 1):
        total = value * i
        value = total
    return total


for x, index in enumerate(range(36)):
    print(index, factorial(x))
