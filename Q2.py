def check_palindrome():
    """
    Runs through all 6-digit numbers and checks the mentioned conditions.
    The function prints out the numbers that satisfy this condition. 
   
    Note: It should print out the first number (with a palindrome in its last 4 digits), 
    not all 4 "versions" of it.
    """
    for i in range(100000,1000000):
        str_num = str(i)
        str_num = str_num[2:]
        if palindrome_test(str_num):
            str_num = str(i+1)
            str_num = str_num[1:]
            if palindrome_test(str_num):
                str_num = str(i+2)
                str_num = str_num[1:5]
                if palindrome_test(str_num):
                    str_num = str(i+3)
                    if palindrome_test(str_num):
                        print(i)

def palindrome_test(pali):
    """
    Recieves a string and tests if its a palindrome 
    Returns true or false
    """
    new = pali[::-1]
    return pali==new

check_palindrome()