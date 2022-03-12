import math
# CTI-110
# P3HW2 - Pizza Order
# Josh Lockart
# 3/11/2022

def main():

    # User inputs how many students and people per pizza
    student_pizza = int(input('How many students do you want pizza for?'))
    people_per_pizza = float(input('Enter number of people per pizza (1.5, 2, 3):'))

    # Calculating pizzas needed plus the total cost with a 6% tax
    pizzas_needed = int(student_pizza / people_per_pizza)
    pizza_tax = float(5 * pizzas_needed * 0.06)
    pizza_total = float(5 * pizzas_needed + pizza_tax)

    # Outputting user input
    print('How many students do you want pizza for?', student_pizza)
    print('Enter number of people per pizza (1.5, 2, 3):', people_per_pizza)

    # Running user input through statements 
    if people_per_pizza == 1.5:
        print('----Pizza Order--------')
        print('Number of Students :', student_pizza)
        print('Pizzas Needed:', pizzas_needed)
        print('Price ${:.2f}'.format(pizza_total))
        print('--------------------------')
    elif people_per_pizza == 2:
        print('----Pizza Order--------')
        print('Number of Students :', student_pizza)
        print('Pizzas Needed:', pizzas_needed)
        print('Price ${:.2f}'.format(pizza_total))
        print('--------------------------')
    elif people_per_pizza == 3:
        print('----Pizza Order--------')
        print('Number of Students :', student_pizza)
        print('Pizzas Needed:', pizzas_needed)
        print('Price ${:.2f}'.format(pizza_total))
        print('--------------------------')
    else:
        print()
        print('INVALD ENTRY!!!!')
        print('Should have entered, 1.5, 2, or 3\n')
        print('Run Program again')

# Executing program
main()