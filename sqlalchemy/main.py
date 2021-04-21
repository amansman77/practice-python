from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS

from entity import sql_db

from handler import VisualizerHandler

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://aiplatform:platformadmin@192.168.7.130:30432/platform_rms'
app.config['SQLALCHEMY_ECHO'] = True
app.config["MONGO_URI"] = "mongodb://aiplatform:platformadmin@192.168.7.130:30717/rawdata"

CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

sql_db.init_app(app)
app.app_context().push()

visualizer_handler = VisualizerHandler(app, socketio)
socketio.on_event('visualize', visualizer_handler.visualize, namespace = '/visualize')

if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0', port=8082, debug=True)