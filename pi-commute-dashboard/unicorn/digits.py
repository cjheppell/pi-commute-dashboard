def get(digit):
    if digit == '1':
        return one()
    if digit == '2':
        return two()
    if digit == '3':
        return three()
    if digit == '4':
        return four()
    if digit == '5':
        return five()
    if digit == '6':
        return six()
    if digit == '7':
        return seven()
    if digit == '8':
        return eight()
    if digit == '9':
        return nine()
    if digit == '0':
        return zero()
    
    raise Exception('{0} was not a digit'.format(digit))

def one():
    return  [
                [0,1,0],
                [0,1,0],
                [0,1,0],
                [0,1,0],
                [0,1,0],
            ]

def two():
    return  [
                [1,1,1],
                [0,0,1],
                [1,1,1],
                [1,0,0],
                [1,1,1],
            ]

def three():
    return  [
                [1,1,1],
                [0,0,1],
                [1,1,1],
                [0,0,1],
                [1,1,1],
            ]

def four():
    return  [
                [1,0,1],
                [1,0,1],
                [1,1,1],
                [0,0,1],
                [0,0,1],
            ]

def five():
    return  [
                [1,1,1],
                [1,0,0],
                [1,1,1],
                [0,0,1],
                [1,1,1],
            ]

def six():
    return  [
                [1,1,1],
                [1,0,0],
                [1,1,1],
                [1,0,1],
                [1,1,1],
            ]

def seven():
    return  [
                [1,1,1],
                [0,0,1],
                [0,0,1],
                [0,0,1],
                [0,0,1],
            ]

def eight():
    return  [
                [1,1,1],
                [1,0,1],
                [1,1,1],
                [1,0,1],
                [1,1,1],
            ]

def nine():
    return  [
                [1,1,1],
                [1,0,1],
                [1,1,1],
                [0,0,1],
                [0,0,1],
            ]

def zero():
    return  [
                [1,1,1],
                [1,0,1],
                [1,0,1],
                [1,0,1],
                [1,1,1],
            ]