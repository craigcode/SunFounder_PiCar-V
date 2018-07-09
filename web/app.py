from flask import Flask
from driver import stream

app = Flask(__name__)

#print stream.restart()

@app.route('/')
def hello_world():
    return 'She carried a Raspberry Flask'

@app.route('/stream-start'):
    print stream.restart()
    return 'Video stream started'

@app.route('/stream-stop'):
    print stream.stop()
    return 'Video stream stopped'

@app.route('/connection-test'):
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
