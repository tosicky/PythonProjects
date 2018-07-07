import time

start_time = time.time()
#sys.setrecursionlimit(10000)

def primeNum(num):
    primeNum = [2]

    if num < 2:
        pass
    else:
        x = 3
        while x <= num:
            for y in primeNum:  # use the primes list!
                if x % y == 0:
                    x += 2
                    break
            else:
                primeNum.append(x)
                x += 2

    for prime in primeNum:
        yield prime

    #return primeNum


if __name__ == "__main__":

    number = int(input("Enter the number: "))

    #prime1 = next((prime for prime in primeNum(number)), False)

    prime = primeNum(number)

    print(next(prime))
    print(next(prime))

print("--- %s seconds ---" % (time.time() - start_time))
