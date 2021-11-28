import sqlite3
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# Establish sqlite database connection
conn = sqlite3.connect('stock_data.db')
c = conn.cursor()

# Create data table in stock_data
c.execute('''CREATE TABLE IF NOT EXISTS mytable(monthday MONTHDAY, year YEAR, open OPEN, high HIGH, low LOW, close CLOSE, adjclose ADJCLOSE, volume VOLUME)''')

# Add data values from text file, saving the stock symbol on first line
sql_insert = ''' INSERT INTO mytable(monthday, year, open, high, low, close, adjclose, volume) VALUES (?, ?, ?, ?, ?, ?, ?, ?) '''
with open('testinput.txt', 'r') as fr:
    stock_symbol = fr.readline().strip()
    for line in fr.readlines()[1:]:
        line = line.replace('\n', '').split()
        v1, v2, v3, v4, v5, v6, v7, v8, v9 = line
        date = "" + str(datetime.datetime.strptime(v1, "%b").month) + v2[:-1]
        c.execute(sql_insert, (int(date), int(v3), float(v4.replace(',', '')), float(v5.replace(',', '')), float(v6.replace(',', '')), float(v7.replace(',', '')), float(v8.replace(',', '')), int(v9.replace(',', ''))))

conn.commit()

# sql_select = ''' SELECT * FROM mytable ORDER BY monthday ASC'''
# for row in c.execute(sql_select):
#     print(row)

# Fetch data from database into sql_plot_data
sql_plot = ''' SELECT monthday, close FROM mytable ORDER BY monthday ASC '''
sql_plot_data = c.execute(sql_plot).fetchall()

# Graph stylization
sns.set_style("darkgrid")
font = {'fontname':'Comic Sans MS'}

# Draw Historical stock price line plot
figure = plt.figure()
graph = figure.add_subplot(1, 1, 1)
x_axis = []
y_axis = []
for x in sql_plot_data:
    x_axis.append(x[0])
    y_axis.append(x[1])
graph.plot(x_axis, y_axis, color='mediumorchid')

# Add title and axes titles
plt.title('Historical Stock Prices for ' + stock_symbol, **font)
plt.xlabel('Date (MMDD, 2021)', **font)
plt.ylabel('Price (USD)', **font)
sns.despine()
plt.show()
conn.close()