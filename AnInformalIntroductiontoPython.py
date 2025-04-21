
# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is 
not a comment because it's inside quotes."

from shapely.geometry import Polygon
from shapely.ops import polygonize
import geopandas as gpd

# Define a compound polygon (one polygon with two disconnected areas)
# Example with unknown disconnection points
poly = Polygon([
    (0, 0), (1, 0), (1, 1), (0, 1), (0, 0),  # First square
    (2, 2), (3, 2), (3, 3), (2, 3), (2, 2)     # Second square (improperly connected)
])

# Extract the boundary of the polygon (boundary can have disconnected segments)
boundary = poly.boundary

# Use polygonize to break boundary into separate polygons
polygons = list(polygonize(boundary))

# Create a GeoDataFrame from the list of polygons
gdf = gpd.GeoDataFrame(geometry=polygons)

# Set a coordinate reference system (optional, example EPSG:4326)
gdf.set_crs("EPSG:4326", inplace=True)

# Save the polygons as a shapefile
gdf.to_file("separate_areas.shp")
