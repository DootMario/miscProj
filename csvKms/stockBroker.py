import csv

class StockStat:
    def __init__(self, symbol, maxx, minn, volume):
        self.symbol = symbol
        self.maxx = maxx
        self.minn = minn
        self.volume = volume

with open('stocks.csv', 'r') as csvfile:

    dicc = {}

    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        if row[0] not in dicc.keys():
            dicc.update({row[0]: StockStat(row[0], float(row[1]), float(row[1]), int(row[5]))})
        else:
            if float(row[1]) < dicc[row[0]].minn:
                dicc[row[0]].minn = float(row[1])
            if float(row[1]) > dicc[row[0]].maxx:
                dicc[row[0]].maxx = float(row[1])
            dicc[row[0]].volume = dicc[row[0]].volume + int(row[5])

sk = list(dicc.keys())
sk.sort()

with open('csvout.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Symbol", "Volume", "Max", "Min"])

    for sym in sk:
        stock = dicc[sym]
        writer.writerow([stock.symbol, stock.volume, stock.maxx, stock.minn])