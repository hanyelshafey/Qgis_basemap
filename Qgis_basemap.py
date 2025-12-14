# ============================================================
# QGIS XYZ Basemap Loader
# ------------------------------------------------------------
# Original concept inspired by community scripts (GPL-3)
# Significant refactoring, restructuring, and extensions by:
#
# Author (Modifications): Hani Elshafei
# Organization: SAI , Spatial Artificial Intelligence
# Year: 2025
#
# License:
# This script is distributed under the GNU GPL v3 license.
# You are free to use, modify, and redistribute this script
# under the same license terms.
#
# DISCLAIMER:
# Tile services (Google, Esri, etc.) are subject to their own
# terms of service. The author is not responsible for misuse.
# ============================================================

from qgis.PyQt.QtCore import QSettings
from qgis.utils import iface


def xyz_source(
    name,
    url,
    zmax="19",
    zmin="0",
    referer="",
    authcfg="",
    username="",
    password=""
):
    """
    Helper function to define an XYZ basemap source
    """
    return {
        "type": "connections-xyz",
        "name": name,
        "url": url,
        "zmax": zmax,
        "zmin": zmin,
        "referer": referer,
        "authcfg": authcfg,
        "username": username,
        "password": password,
    }


XYZ_SOURCES = [
    xyz_source(
        "Google Satellite",
        "https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}"
    ),
    xyz_source(
        "Google Maps",
        "https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}"
    ),
    xyz_source(
        "Esri World Imagery",
        "https://server.arcgisonline.com/ArcGIS/rest/services/"
        "World_Imagery/MapServer/tile/{z}/{y}/{x}",
        zmax="17"
    ),
    xyz_source(
        "OpenStreetMap Standard",
        "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
        zmax="19"
    ),
]


def register_xyz_sources(sources):
    """
    Register XYZ sources inside QGIS Browser
    """
    settings = QSettings()

    for src in sources:
        base_key = f"qgis/{src['type']}/{src['name']}"
        settings.setValue(f"{base_key}/url", src["url"])
        settings.setValue(f"{base_key}/zmax", src["zmax"])
        settings.setValue(f"{base_key}/zmin", src["zmin"])
        settings.setValue(f"{base_key}/referer", src["referer"])
        settings.setValue(f"{base_key}/authcfg", src["authcfg"])
        settings.setValue(f"{base_key}/username", src["username"])
        settings.setValue(f"{base_key}/password", src["password"])

    iface.reloadConnections()


# === Execute ===
register_xyz_sources(XYZ_SOURCES)
