def nth_power(n, power):
    """
    calculates power  for number up to n
    """
    return [i**power for i in range(n)]

print(nth_power(10, 4))
print(nth_power(20, 4))