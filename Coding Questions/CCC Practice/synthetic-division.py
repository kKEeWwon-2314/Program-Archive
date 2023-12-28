def synthetic_division(dividend, divisor):
    dividend = list(dividend)
    normalizer = int(divisor)

    for i in range(len(dividend) - len(divisor) + 1):
        dividend[i] /= normalizer

        c = dividend[i]
        if c != 0:  # Useless to multiply if coef is 0
            for j in range(1, len(divisor)):
                dividend[i + j] += -divisor[j] * c
    separator = 1 - len(divisor)
    return dividend[:separator], dividend[separator:]