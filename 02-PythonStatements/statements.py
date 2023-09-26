st  = 'Print only the words that start with s in this sentence'
ls = st.split()
print(ls)
for letter in ls:
    if(letter[0] == 's'):
        print(letter)
    else:
        pass

#================================================================
st  = 'Print only the words that start with s in this sentence'
ls = st.split()
print(ls)
for letter in ls:
    if(letter.startswith('s')):
        print(letter)
    else:
        pass

#==========================================================
    
#Print all even numbers from 0-100
for num in range(0,100):
    if(num%2==0):
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

#==========================================================
num=0
while(num<100):
    if(num%2==0):
        print(f"{num} is Even")
        num+=1
    else:
        print(f"{num} is Odd")
        num+=1
#=======================================================
#List comprehention for printing all numbers between 0-50 which are divisible by 3

list_comp = [num for num in range(0,50) if num%3==0]
print(list_comp)

list2 = [num*2 for num in range(0,50) if num%3==0]
print(list2)


list3 = [x*2 if(x%2==0) else "Invalid" for x in range(0,10)] 
print(list3)

#=============================================================================

#print "even" if length of word is even in given string
str = "print the even if lenght of word is even"
list5 = str.split()
for letter in list5:
    if(len(letter)%2==0):
        print(f"{letter} is Even lenght")
    else:
       print(f"{letter} is odd lenght")

#==============================================================================
#using List Comprehention

list4 = ['even' if len(letter)%2==0 else "odd" for letter in str.split() ]
print(list4)

#===============================================================================
#Use list comprehention to create a list of the first letter of every word in the string

str = 'Create a list of the first letters of every word in this string.'
ls = []
list7 = [ls.append(letter[0]) for letter in str.split()]
print(ls)






