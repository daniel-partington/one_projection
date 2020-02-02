from typing import Tuple, List
from glob import glob

def get_files(tgt_dir: str) -> Tuple[List]:
    shps = glob("{}/*.shp".format(tgt_dir))
    rsts = glob("{}/*.tif*".format(tgt_dir))

    return shps, rsts
# End get_files()