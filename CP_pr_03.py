def power_modulo(a, b, m):
    result = 1
    a %= m

    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        b //= 2
        a = (a * a) % m

    return result

if __name__ == "__main__":
    a, b, m = map(int, input().split())

    result = power_modulo(a, b, m)

    print("Result is:", result)
