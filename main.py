# main.py
from data_fetcher import DataFetcher
from data_processor import DataProcessor
from visualizer import Visualizer
from logger import Logger

def main():
    api_key = '<YOUR_API_KEY>'  # openweathermap API 키 입력
    city = input("Which City? ")
    
    fetcher = DataFetcher(api_key, city)
    processor = DataProcessor()
    visualizer = Visualizer()
    logger = Logger()
    
    raw_data = fetcher.fetch_weather()
    processed_data = processor.process_data(raw_data)
    logger.save_data(processed_data)
    visualizer.plot_data(processed_data)

if __name__ == "__main__":
    main()
