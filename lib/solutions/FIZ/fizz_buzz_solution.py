# noinspection PyUnusedLocal
def fizz_buzz(number):

        if number >=1 and number <= 9999:
            lst = [int(i) for i in str(number)]
            has3 = False
            has5 = False
            hasIden = False
            for i in lst:
                if i == 3:
                    has3 = True
                elif i == 5:
                    has5 = True
                elif lst[0] == i:
                    hasIden = True
            if (number % 3 == 0 or has3) and (number % 5 == 0 or has5) and (number >  10 and hasIden):
                return "fizz buzz Delux"
            if (number % 3 == 0 or has3  ) and (number % 5 == 0 or has5):
                return "fizz buzz"
            if (number % 3 == 0 or has3  ):
                return 'fizz'
            elif (number % 5 == 0 or has5):
                return 'buzz'
            elif (number >  10 and hasIden):
                return 'Delux'

            else:
                return number
        else:
            return number

'''if __name__ == '__main__':
    test = fizz_buzz(9999)
    print(test)'''
