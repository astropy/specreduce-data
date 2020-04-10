# utility functions for reading data files

from astropy.table import Table


def read_basic_ascii_table(table_file):
    """
    Try to read a file using AstroPy Table's basic ascii reader
    """
    t = Table.read(table_file, format='ascii')
    return t
