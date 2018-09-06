from flask import render_template, request

from binanalyzer import app
from binanalyzer.models.File import File

ALLOWED_EXTENSIONS = ['doc', 'docx', 'exe', 'bin']


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=["GET", "POST"])
def file_uploader():
    if request.method == 'POST':
        if "upload" not in request.files:
            return
        file = request.files["upload"]
        #should be moved to model to validate
        if file.filename == "":
            return "Invalid file"
        if file and allowed_file(file.filename):
            file_obj = File(file)
            data = file_obj.upload()
            if data:
                return render_template("analyzer/analysis.html", result=data)
            else:
                return "error"
    return render_template('uploader/index.html')
