import sqlite3
import datetime

conn = sqlite3.connect('stock_data.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS mytable(month MONTH, day DAY, year YEAR, open OPEN, high HIGH, low LOW, close CLOSE, adjclose ADJCLOSE, volume VOLUME)''')

sql_insert = ''' INSERT INTO mytable(month, day, year, open, high, low, close, adjclose, volume) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?) '''
with open('testinput.txt', 'r') as fr:
    for line in fr.readlines()[1:]:
        # parse the results.txt, create a list of comma separated values
        line = line.replace('\n', '').split()
        v1, v2, v3, v4, v5, v6, v7, v8, v9 = line
        c.execute(sql_insert, (datetime.datetime.strptime(v1, "%b").month, int(v2[:-1]), int(v3), float(v4.replace(',', '')), float(v5.replace(',', '')), float(v6.replace(',', '')), float(v7.replace(',', '')), float(v8.replace(',', '')), int(v9.replace(',', ''))))

conn.commit()

sql_select = ''' SELECT * FROM mytable '''
for row in c.execute(sql_select):
    print(row)

conn.close()