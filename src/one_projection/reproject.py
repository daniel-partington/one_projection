from typing import Union, List, Dict, Optional
from glob import glob
import os

import geopandas as gpd

from one_projection import (get_files, read_shps, write_shpfile, gen_rprj_fn)


def reproject_shp(shp: gpd.GeoDataFrame, crs: str) -> gpd.GeoDataFrame:
    """Reprojects shape data."""
    return shp.to_crs(crs)
# End reproject_shp()


def reproject_rst(rst, crs):
    raise NotImplementedError()
# End reproject_rst()


def reproject(epsg: Union[str, int], tgt_dir: str) -> None:
    """Reprojects all shapefiles and rasters found in the given directory.

    Parameters
    ----------
    * epsg : str or int, epsg code
    * tgt_dir : str, path of directory
    """
    dst_crs = f'EPSG:{epsg}'
    shps, rsts = get_files(tgt_dir)

    for fn, shp_data in read_shps(shps):
        rprj_shp = reproject_shp(shp_data, dst_crs)
        new_fn = gen_rprj_fn(fn, epsg)
        write_shpfile(new_fn, rprj_shp)
    # End for

    # for rst in rsts:
    #     reproject_rst(rst, epsg)
    # # End for

# End reproject()

