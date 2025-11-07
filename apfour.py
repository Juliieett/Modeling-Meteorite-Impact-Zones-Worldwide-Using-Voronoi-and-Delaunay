# ==========================================
# Modeling Meteorite Impact Zones Worldwide
# Using Voronoi Diagrams & Delaunay Triangulation
# ==========================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, Delaunay
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# -------------------------------------------------------
# 1. Load dataset (NASA / Kaggle: meteorite-landings.csv)
# -------------------------------------------------------
df = pd.read_csv("meteorite-landings.csv")

# Basic cleaning
df = df.dropna(subset=['reclat', 'reclong'])   # remove NaNs
df = df[(df['reclat'].between(-90, 90)) & (df['reclong'].between(-180, 180))]

# Filter by size for clarity (optional)
df = df[df['mass'] > 5000]   # keep larger meteorites
df = df.sample(500, random_state=42)  # sample for manageable number of points

# Coordinates for Voronoi/Delaunay
points = df[['reclong', 'reclat']].to_numpy()

# -------------------------------------------------------
# 2. Compute Delaunay triangulation & Voronoi tessellation
# -------------------------------------------------------
delaunay = Delaunay(points)
voronoi = Voronoi(points)

# -------------------------------------------------------
# 3. Visualization Setup (with map)
# -------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 6), subplot_kw={'projection': ccrs.PlateCarree()})
ax.add_feature(cfeature.COASTLINE, linewidth=0.5)
ax.add_feature(cfeature.BORDERS, linewidth=0.3)
ax.add_feature(cfeature.LAND, color='lightgray', alpha=0.5)
ax.add_feature(cfeature.OCEAN, color='lightblue', alpha=0.3)

# Plot Voronoi cells (finite segments only)
for vpair in voronoi.ridge_vertices:
    if vpair[0] >= 0 and vpair[1] >= 0:
        v0, v1 = voronoi.vertices[vpair[0]], voronoi.vertices[vpair[1]]
        ax.plot([v0[0], v1[0]], [v0[1], v1[1]], color='steelblue', linewidth=0.5, alpha=0.7)

# Plot Delaunay edges
for simplex in delaunay.simplices:
    ax.plot(points[simplex, 0], points[simplex, 1], color='darkred', linewidth=0.7, alpha=0.5)

# Meteorite points
ax.scatter(points[:,0], points[:,1], s=12, color='black', label='Meteorite Sites')

# -------------------------------------------------------
# 4. Enhance plot
# -------------------------------------------------------
ax.set_title("Meteorite Impact Influence Zones (Voronoi) and Connectivity (Delaunay)", fontsize=13)
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.legend()
ax.set_global()
ax.set_facecolor("#f9f9f9")

plt.tight_layout()
plt.show()
