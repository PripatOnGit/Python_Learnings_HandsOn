def statusOfNumbers(a,b):
    if(a%2==0 and b%2==0):
        if(a>b):
            print(b)
        else:
            print(a)
    else:
        print(a)
    
statusOfNumbers(2,5)

#===============================================================================

def animal_cracker(str):
    ls = str.split()
    a = ls[0][0]
    b = ls[1][0]
    if(a==b):
        print("Starts with same letter")
        return True
    else:
       print("Diff letters")
       return False

animal_cracker("Lavanya Lagoon")