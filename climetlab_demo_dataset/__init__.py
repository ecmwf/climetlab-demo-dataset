# (C) Copyright 2020 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

from climetlab import Dataset
import math
import xarray as xr
import numpy as np


class DemoDataset(Dataset):

    home_page = "https://github.com/ecmwf/climetlab-demo-dataset"
    documentation = "Generates a dummy temperature field"

    def __init__(self):
        pass

    def _load(self, *args, **kwargs):

        lon = np.arange(-180.0, 180.0, 1.0)
        lat = np.arange(90.0, -91.0, -1.0)
        t2m = 273.15 + 20.0 * np.random.randn(len(lat), len(lon))
        t2m = np.zeros(shape=(len(lat), len(lon)))

        for i in range(0, len(lat)):
            for j in range(0, len(lon)):
                t2m[i, j] = 273.15 + (math.sin(i / 45.0) + math.sin(j / 90.0)) * 15

        ds = xr.Dataset(
            {"t2m": (["latitude", "longitude"], t2m)},
            coords={"longitude": lon, "latitude": lat},
        )

        ds["latitude"].attrs = dict(units="degrees_north", standard_name="latitude")
        ds["longitude"].attrs = dict(units="degrees_north", standard_name="longitude")
        ds["t2m"].attrs = dict(units="K", long_name="2 metre temperature")

        self._ds = ds

    def to_xarray(self):
        return self._ds

    def plot_map(self, driver):
        driver.plot_xarray(self._ds, "t2m")


dataset = DemoDataset
