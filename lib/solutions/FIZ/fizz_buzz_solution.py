# noinspection PyUnusedLocal
def fizz_buzz(number):
        print(number % 10,)
        if number >=1 and number <= 9999:
            if (number % 3 == 0 or number // 10 == 3) and (number % 5 == 0 or number // 10 == 5):
                return "fizz buzz"
            if number % 3 == 0 or number // 10 == 3:
                return 'fizz'
            elif number % 5 == 0 or number // 10 == 5:
                return 'buzz'

            else:
                return number
        else:
            return number

if __name__ == '__main__':
    test = fizz_buzz(75)
    print(test)







