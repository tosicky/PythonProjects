"""
Have the user enter a number and find all Prime Factors (if there are any) and display them
"""

import time

start_time = time.time()

#values = 600851475143

def primeFac(values):
    i = 2
    primeFac = []

    while i <= values:

        if values % i == 0:
            values //= i
            #print(values)
            primeFac.append(i)
        else:
            i += 1
    return primeFac


if __name__ == "__main__":

    value = int(input("Enter a value: "))
    result = primeFac(value)
    print("Prime Factors are: ", result)
    print(max(result))

    primeFacProduct = 1

    for i in result:

        primeFacProduct *= i

    print("Multiplication of the prime factors: " , primeFacProduct)

    print("--- %s seconds ---" % (time.time() - start_time))