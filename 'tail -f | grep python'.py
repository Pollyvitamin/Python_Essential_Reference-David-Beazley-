#стр. 41
# следит за содержимым файла (на манер команды tail -f)
import time
def tail(f):
    f.seek(0,2) # Переход в конец файла
    while True:
        line = f.readline() # Попытаться прочитать новую строку текста
        if not line: # Если ничего не прочитано,
            time.sleep(0.1) # приостановиться на короткое время
            continue # и повторить попытку
        yield line

def grep(lines, searchtext):
    for line in lines:
        if searchtext in line: yield line

# Реализация последовательности команд “tail -f | grep python”
wwwlog = tail(open(“access-log”))
pylines = grep(wwwlog,”python”)
for line in pylines:
    print line,
