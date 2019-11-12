# noinspection PyUnusedLocal
def fizz_buzz(number):
        has3 = False
        has5 = False
        hasIden = False
        isOdd = False
        if number >=1 and number <= 9999:
            lst = [int(i) for i in str(number)]

            for i in lst:
                if i == 3:
                    has3 = True
                elif i == 5:
                    has5 = True

            # check whether the number is identical
            '''for j in lst:
               if(j == lst[0]):
                   hasIden = True
               else:
                    hasIden = False
                    break'''

            isDevisibleBy3 = (number % 3 == 0)
            isDevisibleBy5 = (number % 5 == 0)
            isFizz =  isDevisibleBy3 or has3
            isBuzz = isDevisibleBy5 or has5
            isDelux = ((isDevisibleBy3 and has3) or (isDevisibleBy5 and has5))

            # check whether the number is odd
            if(number % 2 != 0):
                isOdd = True

            if (isFizz and isBuzz and isDelux):
                if isOdd:
                    return "fizz buzz fake deluxe"
                else:
                    return "fizz buzz deluxe"
            elif (isFizz and isBuzz):
                return "fizz buzz"
            elif (isFizz and isDelux):
                if isOdd:
                    return "fizz fake deluxe"
                else:
                    return "fizz deluxe"
            elif (isBuzz and isDelux):
                if isOdd:
                    return 'buzz fake deluxe'
                else:
                    return 'buzz deluxe'
            elif (isDelux):
                if isOdd:
                    return 'fake deluxe'
                else:
                    return 'deluxe'
            elif isFizz:
                return 'fizz'
            elif isBuzz:
                return 'buzz'
            else:
                return number
        else:
            return number

if __name__ == '__main__':
    test = fizz_buzz(243)
    print(test)





