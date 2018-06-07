from binanalyzer import app
from flask import render_template, request
from binanalyzer.models.File import File
import json

ALLOWED_EXTENSIONS = ['doc', 'docx', 'exe']


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=["GET", "POST"])
def file_uploader():
    if request.method == 'POST':
        if "upload" not in request.files:
            return
        file = request.files["upload"]
        if file.filename == "":
            return "Invalid file"
        if file and allowed_file(file.filename):
            file_obj = File(file)
            if file_obj.upload():
                data = json.loads(file_obj.process_file())
                if data:
                    info = {}
                    index = 0;
                    for item in reversed(sorted(data['message'],key=len)):
                        if index > 200:
                            continue
                        info[item] = "".join([" %02x" % ord(c) for c in item])
                        index += 1
                    return render_template("analyzer/analysis.html", result = info)
                else:
                    return "error"
    return render_template('uploader/index.html')

