# стр. 460
"""
Настройка приложения на использование модуля logging обычно выполняется в несколько основных этапов:
1. С помощью функции getLogger() создается несколько объектов класса
Logger. Соответствующим образом устанавливаются значения параметров, таких как уровень важности.
2. Создаются объекты обработчиков различных типов (таких как FileHandler, StreamHandler, SocketHandler
и так далее) и устанавливаются соответствующие уровни важности.
3. Создаются объекты класса Formatter и подключаются к объектам Handler с помощью метода setFormatter().
4.С помощью метода addHandler() объекты Handler подключаются к объектам Logger 
"""
# applogconfig.py
import logging
import sys

# Определить формат сообщений
format = logging.Formatter('%(levelname)-10s %(asctime)s %(message)s')

# Создать обработчик, который выводит сообщения с уровнем CRITICAL
# в поток stderr
crit_hand = logging.StreamHandler(sys.stderr)
crit_hand.setLevel(logging.CRITICAL)
crit_hand.setFormatter(format)

# Создать обработчик, который выводит сообщения в файл
applog_hand = logging.FileHandler('app.log')
applog_hand.setFormatter(format)

# Создать регистратор верхнего уровня с именем ‘app’
app_log = logging.getLogger('app')
app_log.setLevel(logging.INFO)
app_log.addHandler(applog_hand)
app_log.addHandler(crit_hand)

# Изменить уровень важности для регистратора ‘app.net’
logging.getLogger('app.net').setLevel(logging.ERROR)
