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
            print(lst, hasIden)
            isFizz = (number % 3 == 0 or has3)
            isBuzz = (number % 5 == 0 or has5)
            isDelux = (number >  10 and hasIden)

            if (isFizz and isBuzz and isDelux):
                return "fizz buzz delux"
            elif (isFizz and isBuzz):
                return "fizz buzz"
            elif (isFizz  and isDelux):
                return "fizz delux"
            elif ( isBuzz and isDelux  ):
                return 'delux buzz'
            elif (isFizz):
                return 'fizz'
            elif (isBuzz):
                return 'buzz'
            elif (isDelux):
                return 'delux'

            else:
                return number
        else:
            return number

if __name__ == '__main__':
    test = fizz_buzz(3333)
    print(test)



