from flask import Flask
from driver import stream

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'She carried a Raspberry Flask'

if __name__ == '__main__':
    print stream.start()
    app.run(debug=True,host='0.0.0.0')
