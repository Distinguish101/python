print(2**3)

def exponent(base, power):
    result = 1
    for index in range(power):
        result = result * base
    return result


print(exponent(2,9))