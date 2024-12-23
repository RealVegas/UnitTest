# Простые функции

# Сложение
def add(a, b) -> int | float:
    return a + b


# Вычитание
def substract(a, b) -> int | float:
    return a - b


# Умножение
def multiply(a, b) -> int | float:
    return a * b


# Деление
def divide(a, b) -> int | float | None:
    if b == 0:
        raise ValueError('На ноль делить нельзя')
    else:
        return a / b


# Остаток от деления
def modulo(a, b) -> int | float | None:
    if b == 0:
        raise ValueError('На ноль делить нельзя, остаток от деления не определен')
    else:
        return a % b