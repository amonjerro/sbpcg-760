from abc import ABC, abstractmethod
import os
import sys
from typing import List

class FileExporter(ABC):
    @abstractmethod
    def export(self, data, headers):
        pass

class CSVExporter(FileExporter):
    def __init__(self, output_path, file_name):
        self.file_name = file_name
        self.output_path = output_path
    
    def export(self, data:List[List[int]], headers, filename=''):
        filename_to_use = self.file_name
        if filename != '':
            filename_to_use = filename
        
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
        
        
        with open(f'{self.output_path}/{filename_to_use}.csv', 'w') as f:
            f.write(','.join(headers)+'\n')
            for line in data:
                f.write(','.join(map(lambda x: str(x), line))+'\n')
