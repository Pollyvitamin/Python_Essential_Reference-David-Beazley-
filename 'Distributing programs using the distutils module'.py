# стр. 200

"""
Подготовка дистрибутива программы для передачи ее другому лицу,
с помощью модуля distutils
"""

#структура каталога:
spam/
	README.txt
	Documentation.txt
	libspam.py # Одиночный библиотечный модуль
	spampkg/ # Пакет вспомогательных модулей
		 __init__.py
		foo.py
		bar.py
	runspam.py # Сценарий, который запускается как: python runspam.py

#Cоздание файла setup.py в самом верхнем каталоге (spam):
# setup.py
from distutils.core import setup
setup(name = “spam”,
	version = “1.0”,
	py_modules = [‘libspam’],
	packages = [‘spampkg’],
	scripts = [‘runspam.py’])

#создание дистрибутива:
%python setup.py sdist

#установка из дистрибутиваЖ
% unzip spam-1.0.zip
...
% cd spam-1.0
% python setup.py install
...
%
