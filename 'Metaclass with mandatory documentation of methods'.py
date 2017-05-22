# стр. 186

"""
Метакласс, который требует, чтобы все методы снабжались строками документирования
"""

class DocMeta(type):
	def __init__(self,name,bases,dict):
		for key, value in dict.items():
			# Пропустить специальные и частные методы
			if key.startswith('__'): continue
			# Пропустить любые невызываемые объекты
			if not hasattr(value,'__call__'): continue
			# Проверить наличие строки документирования
			if not getattr(value,'__doc__'):
				raise TypeError('{} must have a docstring'.format(key))
		type.__init__(self,name,bases,dict)

class Documented: # В Python 3 используется синтаксис
	__metaclass__ = DocMeta # class Documented(metaclass=DocMeta)

class Foo(Documented):
	def spam(self,a,b):
		'Метод spam делает кое-что'
		pass
