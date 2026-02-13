import time
import sys

# increase limit for big integer to string conversion
sys.set_int_max_str_digits(1000000)

def calprod() -> int:
    product = 1 
    for i in range(1, 100000):
        product *= i
    return product

star_time = time.time()
result = calprod()
end_time = time.time()

elapsed = end_time - star_time

print(f'The result is {len(str(result))} digit long.')
print(f'Took {elapsed:.2f} seconds to calculate.')