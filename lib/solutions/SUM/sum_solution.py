# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):


    try:
        if (x >= 0 and x <= 100) and (y >= 0 and y <= 100):
            return x+y
        else :
            return (f"Values are out of range")
    except Exception as e:
        return e


'''if __name__ == '__main__':
    sum = compute(2,3)
    print(sum)'''
