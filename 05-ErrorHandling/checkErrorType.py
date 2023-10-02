try:
    a="Hello"+20
    x=int(input("Enter first number:"))
    y=int(input("Enter second number:"))
    print(x/y)
except (ZeroDivisionError,ValueError,TypeError) as msg:
    print(msg.__class__,msg)


#====================================================

try:
    # Your code that might cause an exception
    # For example:
    x = 1 / 0
except Exception as e:
    # Print the exception message
    print(f"An exception occurred: {str(e)}")