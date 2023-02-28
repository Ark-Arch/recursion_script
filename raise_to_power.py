
def raise_to_power(base, exponent):
    if (exponent < 2):
        return base
    else:
        return base * raise_to_power(base, exponent-1)

print(raise_to_power(2,5))