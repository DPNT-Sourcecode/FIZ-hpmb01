# noinspection PyUnusedLocal
def fizz_buzz(number):

        if number >=1 and number <= 9999:
            if number % 3 == 0 and number % 5 == 0:
                return 'fizz buzz'
            elif number % 3 == 0:
                return 'fizz'
            elif number % 5 == 0:
                return 'buzz'
            else:
                return number
        else:
            return number

'''if __name__ == '__main__':
    test = fizz_buzz(15)
    print(test)'''


