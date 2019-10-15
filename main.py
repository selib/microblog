from flask import Flask
from flask import url_for
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Index Page</h1> <h2><a href="hello">Continue</a><h2>'

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
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_flex_python_static_files]