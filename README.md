# Meteorite Impact Zones Visualization

Visualization of meteorite impact sites worldwide using Voronoi diagrams and Delaunay triangulation.

## Description

This project analyzes NASA meteorite landing data and creates a geographic visualization showing:
- **Voronoi diagrams**: Influence zones around each meteorite impact site
- **Delaunay triangulation**: Spatial connectivity between neighboring impact sites
- **World map overlay**: Geographic context using Cartopy

## Requirements

- Python 3.x
- Required packages:
  ```
  pandas numpy matplotlib scipy geopandas shapely cartopy
  ```

## Installation

Install dependencies:
```bash
pip install pandas numpy matplotlib scipy geopandas shapely cartopy
```

## Usage

1. Ensure you have the `meteorite-landings.csv` file in the project directory
2. Run the script:
   ```bash
   python apfour.py
   ```

## Output

The script generates an interactive visualization showing:
- Meteorite impact sites (black dots)
- Voronoi cell boundaries (steel blue lines)
- Delaunay triangulation edges (dark red lines)
- World map with coastlines and borders

## Data Source

NASA Meteorite Landings Dataset (meteorite-landings.csv)

## Features

- Filters meteorites by mass (>5000g)
- Samples 500 points for optimal visualization
- Validates and cleans coordinate data
- Creates publication-quality geographic visualizations

