# NucleoSite

A pilot desktop application designed to streamline the process of finding suitable locations for nuclear power plants.

## Features

- Interactive map interface with zoom and coordinate conversion
- State-wise dam visualization and selection
- Detailed parameter analysis including:
  - Earthquake risk assessment
  - Population density analysis
  - Distance from highways and airports
  - Soil/geotechnical conditions
  - Mining activity analysis
  - Wind speed data
- Grid point visualization
- Comprehensive PDF report generation

## Project Structure

```
nucle-o-site/
├── src/                    # Source code
│   ├── core/              # Core functionality
│   │   ├── application.py        # Main application logic
│   │   ├── data_manager.py      # Data handling and management
│   │   ├── map_manager.py       # Map visualization and interaction
│   │   └── coordinate_*.py      # Coordinate transformation utilities
│   ├── ui/                # User interface components
│   │   ├── main_window.py       # Main application window
│   │   └── splash_screen.py     # Application splash screen
│   └── utils/             # Utility functions
│       ├── config.py            # Configuration management
│       ├── constants.py         # Application constants
│       └── report_generator.py  # PDF report generation
├── data/                  # Data directory
│   ├── states/           # State boundary shapefiles
│   ├── dams/            # Dam location data
│   ├── grid/            # Grid point data
│   ├── highways/        # Highway network data
│   ├── airports/        # Airport location data
│   ├── population/      # Population density data
│   └── wind/           # Wind speed data
├── reports/              # Generated reports
└── Optics/              # UI resources and images
```

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/nucle-o-site.git
cd nucle-o-site
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Prepare data directories:
```bash
python -c "from src.core.data_manager import DataManager; DataManager()"
```

5. Run the application:
```bash
python app.py
```

## Data Requirements

Place your data files in the following structure:
- `data/states/states.shp` - State boundary shapefile
- `data/dams/dams.shp` - Dam locations shapefile
- `data/grid/grid_points.shp` - Grid points shapefile
- `data/highways/national_highways.shp` - Highway network shapefile
- `data/airports/airports.shp` - Airport locations shapefile
- `data/population/population_density.tif` - Population density raster
- `data/wind/wind_speed.csv` - Wind speed data

## Dependencies

- PyQt5
- Matplotlib
- GeoPandas
- Shapely
- Rasterio
- ReportLab
- NumPy
- Pandas

## Developers

Developed by Om Gupta and Nirman Jaiswal under the mentorship of Prof. Sushobhan Sen at IIT Gandhinagar, as part of the Summer Research Internship Program (SRIP) 2024.
