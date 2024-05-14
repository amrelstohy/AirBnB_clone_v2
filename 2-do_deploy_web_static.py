#!/usr/bin/python3
"""
Deploying archive
"""

from fabric.api import put, run
from fabric import Connection
import os

if __name__ == "__main__":
    env.hosts = ['54.165.2.91', '54.210.108.204']
    env.user = ['ubuntu']
    env.key_filename = '~/.ssh/school'


    def do_deploy(archive_path):
        """
        functiun of deployment
        """


        if not os.path.exists(archive_path):
            return (None)
        try:
            put(archive_path, "/tmp/")
            archive_name = archive_path.split('/')[-1]
            folder_name = archivename.split('.')[0]
            run("sudo mkdir -p /data/web_static/releases/{}/".format(folder_name))
            run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
                archive_name, folder_name))
            run("sudo rm /tmp/{}".format(archivename))
            run("sudo rm -rf /data/web_static/current")
            run("ln -sf /data/web_static/releases/{}/"
                "/data/web_static/current".format(folder_name))
            return (True)
        except Exception as e:
            return (False)
