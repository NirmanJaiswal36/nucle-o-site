import json
import os
from pathlib import Path

class Config:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls()
    
    def _initialize(self):
        self.config_file = Path(__file__).parent.parent.parent / 'config.json'
        self.default_config = {
            'data_paths': {
                'shapefiles': 'data/shapefiles',
                'output': 'data/output'
            },
            'thresholds': {
                'population_density': 500,
                'earthquake_risk': 'Zone II',
                'distance_from_city': 30,
                'distance_from_water': 10,
                'distance_from_airport': 50,
                'distance_from_highway': 10
            }
        }
        self.load_config()
    
    def load_config(self):
        if not self.config_file.exists():
            self.save_config(self.default_config)
        
        with open(self.config_file, 'r') as f:
            self.config = json.load(f)
    
    def save_config(self, config_data):
        with open(self.config_file, 'w') as f:
            json.dump(config_data, f, indent=4)
    
    def get(self, key, default=None):
        return self.config.get(key, default)
    
    def set(self, key, value):
        self.config[key] = value
        self.save_config(self.config)
