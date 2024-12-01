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
            f.write('-'.join(headers)+'\n')
            for line in data:
                f.write('-'.join(map(lambda x: str(x), line))+'\n')

class ImageExporter(FileExporter):
    def __init__(self, output_path, filetype):
        self.output_path = output_path
        self.filetype = filetype
    
    def export(self, data:List[List[int]], file_prefix=''):
        import matplotlib.pyplot as plt
        from PIL import Image
        from sbpcg import CreatureTypes

        
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
        
        x = [i for i in range(len(data))]
        fitness = [i[0] for i in data]

        # Plot Average Fitness
        fig, ax = plt.subplots(figsize = (5,2.7), layout="constrained")
        ax.plot(x, fitness)
        ax.set_xlabel("Generations")
        ax.set_ylabel("Average Fitness Value")
        ax.set_title("Average fitness over time")
        fig.canvas.draw()
        image = Image.frombytes('RGB', fig.canvas.get_width_height(), fig.canvas.tostring_rgb())
        plt.close(fig)
        image.save(f'{self.output_path}/{file_prefix}-avgFitness.{self.filetype}')

        frames = []
        for i in range(len(data)):
            fig, ax = plt.subplots(figsize = (5,2.7), layout="constrained")
            ax.bar([i.name for i in CreatureTypes], [data[i][1],data[i][5],data[i][9],data[i][13]])
            ax.set_title(f"Count of creature by type. Gen {i}")
            fig.canvas.draw()
            image = Image.frombytes('RGB', fig.canvas.get_width_height(), fig.canvas.tostring_rgb())
            plt.close(fig)
            frames.append(image)
        frames[0].save(f'{self.output_path}/{file_prefix}-typeCount.gif', save_all=True, append_images=frames[1:], duration=350, loop=0)
        
