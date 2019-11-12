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
            for j in lst:
               if(j == lst[0]):
                   hasIden = True
               else:
                    hasIden = False
                    break

            isFizz = (number % 3 == 0 or has3)
            isBuzz = (number % 5 == 0 or has5)
            isDelux = (number >  10 and hasIden)

            print(isDelux)

            if(isDelux and (number % 2 != 0)):
                isOdd = True
            else:
                isOdd = False
            if (isFizz and isBuzz):
                if(isOdd and isDelux):
                    return "fizz buzz fake deluxe"
                else:
                    return "fizz buzz deluxe"
            elif (isFizz and isBuzz):
                return "fizz buzz"
            elif (isFizz):
                if (isOdd and isDelux):
                    return "fizz fake deluxe"
                else:
                    return "fizz deluxe"
            elif ( isBuzz):
                if(isOdd and isDelux):
                    return 'buzz fake deluxe'
                else:
                    return 'buzz deluxe'
            elif (isDelux):
                if(isOdd):
                    return 'fake deluxe'
                else:
                    return 'deluxe'
            elif (isFizz):
                return 'fizz'
            elif (isBuzz):
                return 'buzz'


            else:
                return number
        else:
            return number

if __name__ == '__main__':
    test = fizz_buzz(550)
    print(test)





