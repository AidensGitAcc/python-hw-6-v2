def chaos(k, x, n):
    for i in range(n):
        x = k * x * (1 - x)
        print(x)

def main():
    print("This program illustrates a chaotic function")
    k = float(input("Enter k: "))
    x = float(input("Enter starting x: "))
    if x < 0 or x > 1:
        print("Error: x must be between 0 and 1")
    else:
        n = int(input("Enter the number of iterations: "))
        chaos(k, x, n)

main()
