import sys
import os
from os import environ, path

# This allows for using cadquery from an external non conda python installation
# Such as a python virtual environment


def find_cadquery_conda_dir():
    """Search for installed cadquery conda instance"""

    # Search the Home directory
    cadquery_home = path.join(path.expanduser("~"), "cadquery")
    if path.isdir(cadquery_home):
        return cadquery_home

    # Search the ProgramData directory for system wide installs
    if sys.platform == "win32":
        cadquery_progfiles = path.join(environ["ALLUSERSPROFILE"], "cadquery")
        if path.isdir(cadquery_progfiles):
            return cadquery_progfiles

    return None


def import_cadquery_conda(condapath=None):
    """Attempt to locate and import cadquery from an external conda install"""
    if condapath is None:
        condapath = find_cadquery_conda_dir()
    if condapath is not None:
        site_dir = path.join(condapath, "lib/site-packages")
        sys.path.append(site_dir)
        bin_dir = path.join(condapath, "Library/bin")
        os.add_dll_directory(bin_dir)


import_cadquery_conda()
