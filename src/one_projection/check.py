from typing import Union, List, Dict, Optional
from glob import glob

import geopandas as gpd
import rasterio as rio

from one_projection import get_files


def check_shp(fn_list, epsg, 
              res: Optional[Dict] = None) -> Dict[str, bool]:
    if res is None:
        res = {}
    
    dst_crs = f'epsg:{epsg}'
    for shp in fn_list:
        crs = gpd.read_file(shp).crs
        try:
            res[shp] = crs['init'] == dst_crs
        except KeyError:
            res[shp] = False
        # End try
    # End for

    return res
# End check_shp()


def check_rst(fn_list: List, epsg: Union[str, int], 
              res: Optional[Dict]=None) -> Dict[str, bool]:
    if res is None:
        res = {}

    for rst_fn in fn_list:
        with rio.open(rst_fn) as rst:
            rst_crs = rst.crs
            is_proj = rst_crs.is_projected
            is_epsg = rst_crs.is_epsg_code
            if (is_proj is True) and (is_epsg is True):
                rst_epsg = rst_crs.to_epsg()

                if str(rst_epsg) == str(epsg):
                    res[rst_fn] = True
                    continue
                # End if
            # End if

            res[rst_fn] = False
        # End with
    # End for

    return res
# End check_rst()


def check(epsg: Union[str, int], tgt_dir: str) -> Dict[str, bool]:
    """Check that files are in given CRS.

    Note: Files that use an alternate method of specifying the CRS
    (i.e. the EPSG code is not given) will be marked as `False`.

    Parameters
    ----------
    * epsg : int, desired EPSG code
    * tgt_dir : str, check shapefiles and geotiffs in the given directory

    Returns
    ----------
    * Dict[str, bool], filenames and bool, true if matches given CRS
    """
    shps, rsts = get_files(tgt_dir)

    res = {}
    if len(rsts) > 0:
        res = check_rst(rsts, epsg, res)
    if len(shps) > 0:
        res = check_shp(shps, epsg, res)

    return res
# End check()
