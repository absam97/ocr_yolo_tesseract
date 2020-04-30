from flask import Flask, render_template, request, session, url_for, redirect, stream_with_context, Response
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import os
from generate_text_region import generate_text_region
from read_text import generated_text
import pytesseract

#Only for Windows after installing tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'

model_path = 'training_data/detection_model-ex-009--loss-0003.916.h5'
json_path = 'training_data/detection_config.json'


app = Flask(__name__)
dropzone = Dropzone(app)

# Dropzone settings
app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'
app.config['DROPZONE_REDIRECT_VIEW'] = 'results'

# Uploads settings

app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/uploads'
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB

app.config['SECRET_KEY'] = 'supersecretkeygoeshere'



@app.route('/', methods=['GET', 'POST'])
def index():
    
    # set session for image results
    if "file_urls" not in session:
        session['file_urls'] = []
    # list to hold our uploaded image urls
    file_urls = session['file_urls']
    # handle image upload from Dropzone
    if request.method == 'POST':
        file_obj = request.files
        for f in file_obj:
            file = request.files.get(f)
            
            # save the file with to our photos folder
            filename = photos.save(
                file,
                name=file.filename    
            )
            # append image urls
            file_urls.append(photos.url(filename))
            
        session['file_urls'] = file_urls
        return "uploading..."
    # return dropzone template on GET request    
    return render_template('ocr.html')

@app.route('/results')
def results():
    
    # redirect to home if no images to display
    #if "file_urls" not in session or session['file_urls'] == []:
    #    return redirect(url_for('index'))
        
    # set the file_urls and remove the session variable
    #file_urls = session['file_urls']
    #session.pop('file_urls', None)
    result = generate()
    return render_template("results.html", result = result)
    
    #return render_template('results.html',file_urls=file_urls)
    #return Response(stream_template('results.html', data=generate()))


def generate():
    image_name = os.listdir('uploads/')[0]
    _, object_path_arr = generate_text_region(model_path, json_path, 'uploads/' + image_name, 'text_detected')
    text = generated_text()
    os.remove('deskewed_fin.jpg')
    os.remove('processed_fin.jpg')
    os.remove('text_detected-objects/licence-00000.jpg')
    os.rmdir('text_detected-objects')
    for f in os.listdir('uploads/'):
        os.remove('uploads/' + f)
    return text

def main():
    index()
    results()

if __name__=="__main__":
    app.run(debug = True, host="0.0.0.0", port = 80, threaded=False)
