import time

from input_queue import InputQueue

if __name__ == '__main__':
    input_queue = InputQueue()
    
    while True:
        count = input_queue.get_count()
        print('Get count:', count)

        time.sleep(5)