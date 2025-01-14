import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
                    
def wait_for_event(e):
    logging.debug('wait_for_event starting')
    event_is_set = e.wait()
    logging.debug('event set: %s', event_is_set)

def wait_for_event_timeout(e, t):
    while not e.isSet():
        isSet = e.isSet()
        print("isSet() is: %r" % isSet)
        logging.debug('wait_for_event_timeout starting')
        event_is_set = e.wait(t)
        logging.debug('event set: %s', event_is_set)
        if event_is_set:
            logging.debug('processing event')
        else:
            logging.debug('doing other things')

if __name__ == '__main__':
    while True:
        e = threading.Event()
        t1 = threading.Thread(name='blocking', 
                          target=wait_for_event,
                         args=(e,))
        t1.start()

        t2 = threading.Thread(name='non-blocking', 
                          target=wait_for_event_timeout, 
                          args=(e, 2))
        t2.start()

        logging.debug('Waiting before calling Event.set()')
        e.set()
        t1.join()
        logging.debug('Event is set')
