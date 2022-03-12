# I was supposed to put a comment here
# My Last Name

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = range(90, 100)
    B_Score = range(80, 89)
    C_Score = range(70, 79)
    D_Score = range(60, 69)
    F_Score = range(0, 59)
    

    # Inputs user integer
    score = int(input('Enter grade: '))

    # Running user input through statements
    if score in A_score:
        print('Your grade is: A')
    elif score in B_Score:
        print('Your grade is: B')
    elif score in C_Score:
        print('Your grade is: C')
    elif score in D_Score:
        print('Your grade is: D')
    elif score in F_Score:
        print('Your grade is: F')
    else:
        print("Your grade isn't readable, please try again.")
        

# program start

main()