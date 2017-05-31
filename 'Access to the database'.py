# стр. 379
#Обход всех записей в наборе данных:

import sqlite3
conn = sqlite3.connect('dbfile')
cur = conn.cursor()
# Пример простого запроса
cur.execute('select name, shares, price from portfolio where account=12345')
# Обход результатов в цикле
while True:
  row = cur.fetchone()
  if not row: break
  # Обработать запись
  name, shares, price = row
  ...
# Альтернативный подход (с использованием итераций)
cur.execute('select name, shares, price from portfolio where account=12345')
for name, shares, price in cur:
  # Обработать запись
  ...
  
 # стр. 382
 #Отображение результатов в словари, используя функции-генераторы:
 
 def generate_dicts(cur):
  import itertools
  fieldnames = [d[0].lower() for d in cur.description ]
  while True:
    rows = cur.fetchmany()
    if not row: return
    for row in rows:
      yield dict(itertools.izip(fieldnames,row))
# Пример использования
cur.execute('select name, shares, price from portfolio')
for r in generate_dicts(cur):
  print(r['name'],r['shares'],r['price'])
  
# стр. 389
# Основные операции:

#Создание новых таблиц в базе данных
import sqlite3
conn = sqlite3.connect('mydb')
cur = conn.cursor()
cur.execute('create table stocks (symbol text, shares integer, price real)')
conn.commit()

#Добавление новых значений в таблицы
import sqlite3
conn = sqlite3.connect('mydb')
cur = conn.cursor()
cur.execute('insert into stocks values (?,?,?)',('IBM',50,91.10))
cur.execute('insert into stocks values (?,?,?)',('AAPL',100,123.45))
conn.commit()
stocks = [ ('GOOG',75,380.13),
('AA',60,14.20),
('AIG',125, 0.99) ]
cur.executemany('insert into stocks values (?,?,?)',stocks)

#Изменение существующих записей
cur.execute('update stocks set shares=? where symbol=?',(50,'IBM'))

#Удаление записей
cur.execute('delete from stocks where symbol=?',('SCOX',))

#Выполнение простых запросов:
# Выбрать все данные из таблицы
for row in cur.execute('select * from stocks'):
  инструкции
# Выбрать только некоторые столбцы
for shares, price in cur.execute('select shares,price from stocks'):
  инструкции
# Выбрать записи, соответствующие условию
for row in cur.execute('select * from stocks where symbol=?',('IBM',))
  инструкции
# Выбрать записи, соответствующие условию, и отсортировать их
for row in cur.execute('select * from stocks order by shares'):
  инструкции
# Выбрать записи, соответствующие условию,
# и отсортировать их в обратном порядке
for row in cur.execute('select * from stocks order by shares desc'):
  инструкции
# Выполнить соединение таблиц по общему столбцу (symbol)
for row in cur.execute('''select s.symbol, s.shares, p.price
                          from stocks as s, prices as p using(symbol)'''):
  инструкции
