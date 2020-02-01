import one_projection as op


def test_crs_check():
    shp_dir = "data/shp"

    res = op.check(28355, shp_dir)

    assert all(res.values()) == True

if __name__ == '__main__':
    test_crs_check()