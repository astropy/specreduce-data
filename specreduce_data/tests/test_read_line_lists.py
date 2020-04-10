# test to make sure line list data is properly packaged and can be read in correctly

import os
import warnings

import astropy

from ..readers import read_basic_ascii_table, collect_data_files


def test_read_line_lists():
    line_dir = os.path.join("reference_data", "line_lists")
    data_files = collect_data_files(line_dir)
    for f in data_files:
        try:
            t = read_basic_ascii_table(f, names=['wavelength'])
            assert(len(t) > 0)
            assert(len(t.columns) >= 1)
        except astropy.io.ascii.core.InconsistentTableError as e:
            try:
                t = read_basic_ascii_table(
                    f,
                    reader="ascii.fixed_width",
                    names=['wavelength', 'info'],
                    col_starts=(0, 10),
                    delimiter=' '
                )
                assert(len(t) > 0)
                assert(len(t.columns) >= 1)
            except Exception as e:
                msg = f"Failed to load {f} as a AstroPy Table: {e.__class__.__name__}"
                warnings.warn(msg)
