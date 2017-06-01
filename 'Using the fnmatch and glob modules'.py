# стр. 399
#Модуль fnmatch обеспечивает поддержку сопоставления имен файлов с применением шаблонных символов, 
#как это делает командная оболочка в системе UNIX. 

fnmatch('foo.gif', '*.gif') # Вернет True
fnmatch('part37.html', 'part3[0-5].html') # Вернет False

# Пример поиска файлов в дереве каталогов
# с помощью функции os.walk(), модуля fnmatch и генераторов
def findall(topdir, pattern):
  for path, files, dirs in os.walk(topdir):
    for name in files:
      if fnmatch.fnmatch(name,pattern):
        yield os.path.join(path,name)

# Отыскать все файлы с расширением .py
for pyfile in findall(".","*.py"):
print(pyfile)


#Модуль glob позволяет получить список всех имен файлов в каталоге, соответствующих указанному шаблону, 
#с применением правил командной оболочки UNIX.

htmlfile = glob('*.html')
imgfiles = glob('image[0-5]*.gif')
