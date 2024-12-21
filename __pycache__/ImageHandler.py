from PIL import Image, ImageFilter, ImageFont, ImageDraw

class ImageHandler():
    def __init__(self, img):
        self.img = Image.open(img)
    
    def load(self):
        return self.img

    def save(self, img2):
        self.img.save(img2)

    def turn(self, pix):
        self.img = self.img.rotate(pix)

    def pruning(self, data):
        self.img = self.img.resize(data)


      