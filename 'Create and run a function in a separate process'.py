# стр. 521
#Cоздавание и запуск функции в отдельном процессе

import multiprocessing
import time

def clock(interval):
  while True:
    print('The time is %s' % time.ctime())
    time.sleep(interval)

if __name__ == '__main__':
  p = multiprocessing.Process(target=clock, args=(15,))
  p.start()


import multiprocessing
import time

class ClockProcess(multiprocessing.Process):
  def __init__(self,interval):
    multiprocessing.Process.__init__(self)
    self.interval = interval
  def run(self):
    while True:
      print('The time is %s' % time.ctime())
      time.sleep(self.interval)

if __name__ == '__main__':
  p = ClockProcess(15)
  p.start()
