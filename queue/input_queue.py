import time

import queue, threading

class InputQueue:

    def __init__(self):
        self.q = queue.Queue()

        t = threading.Thread(target=self.__reader)
        t.daemon = True
        t.start()
    
    def __reader(self):
        count = 0
        while True:
            try:
                try:
                    _count = self.q.get_nowait()
                    print('Remove count:', _count)
                except queue.Empty:
                    pass

                self.q.put(count)
                print('Put count:', count)
                time.sleep(1)
                count += 1
            except Exception as ex:
                print('Exception: ', ex)

    def get_count(self):
        return self.q.get()
