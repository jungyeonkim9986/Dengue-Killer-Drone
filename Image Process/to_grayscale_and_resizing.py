from PIL import Image
import os

dirpath='/Users/kimjuhwan/Desktop/Nonpuddle/'
img_list = os.listdir(dirpath)
for i in img_list:
    if not i.endswith('.jpg'):
        img_list.remove(i)
#print(nonpuddle_img_list)

j=1
for i in img_list:
    image = Image.open(dirpath + i).convert('L')
    resized = image.resize((256, 256))
    resized.save('/Users/kimjuhwan/Desktop/nonpuddle-gray2/' + str(j) + '.jpeg')
    j+=1
