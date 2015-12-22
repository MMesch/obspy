# -*- coding: utf-8 -*-
# -------------------------------------------------------------------
# Filename: gcpaths.py
#  Purpose: Returns paths that connect stations with events
#   Author: Matthias Meschede
#    Email: meschede@ipgp.fr
#
# Copyright (C) 2015 Matthias Meschede
# ---------------------------------------------------------------------

"""
Provides functions to get greatcircle paths between stations and events in 2D
(on the surface) and 3D (combined with taup). Plotting routines for matplotlib
(basemap) and vtk (for 3D path plots) are available as well.

:copyright:
    The ObsPy Development Team (devs@obspy.org)
:license:
    GNU Lesser General Public License, Version 3
    (http://www.gnu.org/copyleft/lesser.html)

.. _`Generic Mapping Tools (GMT)`: http://gmt.soest.hawaii.edu
.. _`bb.m`: http://www.ceri.memphis.edu/people/olboyd/Software/Software.html
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from future.builtins import *  # NOQA @UnusedWildImport

import io
import warnings

import numpy as np
import matplotlib.pyplot as plt

def get_gcpaths(inventory, lat, lon):

if __name__ == '__main__':
    import doctest
    doctest.testmod()
