# стр. 473
# Парсинг аргуметов командной строки

# foo.py
import optparse
p = optparse.OptionParser()

# Простой параметр без аргументов
p.add_option('-t', action='store_true', dest='tracing')

# Параметр, принимающий строковый аргумент
p.add_option('-o', '--outfile', action='store', type='string', dest='outfile')

# Параметр, принимающий целочисленный аргумент
p.add_option('-d', '--debuglevel', action='store', type='int', dest='debug')

# Параметр с небольшим числом допустимых значений аргумента
p.add_option('--speed', action='store', type='choice', dest='speed',
choices=['slow','fast','ludicrous'])

# Параметр, принимающий несколько аргументов
p.add_option('--coord', action='store', type='int', dest='coord', nargs=2)

# Группа параметров, значения которых сохраняются в одном и том же атрибуте
p.add_option('--novice', action='store_const', const='novice', dest='mode')
p.add_option('--guru', action='store_const', const='guru', dest='mode')

# Установить значения по умолчанию для различных параметров
p.set_defaults(tracing=False,
               debug=0,
               speed='fast',
               coord=(0,0),
               mode='novice')

# Проанализировать аргументы
opt, args = p.parse_args()

# Вывести значения параметров
print('tracing :', opt.tracing)
print('outfile :', opt.outfile)
print('debug :', opt.debug)
print('speed :', opt.speed)
print('coord :', opt.coord)
print('mode :', opt.mode)

# Вывести оставшиеся аргументы
print('args :', args)

% python foo.py -h
usage: foo.py [options]

options:
-h, --help show this help message and exit
-t
-o OUTFILE, --outfile=OUTFILE
-d DEBUG, --debuglevel=DEBUG
--speed=SPEED
--coord=COORD
--novice
--guru

% python foo.py -t -o outfile.dat -d 3 --coord 3 4 --speed=ludicrous blah
tracing : True
outfile : outfile.dat
debug : 3
speed : ludicrous
coord : (3, 4)
mode : novice
args : [‘blah’]

% python foo.py --speed=insane
usage: foo.py [options]

foo.py:error:option --speed:invalid choice:’insane’
(choose from ‘slow’, ‘fast’, ‘ludicrous’)
