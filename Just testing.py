def list_divide(numbers, divide = 2):
    count = 0
    if len (numbers) == 0:
        return 0
    for i in numbers:
        try:
            if i % divide == 0:
                count += 1
        except:
            return 'Error: List_DivideException'
        return count
    
    def test_list_divide():
        print (list_divide)([1,2,3,4,5])
        print (list_divide)([2,4,6,8,10])
        print (list_divide)([30, 54, 63,98, 100], divide=10)
        print (list_divide)([])
        print (list_divide)([1,2,3,4,5], 1)

    test_list_divide