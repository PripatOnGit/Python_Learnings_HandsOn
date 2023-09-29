def myfunc(a):
    print(a)

myfunc(6)

#==================================
def myfunc1(*args):
    print(*args)

myfunc1(1,3,5,7,9)

#===================================

def myfunc2(**kwargs):
    print(f"value is: {kwargs['veggie']}")

myfunc2(veggie='lady finger')


