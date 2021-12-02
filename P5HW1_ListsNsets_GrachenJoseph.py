# List collection, judgement, and verdict
# 11/07/2021
# CTI-110 P5HW1 - Lists and Sets
# Joseph Grachen
# 


def the_collector():
    num_list = []
    for x in range(1, 11):
        num = float(input('Enter number ' + str(x) + ' > '))
        num_list.append(num)

    return num_list


def the_judge(num_list):
    small = min(num_list)
    large = max(num_list)
    _sum = sum(num_list)
    average = '{:.1f}'.format(_sum / len(num_list))

    return [small, large, _sum, average]


def the_answer(collected: list, judged: list):
    # Displays the collected list
    print('Created list > ', collected)
    # Displays the results from the_judge
    print('Smallest number in the list > ', judged[0])
    print('Largest number in the list > ', judged[1])
    print('Sum of the numbers in the list > ', judged[2])
    print('Average of the numbers in the list > ', judged[3])
    # Converts the list to a set
    collected_set = set(collected)
    # Displays the created set
    print(collected_set)


collected = [0]
judged = [0, 0, 0, 0]

while 1:
    print('-----MENU-----\n 1) Create List\n 2) Display Results\n 3) Exit\n ---------------')
    try:
        selection = int(input('Make selection > '))
        if selection == 1:
            collected = the_collector()
            judged = the_judge(collected)
        elif selection == 2:
            the_answer(collected, judged)
        elif selection == 3:
            break

    except ValueError:
        continue


# PSEUDOCODE
# Create a function to collect 10 number from user
# Append each input to the end of the list being created
# Create another function to judge the list which was input
# The judgement will be the smallest, largest, sum, and average of the numbers in the list
# Create a final function to print the list, the judgement of it, and the conversion to a set
# Create a menu driven display
# The display asks the user to input numbers for the list then displays the answer of judgement with an input
