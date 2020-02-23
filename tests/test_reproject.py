import one_projection as op


def test_shp_reproject():
    shp_dir = "tests/data/shp"

    res = op.check(28355, shp_dir)
    assert all(res.values()) == True

    op.reproject(4326, shp_dir)

    res = op.check(4326, shp_dir)
    assert all(res.values()) == False
    
# End test_shp_reproject()


def test_rst_reproject():
    shp_dir = "tests/data/rst"

    tmp = op.reproject(4326, shp_dir)
    for shp in tmp:
        assert tmp[shp].crs == 'EPSG:4326'
# End test_shp_reproject()


def teardown():
    import os
    from glob import glob

    shp_dir = "tests/data/shp"

    rprj_files = glob(shp_dir+'/*_4326.*')
    for fn in rprj_files:
        os.remove(fn)

    rst_dir = "tests/data/rst"
    rprj_files = glob(rst_dir+'/*_4326.*')
    for fn in rprj_files:
        os.remove(fn)
# End teardown()


if __name__ == '__main__':
    test_shp_reproject()