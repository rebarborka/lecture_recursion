
def recursive_nth_fibo(cislo):
    if cislo == 0:
        return 0
    elif cislo == 1:
        return 1
    else:
        return recursive_nth_fibo(cislo - 1) + recursive_nth_fibo(cislo-2)

def main():
    n = int(input("Počet členov Fibonacciho postupnosti:"))
    sekvencia = [recursive_nth_fibo(num) for num in range(n+1)]
    print(sekvencia)

    pass


if __name__ == "__main__":
    main()
