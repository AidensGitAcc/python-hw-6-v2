def triangleType(a, b, c):
    if a == b and b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "scalene"

def main():
    print("This program helps Telly Monster identify triangles")
    a = float(input("Enter the length of side 1: "))
    b = float(input("Enter the length of side 2: "))
    c = float(input("Enter the length of side 3: "))
    print("The triangle is", triangleType(a, b, c))

main()
