import time

F = [-1]*1001
F[0] = 1
F[1] = 1

def fibonacci_optimised(n):
    global N
    if F[n] != -1:
        return F[n]
    else:
        N += 1
        F[n] = fibonacci_optimised(n-1) + fibonacci_optimised(n-2)
        return F[n]

def fibonacci_not_optimised(n):
    global N
    if n == 1 or n == 0:
        return 1
    else:
        N += 1
        return fibonacci_not_optimised(n-1) + fibonacci_not_optimised(n-2)

nbr = 20

print("Dynamic programming : \n")
t = time.time()
N = 0
print("Fibonacci(" + str(nbr) + ") = " + str(fibonacci_optimised(nbr)))
print("Time of execution : " + str(time.time() - t))
print("Nbr of execution of the fibonacci function" + str(N))

print("\n--------------\n")

N = 0
t = time.time()
print("Fibonacci(" + str(nbr) + ") = " + str(fibonacci_not_optimised(nbr)))
print("Time of execution : " + str(time.time() - t))
print("Nbr of execution of the fibonacci function" + str(N))
