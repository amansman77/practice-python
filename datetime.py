import datetime

if __name__ == '__main__':
    a = datetime.datetime(100,1,1,11,34,59)
    b = a + datetime.timedelta(0,3) # days, seconds, then other fields.
    print(a.time())
    print(b.time())

    start_time = datetime.datetime.strptime('20200602_133422', '%Y%m%d_%H%M%S')
    finish_time = start_time + datetime.timedelta(0,3)
    print(start_time.time())
    print(finish_time.time())