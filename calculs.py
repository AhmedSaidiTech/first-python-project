def addition (a,b) :
    return a+b
def soustraction(a,b):
    return a-b
def multiplication (a,b):
    return a*b
def division (a,b) :
    try :
        return a / b 
    except ZeroDivisionError :
        print("le 2 eme argument argument doit etre non nulle !")
