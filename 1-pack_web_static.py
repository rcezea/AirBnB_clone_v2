#!/usr/bin/python3
"""
Create a .tgz archive for web static
"""

from datetime import datetime
from fabric.api import local


def do_pack():
    """
    packing web static files
    """

    try:
        dateT = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        file_dir = "versions/web_static_{}.tgz".format(dateT)
        local("tar -cvzf {} web_static".format(file_dir))
        return file_dir

    except Exception:
        return None
