#This is a hello world code.... But better 🤡🤡
import random

def Hello_World():
    name = input("What is your name? ")
    while True:
        try:

            age = int(input ("What is your age? "))
            if age <= 0:
                print("Age cannot be negative or zero.")
            else:
                break
        except ValueError:
            print("Please enter a valid age.")

    fun_fact = ""
    random_number = random.randint(1, 100)
    if (random_number <= 25):
        fun_fact = "Did you know birds chirp!!" 
    elif (random_number <= 50):
        fun_fact = "Did you know that the Eiffel Tower can be 15 cm taller during the summer?"
    elif (random_number <= 75):
        new_age = age + 2
        fun_fact = f'Did you know that you were never born {new_age} years ago!!'
    else:
        fun_fact = "Did you know that honey never spoils!!"

    print(f"Hello {name}!")
    print("Fun Fact: ", fun_fact)

    decision = input("Would you like to try again?(Y/N): ").strip().lower()
    if decision == "y":
        Hello_World()
    else:
        print("Thank you for using the program. Goodbye!!!!!")
Hello_World()