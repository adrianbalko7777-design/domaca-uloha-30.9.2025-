from PIL import Image


pic = Image.open('les.jpg')
pixels = pic.load()
for y in range(pic.size[1]):
   for x in range(pic.size[0]):
       temp = pixels[x,y] #(343,151,155)
       pixels[x,y] = (temp[0],0,0)

pic.show()
