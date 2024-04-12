from data_fetcher import DataFetcher
from data_processor import DataProcessor
from visualizer import Visualizer
from logger import Logger
import schedule
import time

def fetch_and_process_city_data(city, api_key, log_file_name):
    fetcher = DataFetcher(api_key)
    processor = DataProcessor()
    visualizer = Visualizer(log_file_name)
    logger = Logger(log_file_name)

    raw_data = fetcher.fetch_weather(city)
    processed_data = processor.process_data(raw_data)
    logger.logging(processed_data)
    visualizer.plot_data(processed_data)

def scheduled_job(cities, api_key, log_file_name):
    for city in cities:
        fetch_and_process_city_data(city.strip(), api_key, log_file_name)

if __name__ == "__main__":
    api_key = '575688733bd584393af21c742c7acd64'
    log_file_name = 'log.csv'
    cities = input('Which Cities? ').split(',')
    
    scheduled_job(cities, api_key, log_file_name)
    schedule.every(10).minutes.do(scheduled_job, cities, api_key, log_file_name)

    while True:
        schedule.run_pending()
        time.sleep(1)
