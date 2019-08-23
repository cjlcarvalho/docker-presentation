#! /bin/bash

cp -r ../app/ .

sudo docker build -t app .
sudo docker run -d -p 8000:8000 app

rm -rf ./app
