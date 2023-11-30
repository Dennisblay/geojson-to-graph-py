from shapely.geometry import LineString
import math

ip = LineString([(0, 0), (0, 1), (1, 1), (1, 4), (4, 6), (10, 8), (20, 1), (100, 50)])


def densify_segment(current_row, distance=1):
    current_segment = current_row
    length_of_segment = current_segment.length
    for i in range(distance, math.floor(length_of_segment), distance):
        point = current_segment.interpolate(i)
        print(point)
        print(current_segment)
        current_segment = current_segment.union(point)
    return current_segment


res = densify_segment(ip, 2)
print(res)
