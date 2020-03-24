def primes(n):
    '''Returns a list of all prime numbers less than n'''
    prime = []
    for y in range(2, n + 1):
        for z in range(2, int(y**0.5)+1):
            if y % z == 0:
                break
        else:
            prime.append(y)
    return prime


def is_prime(m):
    '''Returns a boolean indicating whether `m` is a prime number'''
    if m in primes(m):
        return True
    return False
