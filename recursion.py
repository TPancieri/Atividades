def factorial(x):
    """Função que recebe um x e seu retorna seu valor fatorial"""
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)


f = 5

print(f"O valor de {f} é " + str(factorial(f)))
