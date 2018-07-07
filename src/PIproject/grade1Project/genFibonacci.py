"""
Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

"""
import time

start_time = time.time()


def fibonaci(num):
    result = []
    a = 1
    b = 1

    for n in range(num):
        result.append(a)
        olda = a
        a = b               # or use a tuple as -> a,b = b, a+b
        b = olda + b
        #a, b = b, a + b
    return result


#print(fibonaci(10))


if __name__ == "__main__":
    number = int(input("Enter the number you want fibonacci sequence for: "))

    fibGen = fibonaci(number)

    print("The fibonacci sequence for " + str(number) + "\n{}".format(fibGen))

    print("--- %s seconds ---" % (time.time() - start_time))