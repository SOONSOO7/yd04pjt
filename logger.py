# logger.py
import csv

class Logger:
    def logging(self, data):
        	## TO-DO ##
		    # 전달받은 데이터를 파일로 저장한다.
		self.data = data
              ##?? need help  
              
        with open("log.csv", "a", newline='') as file: # w 를 a로 변경
            #로그 데이터를 쓰기 모드로 작성
            writer = csv.writer(file)
            # 열 작성
            writer.writerow(["main", "name"])
            # 열 추가
			for row in file:
                writer.writerow(row)
		
	    return

            
        