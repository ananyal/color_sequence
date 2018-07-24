import time

def hello() :
    print "Hello World!"
    time.sleep(10)

if __name__ == '__main__':
    try:
        hello()
    except KeyboardInterrupt:
        print 'Goodbye'
