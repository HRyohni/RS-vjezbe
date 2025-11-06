# Prost broj je prirodan broj veći od 1 koji je dijeljiv jedino s 1 i samim sobom.
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1): # ovo je chatGpt rijesio ne znam matematiku :(
        if n % i == 0:
            return False
    return True


def primes_in_range(br1, br2):
    return [x for x in range(br1,br2) if isPrime(x)]





print(isPrime(7))   # True
print(isPrime(10))  # False
print(primes_in_range(1, 10)) # [2, 3, 5, 7]