from flask import Flask, render_template, request, redirect, url_for

import os


app = Flask(__name__)

# Set upload folder
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure the folder exists
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return redirect(url_for('home'))

    image = request.files['image']
    if image.filename == '':
        return redirect(url_for('home'))

    # Save the uploaded image to the upload folder
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    image.save(image_path)

    # Render the image on the webpage
    return render_template('index.html', uploaded_image=url_for('static', filename=f'uploads/{image.filename}'))



@app.route('/about')
def about():
    return render_template('brain_tumor.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')



if __name__ == "__main__":
    app.run(port=5001, debug=True)

