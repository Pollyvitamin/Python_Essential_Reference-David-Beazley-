# стр. 558
#Использование очереди в потоках

import threading
from queue import Queue # Use from Queue on Python 2

class WorkerThread(threading.Thread):
  def __init__(self,*args,**kwargs):
    threading.Thread.__init__(self,*args,**kwargs)
    self.input_queue = Queue()
  def send(self,item):
    self.input_queue.put(item)
  def close(self):
    self.input_queue.put(None)
    self.input_queue.join()
  def run(self):
    while True:
      item = self.input_queue.get()
      if item is None:
        break
      # Обработать элемент
      # (замените инструкцию print какими-нибудь полезными операциями)
      print(item)
      self.input_queue.task_done()
      # Конец. Сообщить, что сигнальная метка была принята, и выйти
      self.input_queue.task_done()
      return

# Пример использования
w = WorkerThread()
w.start()
w.send('hello') # Отправить элемент на обработку (с помощью очереди)
w.send('world')
w.close()
