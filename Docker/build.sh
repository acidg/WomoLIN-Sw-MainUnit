#!/bin/bash

source tools.sh
setAppFromShellName $1

echo "Buildname: ${APP}"

sudo docker build --tag womo$APP --file Dockerfile_$APP .
