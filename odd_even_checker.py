x = int(input("Enter a whole number: "))
if x % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

decision = input("Do you want to check another number? (y/n): ")
if decision.lower() == 'y':
    x = int(input("Enter a whole number: "))
    if x % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("Goodbye!")