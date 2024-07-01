#!/usr/bin/python3
"""
Deploying archive
"""

from fabric.api import put, run, env, local
from datetime import datetime
import os

env.hosts = ['34.239.207.34', '54.237.34.156']


def do_deploy(archive_path):
    """
    functiun of deployment
    """

    if not os.path.exists(archive_path):
        return (False)
    try:
        put(archive_path, "/tmp/")
        archive_name = archive_path.split('/')[-1]
        folder_name = archive_name.split('.')[0]
        if run("sudo mkdir -p /data/web_static/releases/{}/".format(
                folder_name)).failed is True:
            return (False)
        if run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
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
        if run("sudo rm -rf /data/web_static/releases/{}/web_static".format(
                folder_name)).failed is True:
            return (False)
        if run("sudo ln -s /data/web_static/releases/{}/"
                " /data/web_static/current".format(
                    folder_name)).failed is True:
            return (False)
        return (True)
    except Exception as e:
        return (False)
