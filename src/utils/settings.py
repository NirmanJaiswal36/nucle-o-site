import os
from pathlib import Path

class Settings:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Settings, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        # Base paths
        self.root_dir = Path(__file__).parent.parent.parent
        self.src_dir = self.root_dir / 'src'
        self.data_dir = self.root_dir / 'data'
        self.reports_dir = self.root_dir / 'reports'
        self.optics_dir = self.root_dir / 'Optics'

        # Create necessary directories
        self.data_dir.mkdir(exist_ok=True)
        self.reports_dir.mkdir(exist_ok=True)

        # Data paths
        self.gis_data = {
            'states': self.data_dir / 'states' / 'states.shp',
            'dams': self.data_dir / 'dams' / 'dams.shp',
            'grid_points': self.data_dir / 'grid' / 'grid_points.shp',
            'highways': self.data_dir / 'highways' / 'national_highways.shp',
            'airports': self.data_dir / 'airports' / 'airports.shp',
            'population': self.data_dir / 'population' / 'population_density.tif',
            'wind_speed': self.data_dir / 'wind' / 'wind_speed.csv'
        }

        # UI resources
        self.ui_resources = {
            'logo': self.optics_dir / 'logo.jpg',
            'splash_screen': self.optics_dir / 'Nucleosite_splash_screen.ui'
        }

        # Parameters and thresholds
        self.thresholds = {
            'earthquake_risk': 'Zone II',
            'population_density': 300,  # per sq.km
            'highway_distance': 100,    # km
            'airport_distance': 100,    # km
            'water_body_distance': 10,  # km
            'city_distance': 30         # km
        }

    @property
    def gis_paths(self):
        """Returns all GIS data paths"""
        return self.gis_data

    @property
    def resources(self):
        """Returns UI resource paths"""
        return self.ui_resources

    @classmethod
    def get_instance(cls):
        """Get the singleton instance"""
        return cls()

    def get_data_path(self, data_type):
        """Get path for a specific data type"""
        return self.gis_data.get(data_type)

    def get_threshold(self, parameter):
        """Get threshold value for a parameter"""
        return self.thresholds.get(parameter)
