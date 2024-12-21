from flask import Flask, request, render_template, send_file
from PIL import Image
import os
import io

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # Limit file size to 5 MB

# Ensure the uploads directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compress', methods=['POST'])
def compress_image():
    try:
        # Get the uploaded image and quality
        file = request.files['image']
        quality = int(request.form['quality'])

        # Open the image
        image = Image.open(file)

        # Convert RGBA to RGB if necessary
        if image.mode == 'RGBA':
            image = image.convert('RGB')

        # Compress and save the image
        output = io.BytesIO()
        image.save(output, format="JPEG", quality=quality)
        output.seek(0)

        # Return the compressed image
        return send_file(output, mimetype='image/jpeg', as_attachment=True, download_name='compressed.jpg')

    except Exception as e:
        return f"Error: {str(e)}", 400

if __name__ == '__main__':
    app.run(debug=True)
