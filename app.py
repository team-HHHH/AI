from flask import Flask, request
from service import ImageProcessService
from OurOCR import init

def create_app():
    app = Flask(__name__)
    init()

    @app.route('/process',methods=['POST'])
    def image_process():
        image = request.files['image']
        image_json = ImageProcessService.process(image, image.filename)
        return image_json

    return app
