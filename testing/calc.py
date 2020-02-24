def add(x, y):
    '''add func'''
    return x + y

def substract(x, y):
    '''substract func'''
    return x - y

def multiply(x, y):
    '''multiply func'''
    return x * y

def divide(x, y):
    '''divide func'''
    if y == 0:
        raise ValueError('can not divide by zero')
    return x / y
