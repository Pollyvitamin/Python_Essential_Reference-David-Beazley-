# стр. 546
#Cоздавание и запуск функции в отдельном потоке

import threading
import time

def clock(interval):
  while True:
    print('Текущее время: %s' % time.ctime())
    time.sleep(interval)

t = threading.Thread(target=clock, args=(15,))
t.daemon = True
t.start()


import threading
import time

class ClockThread(threading.Thread):
  def __init__(self,interval):
    threading.Thread.__init__(self)
    self.daemon = True
    self.interval = interval
  def run(self):
    while True:
      print('Текущее время: %s' % time.ctime())
      time.sleep(self.interval)

t = ClockThread(15)
t.start()
