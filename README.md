# NucleoSite - Nuclear Site Selection Tool

## Project Overview
NucleoSite is a cutting-edge desktop application designed to aid in the selection of optimal sites for nuclear facilities in India. Built with Python and PyQt5, the tool offers interactive geographic visualizations of dam locations, integrating comprehensive data analysis to evaluate dam safety and environmental impacts efficiently.

![NucleoSite Main Interface](Optics/app.png)

*The main interface of NucleoSite shows the interactive map.*


## Key Features
![Data Analysis Interface](Optics/grid_locations.png)

*Dams in India and potential grid locations for Nuclear Plants*

- **Interactive Map Visualization**: Users can navigate through dam locations across different states with options to zoom and access detailed data interactively.
- **Advanced Data Analysis**: Features multiple data layers to evaluate aspects such as seismic risks, population density, and proximity to water sources.

![Data Analysis Interface](Optics/buffer_zone.png)

Grid of potential locations within a 10 km buffer zone at a 1 km distance*

- **Dynamic Reporting**: Enables the generation and exportation of detailed PDF reports summarizing user analysis findings.
![Report Generation Module](Optics/report.png)

- **Customizable Search Parameters**: Users can define specific search criteria and thresholds, tailoring the output to particular needs.

*Example of a report generation module with output preview.*

## Technologies Used
- **Python**: The core programming language used.
- **PyQt5**: Utilized to create the graphical user interface.
- **Matplotlib & GeoPandas**: For processing and visualizing geospatial data.
- **FPDF**: For generating PDF reports.

## Acknowledgements
- Mentorship provided by Prof. Sushobhan Sen, IIT Gandhinagar.
- Developed by Nirman Jaiswal and Om Gupta.

![Poster](Optics/Poster_Presentation.jpg)
