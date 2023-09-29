from PIL import Image
#open image
mac = Image.open('image.jpg')

#type of image
print(type(mac))

#show image
#mac.show()
#size
mac.size

mac.format_description

mac.crop((0,0,100,100))
mac.show()