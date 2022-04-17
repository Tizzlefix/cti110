 # A brief description of the project
    # 4/16/2022
    # CTI-110 P5HW2 - Math Quiz
    # Joshua Lockart

import random
# function for addition
def Addition():

    # getting random integers in range 1 to 100
    a = random.randint(1,100)
    b = random.randint(1,100)
    print("   ",a)
    print(" + ",b)

    # calculating sum
    sum = a+b
    # asking for user answer
    answer = int(input("\nEnter answer: "))
    # variable to count guesses
    guess = 1
    # loop for getting answer while answer is not correct

    while sum!=answer:
        # if answer less than sum print it is too low
        if answer<sum:
            print("Sorry, guess is too low.")
        # if answer more than sum print it is too high
        else:
            print("Sorry, guess is too high.")
        # again getting user input
        answer = int(input("\ntry again: "))
        # incrementing the count of gueses
        guess+=1

    # printing congratulation if answer is correct
    print("Congratulations!!!! your answer is correct....")
    # printing number of gueses
    print("Number of guesses: ",guess)

# function for subtraction
def Subtraction():

    # getting random integers in range 1 to 100
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    print("   ", a)
    print(" - ", b)
    # calculating difference
    diff = a - b
    # asking for user answer
    answer = int(input("\nEnter answer: "))
    # variable to count guesses
    guess = 1
    # loop for getting answer while answer is not correct

    while diff != answer:
        # if answer less than diff print it is too low
        if answer < diff:
            print("Sorry, guess is too low.")
        # if answer more than diff print it is too high
        else:
            print("Sorry, guess is too high.")
        # again getting user input
        answer = int(input("\ntry again: "))
        # incrementing the count of gueses
        guess += 1

    # printing congratulation if answer is correct
    print("Congratulations!!!! your answer is correct....")
    # printing number of gueses
    print("Number of guesses: ", guess)

# function to display menu and get user choice
def main():

    # displaying menu
    print("\nMain Menu")
    print("-"*15)
    print("1. Addition Random Numbers")
    print("2. Subtraction Random Numbers")
    print("3. Exit\n")
    # getting user input
    
    option = int(input("Please choose one of the option: "))
    # if option equals to 1 call Addition() function
    if option==1:
        Addition()
    # if option equals to 2 call Subtraction() function
    elif option==2:
        Subtraction()
    # if option equals to 3 exit the program
    elif option == 3:
        print("Thank you for playing..")
        print("Bye!!")
        exit()
    # else print invalid option
    else:
        print("Invalid option. Please choose again")
    # again calling the function until user exits the program

    main()


print("Welcome to the Math Quiz\n")
main()