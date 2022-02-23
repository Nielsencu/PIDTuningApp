import csv

class Logger():
    def __init__(self,folder, name):
        self.rows = []
        self.name = name
        self.log_folder = folder

    def addRow(self,row):
        self.rows.append(tuple((str(i) for i in row)))

    def __del__(self):
        with open(self.log_folder + self.name + '.csv', 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            for row in self.rows:
                writer.writerow(row)