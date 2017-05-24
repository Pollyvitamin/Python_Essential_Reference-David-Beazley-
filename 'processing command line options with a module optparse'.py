# стр. 205
"""
Обработка параметров командной строки с помощью модуля optparse.
"""

import optparse
p = optparse.OptionParser()

# Параметр имеет дополнительный аргумент
p.add_option('-o',action='store',dest='outfile')
p.add_option('--output',action='store',dest='outfile')

# Параметр устанавливает логический флаг
p.add_option('-d',action='store_true',dest='debug')
p.add_option('--debug',action='store_true',dest='debug')

# Установить значения по умолчанию для отдельных параметров
p.set_defaults(debug=False)

# Анализ командной строки
opts, args = p.parse_args()

# Извлечение значений параметров
outfile = opts.outfile
debugmode = opts.debug
