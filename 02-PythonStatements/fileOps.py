#read file
with open('test.txt', 'r') as f:
    print(f.read())
    print(f.readline())
    print(f.readlines())
    f.close()


#write to file
with open ('test.txt', 'a') as f:
    f.write("\n I like coding")
    f.close()