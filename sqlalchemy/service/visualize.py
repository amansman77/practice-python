from repository import DasFileRepository

import time

class Visualizer:

    def __init__(self, app):
        super().__init__()
        self.das_file_repository = DasFileRepository()
        self.app = app

    def visualize(self, request):
        file_id = request['file_id']

        result = DasFileRepository.find_das_files_by_related_id(file_id)

        time.sleep(60*5)
        print(f'result: {result}')