from typing import Tuple, List
from glob import glob

import geopandas as gpd


def get_files(tgt_dir: str) -> Tuple[List]:
    shps = glob("{}/*.shp".format(tgt_dir))
    rsts = glob("{}/*.tif*".format(tgt_dir))

    return shps, rsts
# End get_files()


def read_shps(shps: List) -> List:
    """Generator for reading in shapefiles"""
    for shp in shps:
        yield shp, gpd.read_file(shp)
    # End for
# End read_shps()


def write_shps(shps: List) -> None:
    for shp in shps:
        pass