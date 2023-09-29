#handling binary data
f1 = open("image.jpg",'rb')
f2 = open("newpic.jpg",'wb')
bytes = f1.read()
f2.write(bytes)
print("new image is available with name newpic.jpg")