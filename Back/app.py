from plot_chart import plotChart
from flask import Flask, jsonify, send_file, request
from flask_cors import CORS

import os


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

#We can change this to POST method once we have input from vue
@app.route('/chart', methods=['GET'])
def get_chart():
    return send_file('.\charts\RGBSG_BITES.jpg', mimetype='image/jpg')

@app.route('/loadChart', methods=[ 'POST'])
def load_chart():
    if request.method == 'POST':
        post_data = request.get_json()
        plotChart(post_data.get('choice'))
        response_object = {'status': 'success'}
        response_object['message'] = 'Loaded!'
        response_object['imageURL'] = 'chart'
        return jsonify(response_object)

@app.route('/datafile', methods=['GET'])
def get_datafile():
    return send_file('.\data\RGBSG\\rgbsg.h5')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)
    if(port!=5000):
        app.run(debug=False, port=port, host='0.0.0.0')
    else:
        app.run()