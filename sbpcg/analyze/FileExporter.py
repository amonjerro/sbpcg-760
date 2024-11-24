from abc import ABC, abstractmethod
import os
from typing import List

class FileExporter(ABC):
    @abstractmethod
    def export(self, data, headers, filename=''):
        pass

class CSVExporter(FileExporter):
    def __init__(self, output_path):
        self.output_path = output_path
    
    def export(self, data:List[List[int]], headers, filename=''):
        
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
        
        
        with open(f'{self.output_path}/{filename}.csv', 'w') as f:
            f.write(','.join(headers)+'\n')
            for line in data:
                f.write(','.join(map(lambda x: str(x), line))+'\n')

class ImageExporter(FileExporter):
    def __init__(self, output_path, filetype):
        self.output_path = output_path
        self.filetype = filetype
    
    def export(self, data:List[List[int]], filename=''):
        import matplotlib.pyplot as plt
        from PIL import Image

        
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
        
        x = [i for i in range(len(data))]
        fitness = [i[0] for i in data]
        print(fitness[0])

        fig, ax = plt.subplots(figsize = (5,2.7), layout="constrained")
        ax.plot(x, fitness)
        ax.set_xlabel("Generations")
        ax.set_ylabel("Average Fitness Value")
        ax.set_title("Average fitness over time")
        
        fig.canvas.draw()
        image = Image.frombytes('RGB', fig.canvas.get_width_height(), fig.canvas.tostring_rgb())
        plt.close(fig)
        image.save(f'{self.output_path}/{filename}.{self.filetype}')