# main.py
from data_fetcher import DataFetcher
from data_processor import DataProcessor
from visualizer import Visualizer
# from logger import Logger

def main():
    api_key = '575688733bd584393af21c742c7acd64'  # openweathermap API 키 입력
    city = input("Which City? ")

    fetcher = DataFetcher(api_key)
    processor = DataProcessor()
    visualizer = Visualizer()
    # logger = Logger()
    
    raw_data = fetcher.fetch_weather(city)
    processed_data = processor.process_data(raw_data)
    print(processed_data)
    # logger.save_data(processed_data)
    visualizer.plot_data(processed_data)

if __name__ == "__main__":
    main()
