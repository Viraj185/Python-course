def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


fact = input("Enter a number: ")

print(f"Fatorial of the number is :{factorial(int(fact))}")