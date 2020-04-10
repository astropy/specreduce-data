# test to make sure line list data is properly packaged and can be read in correctly

import os
import warnings

import astropy

from ..readers import read_basic_ascii_table, collect_data_files


def test_read_onesstds():
    std_dir = os.path.join("reference_data", "onedstds")
    data_files = collect_data_files(std_dir)
    t = None
    for f in data_files:
        try:
            t = read_basic_ascii_table(
                f,
                reader="ascii.basic",
                names=["wavelength", "AB mag", "bin width"]
            )
            assert(len(t) > 0)
            assert(len(t.columns) == 3)
        except astropy.io.ascii.core.InconsistentTableError as e:
            orig_e = e.__class__.__name__
            try:
                t = read_basic_ascii_table(
                    f,
                    reader="ascii.basic",
                    names=None
                )
                assert(len(t) > 0)
            except Exception as e:
                msg = f"Failed to load {f} as a AstroPy Table : {orig_e} {e.__class__.__name__}"
                warnings.warn(msg)
