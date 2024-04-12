# data_processor.py
import json

class DataProcessor:
    def process_data(self, json_data):
		    ## TO-DO ##
		    ## API를 통해 입력받은 json중에서 필요한 field값만 추출하기
      self.process_data = {
         # "coord": json_data.get("coord"),
         "weather": json_data.get("weather"),
         "main": json_data.get("main"),
         "wind": json_data.get("wind"),
         "visibility": json_data.get("visibility"),
         "clouds": json_data.get("clouds"),
         # "dt": json_data.get("dt"),
         # "sys": json_data.get("sys"),
         "timezone": json_data.get("timezone"),
         # "id": json_data.get("id"),
         "name": json_data.get("name"),
         "cod": json_data.get("cod")
      }

        return processed_data