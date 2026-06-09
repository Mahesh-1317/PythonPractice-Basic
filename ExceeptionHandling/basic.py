def devide(n):
    try:
        n = 1/n
    except ZeroDivisionError:
        print("Andha h kya")
        return None
    else:
        print("Everything is fine")
        return n
    
print(devide(5))
print()
print(devide(0))