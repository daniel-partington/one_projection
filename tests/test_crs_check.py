import one_projection as op


def test_shp_check():
    shp_dir = "tests/data/shp"

    res = op.check(28355, shp_dir)

    assert all(res.values()) == True
# End test_shp_check()


def test_rst_check():
    rst_dir = "tests/data/rst"

    res = op.check(28355, rst_dir)

    assert all(res.values()) == False
# end test_rst_check()


if __name__ == '__main__':
    test_shp_check()
    test_rst_check()