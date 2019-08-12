def prime(number):
    i = 2
    while (i < number):
        if(number % i == 0):
            return False
        i += 1
    return True

def prime_generator():
    j = 2
    while True:
        if(prime(j)):
            yield j
        j += 1

for x in prime_generator():
    if(x > 2000):
        break
    print(x)
