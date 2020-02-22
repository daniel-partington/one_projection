from typing import Union, List, Dict, Optional
from glob import glob

import geopandas as gpd
import rasterio as rio

from one_projection import (get_files, read_shps)


def reproject_shp(shp: gpd.GeoDataFrame, crs: str) -> Dict:
    """"""
    return shp.to_crs(crs)
# End reproject_shp()


def reproject(epsg: Union[str, int], tgt_dir: str) -> None:
    dst_crs = f'EPSG:{epsg}'
    shps, rsts = get_files(tgt_dir)

    rprj = {}
    for fn, shp_data in read_shps(shps):
        rprj_shp = reproject_shp(shp_data, dst_crs)
        rprj[fn] = rprj_shp

    # rsts = read_rsts()
    # rprj_rsts = reproject_rst(rsts, dst_crs)

    return rprj
# End reproject()

