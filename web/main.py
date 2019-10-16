from flask import Flask
from flask import url_for
from flask import request
from flask import render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Index Page</h1> <h2><a href="hello">Continuesss</a><h2>'

@app.route('/hello/')
@app.route('/hello/<name>')

def hello(name=None):
    url_for('static', filename='style.css')
    return render_template('hello.html', name=name)

@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['projectFilepath']
    projectpath = "<h1>Your data entry was <b>"+ projectpath +"</b>.</h1>"
    projectpath = projectpath+"<h2>Thx<h2>"
    return(projectpath)
    
    
if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
# [END gae_flex_python_static_files]