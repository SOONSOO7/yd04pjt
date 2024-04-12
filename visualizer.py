# visualizer.py
import plotly.graph_objects as go
import csv
from os.path import exists

class Visualizer:
    def __init__(self, file_name):
        self.file_name = file_name

    def plot_data(self, data):
        temperatures = []
        city = data['name']

        if not data['main']:
            return

        if exists(self.file_name):
            with open(self.file_name, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == city:
                        temperatures = [x for idx, x in enumerate(row) if idx != 0]

        #temperatures = [entry['temperature'] for entry in data]
        temperatures.append(data['main']['temp'])
        fig = go.Figure()
        fig.add_trace(go.Scatter(y=temperatures, mode='lines+markers', name='Temperature'))
        
        fig.update_layout(title=f'{data["name"]}: Temperature Over Time(24h)',
                          xaxis_title='Time',
                          yaxis_title='Temperature (°C)',
                          template='plotly_dark')
        
        output_file = data["name"] + '.png'
        fig.write_image(data["name"] + '.png')
        print(f"Graph saved to {output_file}")
    
