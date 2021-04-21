from service import Visualizer

class VisualizerHandler:

    def __init__(self, app, socketio):
        self.visualizer = Visualizer(app)
        self.socketio = socketio
        self.app = app
 
    def visualize(self, request: dict):
        self.visualizer.visualize(request)        

        print(f'[VisualizerHandler.visualize] finish')

