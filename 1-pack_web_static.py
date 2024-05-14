#!/usr/bin/python3
"""
this module is for compressing and deployment
"""


from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    sssssss
    """
    if not os.path.exists("versions"):
        os.makedirs("versions")

    now = datetime.now()
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
        now.year, now.month, now.day, now.hour, now.minute, now.second)
    result = local("tar -cvzf versions/{} web_static".format(
        archive_name), capture=True)
    if result.succeeded:
        return (os.path.join("versions", archive_name))
    else:
        return (None)
