# стр. 419
# Чтения файлов с настройками, вместо передачи параметров командой строке

# appconfig.ini
# Файл с параметрами настройки приложения mondo
[output]
LOGFILE=%(LOGDIR)s/app.log
LOGGING=on
LOGDIR=%(BASEDIR)s/logs
[input]
INFILE=%(INDIR)s/initial.dat
INDIR=%(BASEDIR)s/input

from configparser import ConfigParser # Use from ConfigParser in Python 2
# Словарь со значениями по умолчанию
defaults = {
'basedir' : '/Users/beazley/app'
}
# Создать объект ConfigParser и прочитать файл .ini
cfg = ConfigParser(defaults)
cfg.read('appconfig.ini')

>>> cfg.get('output','logfile')
'/Users/beazley/app/logs/app.log'
>>> cfg.get('input','infile')
'/Users/beazley/app/input/initial.dat'
>>> cfg.getboolean('output','logging')
True
