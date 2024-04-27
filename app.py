from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from PIL import Image
import numpy as np
import os


def resize_image(img, ratio):
    # Resize the image by the given ratio
    return img.resize((img.width // ratio, img.height // ratio))


def image_to_ascii(img_array, shader):
    result = ''
    shader = list(shader)[::-1]  # Reverse the shader list (light to dark)
    print(shader)
    max_pixel_value = 255  # Assuming 8-bit grayscale
    for row in img_array:
        for pixel in row:
            fraction = pixel / max_pixel_value
            # Calculate the index in the shader list
            index = int(fraction * (len(shader) - 1))
            result += shader[index]
        result += '\n'
    return result


app = Flask(__name__)
bootstrap = Bootstrap(app)


app.config['UPLOAD_FOLDER'] = 'flask-uploads'

default_shader = "#. "


@app.route('/', methods=['GET'])
def home():

    return render_template('home.html')


@app.route('/result', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return 'No file part'

    image = request.files['image']
    if image.filename == '':
        return 'No selected file'

    img = Image.open(image)

    img = img.convert('L')  # Convert to grayscale

    # Get optional parameters
    shader = request.form.get('asciiChars', '')
    if shader == '':
        shader = default_shader
    else:
        shader = shader.replace(' ', '')
        shader += ' '

    pixel_ratio = int(request.form.get('pixelRatio', 1))
    img_resized = resize_image(img, pixel_ratio)
    img_resized.save(os.path.join(
        app.config['UPLOAD_FOLDER'], image.filename+'_resized.jpg'))

    img_array = np.array(img_resized)

    asciified = image_to_ascii(img_array, shader)

    return render_template('result.html', asciified=asciified, shader=shader, pixel_ratio=pixel_ratio)


if __name__ == '__main__':
    app.run(debug=True)
