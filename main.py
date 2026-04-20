# 1-mashq
def is_palindrome(num):
    return str(num) == str(num)[::-1]

print(is_palindrome(12321)) 
print(is_palindrome(12345))  
# 2-mashq
def flexible_sum(*args, **kwargs):
    total = sum(args)
    if 'multiplier' in kwargs:
        total *= kwargs['multiplier']
    return total

print(flexible_sum(1, 2, 3, multiplier=2))  
# 3-mashq
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} bajarilish vaqti: {end-start:.4f} soniya")
        return result
    return wrapper

@timer
def heavy_calc(n):
    return sum(i*i for i in range(n))

print(heavy_calc(1000000))
