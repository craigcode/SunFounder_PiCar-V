from flask import Flask
from driver import stream
import picar

app = Flask(__name__)

#print stream.restart()

picar.setup()
db_file = "/home/pi/SunFounder_PiCar-V/remote_control/remote_control/driver/config"
fw = front_wheels.Front_Wheels(debug=False, db=db_file)
bw = back_wheels.Back_Wheels(debug=False, db=db_file)

#cam = camera.Camera(debug=False, db=db_file)
#cam.ready()

bw.ready()
fw.ready()

SPEED = 60
bw_status = 0

@app.route('/run')
def run(request):
	global SPEED, bw_status
	debug = ''

	if 'action' in request.GET:
		action = request.GET['action']
		# ============== Back wheels =============
		if action == 'bwready':
			bw.ready()
			bw_status = 0
		elif action == 'forward':
			bw.speed = SPEED
			bw.forward()
			bw_status = 1
			debug = "speed =", SPEED
		elif action == 'backward':
			bw.speed = SPEED
			bw.backward()
			bw_status = -1
		elif action == 'stop':
			bw.stop()
			bw_status = 0

		# ============== Front wheels =============
		elif action == 'fwready':
			fw.ready()
		elif action == 'fwleft':
			fw.turn_left()
		elif action == 'fwright':
			fw.turn_right()
		elif action == 'fwstraight':
			fw.turn_straight()
		elif 'fwturn' in action:
			print "turn %s" % action
			fw.turn(int(action.split(':')[1]))
		
	if 'speed' in request.GET:
		speed = int(request.GET['speed'])
		if speed < 0:
			speed = 0
		if speed > 100:
			speed = 100
		SPEED = speed
		if bw_status != 0:
			bw.speed = SPEED
		debug = "speed =", speed
	
    #host = stream.get_host().split(' ')[0]
	
    #return render_to_response("run.html", {'host': host})

return 'OK'


@app.route('/')
def hello_world():
    return 'She carried a Raspberry Flask'

@app.route('/stream-start')
def stream_start():
    print stream.restart()
    return 'Video stream started'

@app.route('/stream-stop')
def stream_stop():
    print stream.stop()
    return 'Video stream stopped'

@app.route('/connection-test')
def connection_test():
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
