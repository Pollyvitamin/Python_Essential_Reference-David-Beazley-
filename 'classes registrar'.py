# стр. 188

"""
Регистратор классов
"""

registry = { }
def register(cls):
	registry[cls.__clsid__] = cls
	return cls

@register
class Foo(object):
	__clsid__ = '123-456'
	def bar(self):
		pass

print(registry) # {'123-456': <class '__main__.Foo'>}
