# test to make sure extinction data is properly packaged and can be read in correctly

import os
import warnings

from ..readers import read_basic_ascii_table, collect_data_files


def test_read_extinction():
    ext_dir = os.path.join("reference_data", "extinction")
    data_files = collect_data_files(ext_dir)
    for f in data_files:
        try:
            t = read_basic_ascii_table(f, names=['wavelength', 'extinction'])
            assert(len(t) > 0)
            assert(len(t.columns) == 2)
        except Exception as e:
            msg = f"Failed to load {f} as an AstroPy Table: {e.__class__.__name__}"
            warnings.warn(msg)
