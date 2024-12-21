from PIL import Image, ImageFilter, ImageFont, ImageDraw
from img.ImageHandler import ImageHandler

class ImageProcessor():
    def __init__(self, image_handler):
        self.image_handler = image_handler

    def black(self): 
        self.image_handler.img = self.image_handler.img.convert('L')


    def add_text(self, text, position, font_size=12, font_color="black"): 
        draw = ImageDraw.Draw(self.image_handler.img) 
        font = ImageFont.truetype('arial.ttf', font_size)
        draw.text(position, text, font=font, fill=font_color)