# стр. 406

# Открыть архив tar и поместить в него несколько файлов
t = tarfile.open('foo.tar','w')
t.add('README')
import glob
for pyfile in glob.glob("*.py"):
  t.add(pyfile)
t.close()

# Открыть архив tar и выполнить обход всех его элементов
t = tarfile.open('foo.tar')
for f in t:
  print('%s %d' % (f.name, f.size))

# Просмотреть содержимое архива tar
# и вывести содержимое файлов с именем “README”
t = tarfile.open('foo.tar')
for f in t:
  if os.path.basename(f.name) == 'README':
    data = t.extractfile(f).read()
    print("**** %s ****" % f.name)
