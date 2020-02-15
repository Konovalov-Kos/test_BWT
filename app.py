from flask import Flask, render_template
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return 'home'

if __name__ == '__main__':
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
    # app.run(debug=True)
