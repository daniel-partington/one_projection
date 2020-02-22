import one_projection as op


def test_shp_reproject():
    shp_dir = "data/shp"

    tmp = op.reproject(4326, shp_dir)
    for shp in tmp:
        assert tmp[shp].crs == 'EPSG:4326'
# End test_shp_reproject()


if __name__ == '__main__':
    test_shp_reproject()