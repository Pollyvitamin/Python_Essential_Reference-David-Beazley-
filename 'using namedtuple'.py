# стр. 335

"""
Cоздание именованного кортеж NetworkAddress, который поддерживает возможность обращения к его элементам как к атрибутам.
Внутренняя реализация этого класса не использует словарь экземпляра и не увеличивает потребление памяти по сравнению с обычными
кортежами
"""

>>> from collections import namedtuple
>>> NetworkAddress = namedtuple(‘NetworkAddress’,[‘hostname’,’port’])
>>> a = NetworkAddress(‘www.python.org’,80)
>>> a.hostname
‘www.python.org’
>>> a.port
80
>>> host, port = a
>>> len(a)
2
>>> type(a)
<class ‘__main__.NetworkAddress’>
>>> isinstance(a, tuple)
True
>>>
