import time

colors = ['R', 'G', 'B', 'Y']

def print_list():
    for i in range(0, len(colors)) :
        print colors[i]
        time.sleep(1)

if __name__ == '__main__' :
    try:
        print_list()
    except KeyboardInterrupt:
        print 'Goodbye'
