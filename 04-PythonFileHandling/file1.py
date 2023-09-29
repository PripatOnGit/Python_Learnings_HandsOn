with open("file.txt",'r+') as f:
    print(f"file name: {f.name}")
    print("file mode", f.mode)
    print("is file readable: ",f.readable())
    print("is file writable: ",f.writable())

    #f.write("I am Priynka\n")
    ls = ["sunny\n","munny\n","chinny\n","bunny\n"]
    f.writelines(ls)

    lines = f.readlines()
    for line in lines:
        print(line, end='*')

    f.close()
    print("file closed?",f.closed)