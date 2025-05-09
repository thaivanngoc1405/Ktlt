print("Thai Van Ngoc ")
print("MSSV:235752020710016 ")
print("#####################")
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

prime_numbers = tuple(filter(is_prime, range(2, 1000000)))

print("Tuple chứa các số nguyên tố nhỏ hơn 1 triệu:")
print(prime_numbers[:10], "...", prime_numbers[-10:])

