primes = [1, 2, 3, 4]

it = primes.__iter__()

while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
    
