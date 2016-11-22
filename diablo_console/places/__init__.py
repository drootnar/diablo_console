import sys, inspect

from .terrain import *
from .building import *


__all__ = ['autodiscover_places']


def autodiscover_places():
    places = {}
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj) and issubclass(obj, terrain.Place):
            places[obj.input_key] = obj
    return places
