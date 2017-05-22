#стр. 125

class NetworkError(Exception): # наследует класс Exception
	pass 
raise NetworkError('Невозможно найти компьютер в сети.')

class HostnameError(NetworkError): 
	pass
class TimeoutError(NetworkError): 
	pass

def error1():
	raise HostnameError('Хост не найден')
def error2():
	raise TimeoutError('Превышено время ожидания')
try:
	error1()
except NetworkError as e:
	if type(e) is HostnameError:
		# Выполнить действия, характерные для ошибки этого типа
		...

class DeviceError(Exception):
	def __init__(self,errno,msg):
		self.args = (errno, msg)
		self.errno = errno
		self.errmsg = msg
		
# Возбудить исключение (передав несколько аргументов)
raise DeviceError(1, 'Нет ответа')
