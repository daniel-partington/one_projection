from typing import Tuple, List, Generator
from glob import glob
import os

import geopandas as gpd


def get_files(tgt_dir: str) -> Tuple[List]:
    shps = glob("{}/*.shp".format(tgt_dir))
    rsts = glob("{}/*.tif*".format(tgt_dir))

    return shps, rsts
# End get_files()


def read_shps(shps: List) -> Generator:
    """Generator for reading in shapefiles"""
    for shp in shps:
        yield shp, gpd.read_file(shp)
    # End for
# End read_shps()


# def read_rsts(rsts: List) -> Generator:
#     """Generator for reading in shapefiles"""
#     for rst in rsts:
#         yield shp, rio.open(rst)
#     # End for
# # End read_shps()


def gen_rprj_fn(fn, tgt_epsg):
    pre, ext = os.path.splitext(fn)
    return f"{pre}_{tgt_epsg}{ext}"
# End gen_rprj_fn()


def write_shpfile(fn: str, data: gpd.GeoDataFrame) -> None:
    data.to_file(fn)
# End write_shpfile()
