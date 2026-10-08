def classifyAge(age):
    if age <= 12:
        group = "You are a child"
    elif age <= 19:
        group = "You are a teenager"
    elif age <= 65:
        group = "You are an adult"
    else:
        group = "You are a senior"
    if age > 100:
        group = group + ". Congratulations on appearing on the Smucker's jar!"
    return group

def main():
    print("This program classifies a person by their age")
    age = int(input("Enter your age: "))
    print(classifyAge(age))

main()
