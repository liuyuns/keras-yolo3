

from PIL import Image

from io import BytesIO
import base64
import re

def get_image(format, data):
    if format == 'base64':
        image_data = re.sub('^data:image/.+;base64,', '', data)
        image = Image.open(BytesIO(base64.b64decode(image_data)))
        return image
    if format == 'fs':
        image = Image.open(data)
        return image
    
    return None

