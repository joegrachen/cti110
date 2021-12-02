# A math quiz with random numbers
# 11/07/2021
# CTI-110 P5HW2 - Math Quiz
# Joseph Grachen
#

def main():

    import random

    def rand_add():
        x = random.randint(1, 100)
        print(' ', x)
        y = random.randint(1, 100)
        print('+', y)

        the_answer = int(input('And the answer is > '))
        guess_count = 1

        while the_answer != x + y:
            if the_answer > x + y:
                print('The guess was too high!')
                the_answer = int(input('Try again > '))
            elif the_answer < x + y:
                print('The guess was too low!')
                the_answer = int(input('Try again > '))
            guess_count += 1

        print('Congratulations! You are very smart!')
        print('Number of guesses > ', guess_count)

    def rand_sub():
        x = random.randint(1, 100)
        print(' ', x)
        y = random.randint(1, 100)
        print('-', y)

        the_answer = int(input('And the answer is > '))
        guess_count = 1

        while the_answer != x - y:
            if the_answer > x - y:
                print('The guess was too high!')
                the_answer = int(input('Try again > '))
            elif the_answer < x - y:
                print('The guess was too low!')
                the_answer = int(input('Try again > '))
            guess_count += 1

        print('Congratulations! You are very smart!')
        print('Number of guesses > ', guess_count)

    while 1:
        print('MAIN MENU\n ----------\n 1) Adding Random Numbers\n 2) Subtracting Random Numbers\n 3) Exit')
        try:
            selection = int(input('Please choose one of the menu options > '))
            if selection == 1:
                rand_add()
            elif selection == 2:
                rand_sub()
            elif selection == 3:
                print('Thank you for playing! Ciao!')
                break

        except ValueError:
            continue


main()

# PSEUDOCODE
# Build two separate functions to either subtract or add random numbers
# Import random module
# Define variables for each random number
# Print either addition or subtraction of each number then ask user to provide answer
# While the answer is not correct the function diplays either too high or too low
# Each time the user provides an answer it is tabulated
# Once the user provides the correct answer the loop is exited and the number of answers they gave is provided
# A menu is created to move the user through the program
# Selection 1 calls the rand_add function
# Selection 2 calls the rand_sub function
# Selection 3 breaks the loop and exits the program
