def sum_of_two_digits(first_digit, second_digit):
    return first_digit + second_digit


if __name__ == '__main__':
# It Allows You to Execute Code When the File Runs as a Script, but Not When Its Imported as a Module
    a, b = map(int, input().split()) 
    # map returns a list of the results after applying the given function to each item of a given iterable (here converting every element from the output of split to an int ) 
    # will query the user for input, and then split it into words, 
    # convert these words in integers
    # and unpack it into two variables a and b. 
    # This thus will succeed when the user enters two numbers (not more, not less).
    print(sum_of_two_digits(a, b))
