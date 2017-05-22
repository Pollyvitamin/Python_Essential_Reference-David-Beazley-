# стр. 169

"""
Перехват операций по изменению и удалению атрибута с помощью свойств
"""

class Foo(object):
	def __init__(self,name):
		self.__name = name
	@property
	def name(self):
		return self.__name
	@name.setter
	def name(self,value):
		if not isinstance(value,str):
			raise TypeError('Имя должно быть строкой!')
		self.__name = value
	@name.deleter
	def name(self):
		raise TypeError('Невозможно удалить атрибут name')

f = Foo('Гвидо')
n = f.name # вызовет f.name() – вернет функцию
f.name ='Монти' # вызовет метод изменения name(f,”Монти”)
f.name = 45 # вызовет метод изменения name(f,45) -> TypeError
del f.name # вызовет метод удаления name(f) -> TypeError
