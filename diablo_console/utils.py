__all__ = ['load_level']

def load_level(file_object):
    points = []
    with open('diablo_console/images/{}.asc'.format(file_object)) as f:
        for line in f:
            points.append(line[0:-1])  # skip CR
    return points