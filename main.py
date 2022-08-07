from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Mao")

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        save_path = os.path.join(r"~/upload", secure_filename(f.filename))
        f.save(save_path)
        f.close()
        return redirect('/upload')
    return render_template('upload.html')


if __name__ == '__main__':
    app.run('127.0.0.1', 5000)
