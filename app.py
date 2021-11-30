import sqlite3
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import seaborn as sns
import pandas as pd
 
# Establish sqlite database connection
conn = sqlite3.connect('stock_data.db')
c = conn.cursor()
 
# Create data table in stock_data
c.execute('''CREATE TABLE IF NOT EXISTS mytable(date DATE, open OPEN, high HIGH, low LOW, close CLOSE, adjclose ADJCLOSE, volume VOLUME)''')
 
# Add data values from text file, saving the stock symbol on first line
sql_insert = ''' INSERT INTO mytable(date, open, high, low, close, adjclose, volume) VALUES (?, ?, ?, ?, ?, ?, ?) '''
with open('testinput.txt', 'r') as fr:
    stock_symbol = fr.readline().strip()
    for line in fr.readlines()[1:]:
        line = line.replace('\n', '').split()
        v1, v2, v3, v4, v5, v6, v7, v8, v9 = line
        date = "2021-" + str(datetime.datetime.strptime(v1, "%b").month) +'-'+ v2[:-1]
        c.execute(sql_insert, (date, float(v4.replace(',', '')), float(v5.replace(',', '')), float(v6.replace(',', '')), float(v7.replace(',', '')), float(v8.replace(',', '')), int(v9.replace(',', ''))))
 
conn.commit()
 
#sql_select = ''' SELECT * FROM mytable '''
#for row in c.execute(sql_select):
     #print(row)
 
 
# Fetch data from database into sql_plot_data
sql_plot = ''' SELECT date, close FROM mytable '''
df = pd.read_sql_query(sql_plot, con=conn)
df = df[::-1]
df.reset_index(drop=True, inplace=True)
 
# Graph stylization
sns.set_style("darkgrid")

# Add title and axes titles

ax = df.plot('date', 'close', title='Historical Stock Prices for ' + stock_symbol + ' in Last 4 Months', color='mediumorchid', legend=None)
ax.set_xlabel("Date")
ax.set_ylabel("Price (USD)")
sns.despine()
plt.show()
 
sql_delete = 'DROP TABLE mytable ;'
c.execute(sql_delete)
conn.close()
