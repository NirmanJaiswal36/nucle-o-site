# Application constants
APP_NAME = "NucleoSite"
APP_VERSION = "1.0.0"

# UI Constants
WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 1000
SPLASH_SCREEN_DURATION = 3000  # milliseconds

# Map Constants
DEFAULT_FIGURE_SIZE = (20, 20)
HOVER_BUFFER_SIZE = 5000
CLICK_BUFFER_SIZE = 5000

# File paths and directories
SHAPEFILE_DIR = "data/shapefiles"
OUTPUT_DIR = "data/output"
REPORT_TEMPLATE_DIR = "templates"

# Analysis Parameters
DISTANCE_UNITS = "kilometers"
COORDINATE_SYSTEM = "EPSG:4326"  # WGS 84
BUFFER_ZONE_RADIUS = 30  # kilometers

# Thresholds
THRESHOLDS = {
    "population_density": {
        "value": 500,
        "unit": "people/km²",
        "description": "Maximum allowable population density"
    },
    "earthquake_risk": {
        "value": "Zone II",
        "description": "Maximum allowable seismic zone"
    },
    "distance_from_city": {
        "value": 30,
        "unit": "km",
        "description": "Minimum distance from major cities"
    },
    "distance_from_water": {
        "value": 10,
        "unit": "km",
        "description": "Minimum distance from water bodies"
    },
    "distance_from_airport": {
        "value": 50,
        "unit": "km",
        "description": "Minimum distance from airports"
    },
    "distance_from_highway": {
        "value": 10,
        "unit": "km",
        "description": "Minimum distance from highways"
    }
}

# Error Messages
ERROR_MESSAGES = {
    "shapefile_not_found": "Required shapefile not found",
    "invalid_coordinates": "Invalid coordinates provided",
    "calculation_error": "Error in calculation",
    "export_failed": "Failed to export report",
    "data_load_error": "Failed to load required data"
}
