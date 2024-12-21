from PIL import Image, ImageFilter, ImageFont, ImageDraw
from img.ImageHandler import ImageHandler
from img.ImageProcessor import ImageProcessor

def main():
    image = ImageHandler('image_2.jpg')
    
    image.turn(90)
    image.pruning((150, 150))

    image_processor = ImageProcessor(image)

    image_processor.black()
    image_processor.add_text("Вариант 2", (0, 0), font_size=20, font_color="pink") 
    image_processor = image
    image.save('result_image.jpg')

main()