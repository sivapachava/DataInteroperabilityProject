import base64
# encode image to base64
with open('photo.png', 'rb') as imagefile:
    byteform = base64.b64encode(imagefile.read())

f=open('output.bin','wb')
f.write(byteform)
f.close()

# decode base64 to image
file = open('output.bin', 'rb')
byte = file.read()
file.close()

fh = open('find.png', 'wb')
fh.write(base64.b64decode((byte)))
fh.close()



