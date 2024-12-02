from typing import Dict

class DataStream:
    def __init__(self):
        self.last_printed: Dict[str, int] = {}

    def should_output_data_str(self, timestamp: int, data_str: str) -> bool:
        if data_str not in self.last_printed or timestamp >= self.last_printed[data_str] + 5:
            self.last_printed[data_str] = timestamp
            return True
        return False

data_stream = DataStream()
print(data_stream.should_output_data_str(timestamp=0, data_str="hello"))  
print(data_stream.should_output_data_str(timestamp=1, data_str="world"))  
print(data_stream.should_output_data_str(timestamp=6, data_str="hello"))  
print(data_stream.should_output_data_str(timestamp=7, data_str="hello"))  
print(data_stream.should_output_data_str(timestamp=8, data_str="world"))  
