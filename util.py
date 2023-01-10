
def nth_power(n, fn = lambda x: x**3):
    """
    calculates power  for number up to n
    args:
        n: highest number in the list of numbers
        power: power for numbers to raisse, default power is 3
    """
    return [fn(i) for i in range(n)]

print(nth_power(10))
print(nth_power(20))