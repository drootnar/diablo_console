from .places import autodiscover_places

__all__ = ['load_level']

def load_level(file_object):
    points = []
    level_x = 0
    level_y = 0
    places = autodiscover_places()
    with open('diablo_console/images/{}.asc'.format(file_object)) as f:
        for line in f:
            level_y += 1
            level_x = max(level_x, len(line)-1)
            row = []
            for point in line:
                if ord(point) != 10:
                    row.append(places[point])
            points.append(row)
    return points, level_x, level_y
