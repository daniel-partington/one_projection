# one_proj.check(epsg, shp_dir)
from typing import Union
from glob import glob

import geopandas as gpd


def check(epsg: Union[str, int], tgt_dir: str) -> dict:
    """Ensure files are in given CRS.

    Note: Files that use an alternate method of specifying the CRS
    (i.e. the EPSG code is not given) will be marked as `False`.

    Parameters
    ----------
    * epsg : int, desired EPSG code
    * tgt_dir : str, check files in the given directory

    Returns
    ----------
    * Dict[str => bool], filenames and bool, true if matches given CRS
    """
    dst_crs = 'epsg:{}'.format(epsg)

    shps = glob("{}/*.shp".format(tgt_dir))
    rsts = glob("{}/*.tif*".format(tgt_dir))

    res = {}
    for shp in shps:
        crs = gpd.read_file(shp).crs
        try:
            res[shp] = crs['init'] == dst_crs
        except KeyError:
            res[shp] = False
        # End try
    # End for

    return res

    
        


