import csv
from os.path import exists

class Logger:
    def __init__(self, filename="log.csv"):
        self.filename = filename

        if not exists(self.filename):
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['City', 'Temperature'])

    def logging(self, data):
        city = data['name']
        temperature = data['main']['temp']

        updated = False
        rows = []
        try:
            with open(self.filename, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == city:
                        row.append(str(temperature))
                        updated = True
                    rows.append(row)

            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)

                if not updated:
                    writer.writerow([city, str(temperature)])
                    
        except Exception as e:
            print(f'log 저장 중 오류가 발생하였습니다.: {e}')
