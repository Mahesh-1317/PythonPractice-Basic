class MyZeroDivisionError(ZeroDivisionError):
    pass

def division(mine):
    if mine:
        raise MyZeroDivisionError("some worse news")
    else:
        raise MyZeroDivisionError("some bad news")
    
division(False)