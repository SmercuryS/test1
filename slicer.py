def vertical(n,img):
    a = 0
    croper = img.height//n

    for i in range(n):
        img = Image.open('C:/croping/01.jpg')
        region = (0, a, img.width, croper+a)
        img = img.crop(region)
        img.save('C:/croping/0'+'0'+str(i+1)+'.jpg', "JPEG", quality=100)
        a += croper


def horizental(n,img):
    a = 0
    croper = img.height//n

    for i in range(n):
        img = Image.open('C:/croping/01.jpg')
        region = (a, 0, croper+a, img.height)
        img = img.crop(region)
        img.save('C:/croping/0'+'0'+str(i+1)+'.jpg', "JPEG", quality=100)
        a += croper

def main():
    import PIL
    from PIL import Image

    img = Image.open('C:/croping/01.jpg')

    print('finished')

#img.show()