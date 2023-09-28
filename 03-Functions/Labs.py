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

#given list check if 3 is present before any 3

list10 = [1,3,3,5,6,3,3]
for i in range(len(list10)):
    if list10[i:i+1] == [3,3]:
        print(i," ",i+1)



#===============================================================
## map function

#create normal function 
def myfunc(a):
    return (a**2)

ls = [1,2,3,4,5]
 
for item in map(myfunc,ls):
    print(item)


#=================================================================

#create list of even numbers using map function and given list

def check_even(num):
    if (num%2==0):
        return num
    else:
        pass

ls = [1,5,7,9,3,4,6,2,9,10,45,77,146,39,6752,67873,275082758250]

even_list = list(filter(check_even,ls))
print(even_list) 



#=================================

#lambda function
def sqaure(num):
    return num**2

#lambda

sq = lambda num : num ** 2 
print(f"sq is: {sq(5)}")

#==================================

def myfunc(a):
    return (a**2)

ls = [1,2,3,4,5]
 
sq_list = list(map(myfunc, ls))
print(sq_list)

#===========================================================================
#count number of uppercase letters and lowercase letters

str = "How many LoweCase Letters and Uppercase letters are there in String"
def count(str):
    u_count = 0
    l_count = 0
    for ch in str:
        if(ch.isupper()):
            u_count +=1
        elif(ch.islower()):
            l_count +=1
        else:
            pass

    print(f"Uppercase letters: {u_count}")
    print(f"Lowercase letters: {l_count}")

count(str)

#=======================================================
#using dictionary

str = "How many LoweCase Letters and Uppercase letters are there in String"
def count(str):
    d = {'u_count': 0, 'l_count' : 0}
    for ch in str:
        if(ch.isupper()):
            d['u_count'] +=1
        elif(ch.islower()):
            d['l_count'] +=1
        else:
            pass

    print(f"Uppercase letters: {d['u_count']}")
    print(f"Lowercase letters: {d['l_count']}")

count(str)

#=======================================================================

#find unique elements from list

ls = [1,3,4,5,2,3,8,4,5,2,9,1,7,3,9]

seen_num_list = []
def unique_list(lst):
    for num in lst:
        if num not in seen_num_list:
            seen_num_list.append(num)
        else:
            pass
    return seen_num_list

unique_list = unique_list(ls)
print(unique_list)


#==============================================

#multiply all numbers in list

ls = [1,2,3,4,5]
prod = 1
for num in range(len(ls)):
    prod = prod * ls[num]

#================================================
#word is pallindrom or not
flag = True
def check_pallindrom(str):
    for ch in range(0,int(len(str)/2)):
        if(str[ch] == str[len(str)-ch-1]):
            flag = True
        else:
            flag = False

    if(flag == True):
        print("Pallindrom")
    else:
        print("Not a pallindrom")

check_pallindrom("anna")




























