# utility functions for reading packaged data files

import os
import pkg_resources

from astropy.table import Table


def read_basic_ascii_table(table_file, names=None, reader="ascii", **kwargs):
    """
    Try to read a file using AstroPy Table's basic ascii reader
    """
    t = Table.read(table_file, format=reader, names=names, **kwargs)

    return t


def collect_data_files(data_path="", ext=".dat"):
    """
    Walk through data_path, find .dat files, and return list of paths to them.
    """
    data_files = []
    root_dir = pkg_resources.resource_filename("specreduce_data", data_path)
    for root, dirs, files in os.walk(root_dir):
        for name in files:
            if ext in name:
                data_files.append(os.path.join(root, name))

    return data_files
