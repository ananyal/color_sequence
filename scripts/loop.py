import time

def loop():
    while True:
        print 'Hello World!'
        time.sleep(1)

if __name__ == '__main__' :
    try:
        loop()
    except KeyboardInterrupt:
        print 'Goodbye'
