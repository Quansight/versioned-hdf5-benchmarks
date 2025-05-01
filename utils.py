import os
import subprocess


def debug_libhdf5_so():
    """Print out which .so file is actually loaded at runtime for libhdf5"""
    import h5py

    for row in (
        subprocess.check_output(["lsof", "-p", str(os.getpid())])
        .decode("utf-8")
        .splitlines()
    ):
        row = row.strip()
        if "libhdf5" in row:
            print(row)
