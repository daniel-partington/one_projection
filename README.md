# one_projection

A simple tool to ensure one spatial projection.

## Usage (incomplete)

**Programmatic**

```python
import one_projection as op

...
```

**Command-line use**
```bash
$ oneproj [commands]
```

## Development

Assuming you are in the project directory and are on Windows:

This project relies on rasterio which requires additional installation steps for Windows.
Refer to [the documentation](https://pypi.org/project/rasterio/) for more information.

In the steps below, we side-step the additional requirements by relying on the conda ecosystem.

```bash
$ conda env create --file win_dev.yml
$ conda activate oneproj
$ conda install -c conda-forge gdal geopandas rasterio
$ python setup.py develop
```

If all goes well, you should be able to run all tests with

```bash
$ py.test
```
