import random
import timeit


def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


def binary_search(data, key):
    low = 0
    upper = len(data) - 1
    while low <= upper:
        mid = (low + upper) // 2  
        if data[mid] < key:    
            low = mid + 1
        elif data[mid] > key:  
            upper = mid - 1
        else:                    
            return mid
    return -1

def fibonacci_search(arr, x):

    fib2 = 0
    fib1 = 1
    fib = fib1 + fib2
    while fib < len(arr):
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2
    
    offset = -1
    while fib > 1:
        i = min(offset + fib2, len(arr) - 1)
        if arr[i] < x:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif arr[i] > x:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i
    
    if fib1 and offset + 1 < len(arr) and arr[offset + 1] == x:
        return offset + 1
    
    return -1

Linear_times = []
Binary_times = []
Fibonacci_times = []


for n in range(10, 1010, 10):
    S = [random.randint(1, 1000) for _ in range(n)]
    x = random.randint(1, 1000)
    Linear_time = timeit.timeit(lambda: linear_search(S, x), number = 5) / 5
    Binary_time = timeit.timeit(lambda: binary_search(S, x), number = 5) / 5
    Fibonacci_time = timeit.timeit(lambda: fibonacci_search(S, x), number = 5) / 5

    Linear_times.append(Linear_time)
    Binary_times.append(Binary_time)
    Fibonacci_times.append(Fibonacci_time)

    print("Linear search,S =", len(Linear_times)*10, ",time:", Linear_times[(n // 10) - 1])
    print("Binary search,S =", len(Binary_times)*10, ",time:", Binary_times[(n // 10) - 1])
    print("Fibonacci search,S =", len(Fibonacci_times)*10, ",time:", Fibonacci_times[(n // 10) - 1])

