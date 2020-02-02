from typing import Union, List, Dict, Optional
from glob import glob

import geopandas as gpd
import rasterio as rio

from one_projection import get_files

def reproject_shp(fn_list, epsg):
    pass

def reproject(epsg: Union[str, int], tgt_dir: str) -> None:
    dst_crs = {'init': 'EPSG:{}'.format(epsg)}

    shps, rsts = get_files(tgt_dir)

    pass
# End reproject()