def is_prime(func):
    def wrapper(a, b, c):
        res = func(a, b, c)
        k = 0
        for i in range(2, res):
            if res % i == 0:
                k = k + 1
        if k == 0:
            print('Простое')
        else:
            print('Составное')
        return res

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
