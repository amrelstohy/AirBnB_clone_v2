#!/usr/bin/python3
"""
this module is for compressing and deployment
"""


from fabric.api import put, run, env, local
from datetime import datetime
import os


env.hosts = ['100.25.2.69', '34.227.93.105']


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


def do_deploy(archive_path):
    """
    functiun of deployment
    """

    if not os.path.exists(archive_path):
        return (None)
    try:
        put(archive_path, "/tmp/")
        archive_name = archive_path.split('/')[-1]
        folder_name = archive_name.split('.')[0]
        if run("sudo mkdir -p /data/web_static/releases/{}".format(
                folder_name)).failed is True:
            return (False)
        if run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
                archive_name, folder_name)).failed is True:
            return (False)
        if run("sudo rm /tmp/{}".format(archive_name)).failed is True:
            return (False)
        if run("sudo rm -rf /data/web_static/current").failed is True:
            return (False)
        if run("sudo mv /data/web_static/releases/{0}/web_static/*"
                " /data/web_static/releases/{0}/".format(
                    folder_name)).failed is True:
            return (False)
        run("sudo mv /data/web_static/releases/{0}/103-index.html"
            " /data/web_static/releases/{0}/index.html".format(
                folder_name))
        if run("sudo rm -rf /data/web_static/releases/{}/web_static".format(
                folder_name)).failed is True:
            return (False)
        if run("sudo ln -sf /data/web_static/releases/{}/"
                " /data/web_static/current".format(
                    folder_name)).failed is True:
            return (False)
        if run("sudo chown -R ubuntu:ubuntu /data/").failed is True:
            return (False)
        if run("sudo chmod -R 755 /data").failed is True:
            return (False)
        return (True)
    except Exception as e:
        return (False)


def deploy():
    """
    iam here making a full deploy
    """

    file_path = do_pack()
    if file_path is None:
        return (False)
    return (do_deploy(file_path))
