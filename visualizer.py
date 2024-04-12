# visualizer.py
import plotly.graph_objects as go

class Visualizer:
    def plot_data(self, data):
        if not data['main']:
            return

        #temperatures = [entry['temperature'] for entry in data]
        temperatures = [] # samples
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
    
