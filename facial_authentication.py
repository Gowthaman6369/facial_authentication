from flask import Flask, render_template, request, jsonify
import base64
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/store_image', methods=['POST'])
def store_image():
    try:
        data = request.get_json()
        if 'image' in data:
            image_data = base64.b64decode(data['image'])
            image_path = os.path.join('stored_images', 'user_image.jpg')
            with open(image_path, 'wb') as f:
                f.write(image_data)
            return jsonify({'message': 'Image stored successfully'})
        else:
            return jsonify({'error': 'No image data received'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/success.html')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
