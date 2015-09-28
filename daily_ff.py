from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/week/<week_id>')
def schedule(week_id):
    return 'Schedule for week {}'.format(week_id)

if __name__ == '__main__':
    app.run()