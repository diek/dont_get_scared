def is_valid_int(test_value):
    ''' (string) -> Boolean

    tests input for a int, returns true if integer, otherwise False.
    '''
    check = isinstance(test_value, int)
    return(check)
    """ try:
        int(test_value)
        return True

    except ValueError:
        return False """


def small_large():
    ''' 5.2 Write a program that repeatedly prompts a user for integer numbers
    until the user enters 'done'.Once 'done' is entered, print out the largest
    and smallest of the numbers. If the user enters anything other than a valid
    number catch it with a try/except and put out an appropriate message and
    ignore the number. Enter the numbers from the book for problem 5.1 and
    Match the sample output below.

    Invalid input
    Maximum is 7
    Minimum is 4
    '''
    largest = None
    smallest = None
    flag1 = 1
    first_rec = 1
    while (flag1):
        num = input("Enter a number: ")

        if num == "done":
            flag1 = 0
        else:
            cond1 = is_valid_int(int(num))
            if first_rec and cond1:
                ## initialize with first value input
                smallest = int(num)
                largest = int(num)
                first_rec = 0

            elif cond1:
                num = int(num)
                if num < smallest:
                    smallest = num
                elif num > largest:
                    largest = num
                else:
                    print('Invalid input')
            else:
                print('Invalid input')
    return([largest, smallest])

# Make the call
result_set = small_large()
print("Maximum is ", result_set[0])
print("Minimum is ", result_set[1])
