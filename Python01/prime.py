def is_prime(n):
    if n <= 1:
        # return False  # 0 and 1 are not prime numbers
        return 0
    # if n == 2 or n == 3:
    if n in [2,3]:
        # return True  # 2 and 3 are prime numbers
        return 1    
    if n % 2 == 0 or n % 3 == 0:
        # return False  # Eliminate multiples of 2 and 3
        return 0
    
    # Check divisors from 5 to √n, skipping multiples of 2 and 3
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            # return False
            return 0
        i += 6
    # return True
    return 1


print(is_prime(2))    
print(is_prime(11))   
print(is_prime(25))   
print(is_prime(1))    
