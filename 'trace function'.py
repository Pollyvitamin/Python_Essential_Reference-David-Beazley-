#стр. 140
"""
Функция trace() создает функцию-обертку, которая записывает некоторую отладочную информацию в файл и затем вызывает
оригинальный объект функции
"""
enable_tracing = True
if enable_tracing:
	debug_log = open('debug.log','w')

def trace(func):
	if enable_tracing:
		def callf(*args,**kwargs):
			debug_log.write('Вызов {}: {}, {}\n'.format(func.__name__, args, kwargs))
			r = func(*args,**kwargs)
			debug_log.write('{} вернула {}\n'.format(func.__name__, r))
			return r
		return callf
	else:
		return func
