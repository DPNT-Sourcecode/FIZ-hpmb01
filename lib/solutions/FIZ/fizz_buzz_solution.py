# noinspection PyUnusedLocal
def fizz_buzz(number):
        has3 = False
        has5 = False
        hasIden = False
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

            print(hasIden)


            isFizz = (number % 3 == 0 or has3)
            isBuzz = (number % 5 == 0 or has5)
            isDelux = (number >  10 and hasIden)

            if (isFizz and isBuzz and isDelux):
                return "deluxe fizz buzz "
            elif (isFizz and isBuzz):
                return "fizz buzz"
            elif (isFizz  and isDelux):
                return "fizz deluxe"
            elif ( isBuzz and isDelux  ):
                return 'deluxe buzz'
            elif (isDelux):
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
    test = fizz_buzz(222)
    print(test)
