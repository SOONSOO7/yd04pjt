# visualizer.py
import plotly.graph_objects as go

class Visualizer:
    def plot_data(self, data, output_file='output.png'):
        #temperatures = [entry['temperature'] for entry in data]
        temperatures = [12.66, 11.78, 11.5, 10.93, 10.5] # samples
        fig = go.Figure()
        fig.add_trace(go.Scatter(y=temperatures, mode='lines+markers', name='Temperature'))
        
        fig.update_layout(title=f'{data[0]["name"]}: Temperature Over Time(24h)',
                          xaxis_title='Time',
                          yaxis_title='Temperature (°C)',
                          template='plotly_dark')

        fig.write_image(output_file)
        print(f"Graph saved to {output_file}")

test = Visualizer()
test.plot_data()