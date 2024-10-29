import os

import OurOCR
import tempfile

def process(image, image_name):
    suffix = get_suffix(image_name)
    tmp = tempfile.NamedTemporaryFile(mode='w+b', delete=False, dir= 'images',suffix=suffix)

    try:
        tmp.write(image.read())
        tmp.flush()
        json = OurOCR.ocrToGPTAPI(tmp.name)
    finally:
        tmp.close()

    os.remove(tmp.name)
    return json

def get_suffix(image_name):
    _, suffix = os.path.splitext(image_name)
    return suffix