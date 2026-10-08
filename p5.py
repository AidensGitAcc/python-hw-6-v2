def checkFactors(n):
    found = False
    for i in range(2, n):
        if n % i == 0:
            found = True
    return found

def main():
    print("This program checks whether a number is prime")
    n = int(input("Enter an integer: "))
    if n < 2:
        print(n, "is not prime")
    elif checkFactors(n):
        print(n, "is not prime")
    else:
        print(n, "is prime")

main()
