import pyproj
from shapely.geometry import Point, Polygon

class CoordinateTransformer:
    def __init__(self):
        # Initialize the coordinate transformer
        self.wgs84_to_web_mercator = pyproj.Transformer.from_crs(
            'EPSG:4326',  # WGS84 (latitude/longitude)
            'EPSG:3857',  # Web Mercator
            always_xy=True
        )
        
        self.web_mercator_to_wgs84 = pyproj.Transformer.from_crs(
            'EPSG:3857',  # Web Mercator
            'EPSG:4326',  # WGS84 (latitude/longitude)
            always_xy=True
        )

    def to_web_mercator(self, lon, lat):
        """Convert WGS84 coordinates to Web Mercator"""
        return self.wgs84_to_web_mercator.transform(lon, lat)

    def to_wgs84(self, x, y):
        """Convert Web Mercator coordinates to WGS84"""
        return self.web_mercator_to_wgs84.transform(x, y)

    def transform_point(self, point, source_crs, target_crs):
        """Transform a point from source CRS to target CRS"""
        transformer = pyproj.Transformer.from_crs(
            source_crs,
            target_crs,
            always_xy=True
        )
        if isinstance(point, Point):
            x, y = transformer.transform(point.x, point.y)
            return Point(x, y)
        else:
            x, y = transformer.transform(point[0], point[1])
            return (x, y)

    def transform_polygon(self, polygon, source_crs, target_crs):
        """Transform a polygon from source CRS to target CRS"""
        transformer = pyproj.Transformer.from_crs(
            source_crs,
            target_crs,
            always_xy=True
        )
        if isinstance(polygon, Polygon):
            exterior_coords = list(polygon.exterior.coords)
            transformed_coords = [transformer.transform(x, y) for x, y in exterior_coords]
            return Polygon(transformed_coords)
        return None
