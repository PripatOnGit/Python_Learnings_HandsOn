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


#=================================================================================
def makes_twenty(a,b):
    return a==20 or b==20 or (a+b)==20

makes_twenty(20,40)

#=================================================================

#macdonals ----> MacDonals --> make first and fourth characters in uppercase

str ="macdonalds"
first_word = str[0].upper()
second_word = str[1:3]
third_word = str[3].upper()
last_part = str[4:]
print(first_word+second_word+third_word+last_part)

#================================================================================

first_part = str[0:3].capitalize()
second_part = str[3:].capitalize()

print(first_part+second_part)

#==============================================================================
#Reverse the statements

line = "I am home"
rev_line = line[::-1]
print(rev_line)

#================================================================================
def rev_string(line):
    ls = line.split()
    #print(ls)
    new_ls = []
    for item in ls:
        rev_word = item[::-1]
        new_ls.append(rev_word)
    #print(new_ls)

    rev_str = " ".join(new_ls)
    print(rev_str)
rev_string(line)
#==================================================================================


#To check if given number is within 10 of 100 or 200

def check_num():
    num = int(input("Enter number: "))
    if(abs(100-num) <=10 or abs(200-num)<=10):
        print(True)
    else:
        print(False)

check_num()

#=============================================================================
#print square of number
import math
def sq_num():
    num = int(input("Enter number for sqaure: "))
    if(num>0):
        sq = math.sqrt(num)
        print(sq)
    
sq_num()

#==============================================================================