
from PIL import ImageDraw

def mark_image(image, objects):

    draw = ImageDraw.Draw(image)

    rectBox = ['left', 'top', 'right', 'bottom']

    for object in objects:
        box = object["box"]
        rect = list(map(lambda k: box.get(k), rectBox))
        draw.rectangle(rect, outline=(0, 181, 0))
        
    image.show()


