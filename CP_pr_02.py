def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_alternate_primes(N):
    primes = []
    current_number = 2

    while len(primes) < 2 * N:
        if is_prime(current_number):
            primes.append(current_number)
        current_number += 1

    for i in range(0, len(primes), 2):
        print(primes[i], end=" ")
    print()

if __name__ == "__main__":
    n = int(input())
    print_alternate_primes(n)
