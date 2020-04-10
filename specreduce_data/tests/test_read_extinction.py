# test to make sure extinction data is properly packaged and can be read in correctly

import os
import pkg_resources

from ..readers import read_basic_ascii_table

def test_read_extinction():
    ext_dir = os.path.join("reference_data", "extinction")
    for f in pkg_resources.resource_listdir("specreduce_data", ext_dir):
        if ".dat" in f:
            ext_path = pkg_resources.resource_filename(
                "specreduce_data",
                os.path.join(ext_dir, f)
            )
            t = read_basic_ascii_table(ext_path)
            assert(len(t) > 0)
            assert(len(t.columns) == 2)
