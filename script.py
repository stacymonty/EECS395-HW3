import math

class TileSystem():
    def __init__():
        self.earthRadius = 6378137
        self.minLat = -85.05112878
        self.maxLat = 85.05112878
        self.minLon = -180.0
        self.maxLon = 180.0

    def clip(n, minVal, maxVal):
        return min(max(n, minVal), maxVal);

    def map_size(levelOfDetail):
        return 256 << level

    def ground_resolution(lat, levelOfDetail):
        lat = clip(lat, self.minLat, self.maxLat)
        return cos(lat * pi / 180) * 2 * pi * self.earthRadius / map_size(levelOfDetail)

    def mapScale(lat, levelOfDetail, screenDpi):
        return ground_resolution(lat, levelOfDetail) * screenDpi / 0.0254;

    def lat_long_to_pixelXY(lat, lon, int levelOfDetail, out int pixelX, out int pixelY)  
