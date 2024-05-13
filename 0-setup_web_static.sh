#!/usr/bin/env bash
#deployment pre processes
sudo apt-get update
sudo apt-get install nginx -y
sudo ufw allow 'Nginx HTTP'
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
sample="<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Test Page</title>
</head>
<body>
    <h1>This is a test page</h1>
    <p>Hello, world!</p>
</body>
</html>"
sudo bash -c "echo -e '$sample' > /data/web_static/releases/test/index.html"
sudo ln -sn /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
new_loc=\
"\\tlocation /hbnb_static {\\n\\t\\talias /data/web_static/current;\\n\\t}"
sudo sed -i "/server_name 355975-web-01;/a\\ $new_loc" /etc/nginx/sites-enabled/default
sudo nginx -s reload
if [[ $(pgrep -c nginx) -lt 2 ]]; then
	sudo service nginx start
else
	sudo service nginx restart
fi
