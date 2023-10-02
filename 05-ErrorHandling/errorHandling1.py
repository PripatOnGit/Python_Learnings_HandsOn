try:
    # Code that may raise exceptions
    x = int("abc")  # This may raise a ValueError or a TypeError
except Exception as e:
    # Check the type of the exception
    if isinstance(e, ValueError):
        print("Caught a ValueError")
    elif isinstance(e, TypeError):
        print("Caught a TypeError")
    else:
        print("Caught another type of exception")