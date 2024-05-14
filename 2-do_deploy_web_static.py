#!/usr/bin/python3
"""
Deploying archive
"""

from fabric.api import put, run, env
import os

env.hosts = ['54.165.2.91', '54.210.108.204']


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
        run("sudo mkdir -p /data/web_static/releases/{}".format(folder_name))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
            archive_name, folder_name))
        run("sudo rm /tmp/{}".format(archive_name))
        run("sudo rm -rf /data/web_static/current")
        run("ln -sf /data/web_static/releases/{}/web_static"
            " /data/web_static/current".format(folder_name))
        run("sudo chown -R ubuntu:ubuntu /data/")
        return (True)
    except Exception as e:
        return (False)
