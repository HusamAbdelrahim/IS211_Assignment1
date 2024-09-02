#assignment1_part1

def list_divide(numbers, divide=2): #we created a function called list_divide and then what we did was take two parameters which is numbers, and divide with a value of 2
    count = 0
    for i in numbers: # using the loop method to go over the number and check inside
        if i % divide == 0: # 
            count += 1 # if true it will return the value of 1
    return count # using return will reutrn us the result of "count"

class ListDivideException(Exception): #using the class function to contain the information regarding ListDivideException
    pass

def test_list_divide():
    try: #using assert to check the test and the results of the outcome 
        assert list_divide([1, 2, 3, 4, 5]) == 2 
        assert list_divide([2, 4, 6, 8, 10]) == 5
        assert list_divide([30, 54, 63, 98, 100], divide=10) == 2
        assert list_divide([]) == 0
        assert list_divide([1, 2, 3, 4, 5], 1) == 5
    except AssertionError: #If one of the test statement because false then it will raise an error
        raise ListDivideException("A test in test_list_divide failed.")


# run prog
if __name__ == "__main__":
    test_list_divide()
