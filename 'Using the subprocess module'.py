# стр. 506
# Выполнение системных команд

# Выполнить простую системную команду с помощью os.system()
ret = subprocess.call('ls -l', shell=True)

# Выполнить простую команду, игнорируя все, что она выводит
ret = subprocess.call('rm –f *.java',shell=True,stdout=open('/dev/null'))

# Выполнить системную команду, но сохранить ее вывод
p = subprocess.Popen('ls -l', shell=True, stdout=subprocess.PIPE)
out = p.stdout.read()

# Выполнить команду, передать ей входные данные и сохранить вывод
p = subprocess.Popen('wc', shell=True, stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = p.communicate(s) # Передать строку s дочернему процессу

# Создать два дочерних процесса и связать их каналом
p1 = subprocess.Popen('ls -l', shell=True, stdout=subprocess.PIPE)
p2 = subprocess.Popen('wc',shell=True, stdin=p1.stdout,stdout=subprocess.PIPE)
out = p2.stdout.read()
