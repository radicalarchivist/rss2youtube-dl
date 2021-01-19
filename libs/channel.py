import yaml
from pathlib import Path
import os

class LoadFailure(Exception):
    def __init__(self,message="Load failure!"):
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f'{self.message}\n  SYNTAX: {self.syntax}\n'

class Channel:
    def __init__(self,**kwargs):
        try:
            config_file = kwargs['config']
        except KeyError:
            try:
                config_file = os.path.join(kwargs['base'],".channels.yaml")
            except KeyError:
                raise LoadFailure
        Path(config_file).touch()
        with open(config_file,'r') as file:
            self.config = yaml.full_load(file)

    def list(self):
        return [value for item,value in self.config.items()]

if __name__ == "__main__":
    configs = Channel()
    for item in configs.list():
        print('RSS:',item['rss'])
        print('Directory:',item['download_dir'])
        if 'filter' in item:
            if isinstance(item['filter'],list):
                print('Filters',end=": ")
                for filter in item['filter']:
                    print(filter)
            else:
                print('Filters:',item['filter'])
        else:
            print('Filters: NONE')
