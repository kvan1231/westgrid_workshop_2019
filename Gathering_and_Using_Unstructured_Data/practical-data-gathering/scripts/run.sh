#!/bin/bash

docker run -it -p 8080:8888 --name notebook -v "$PWD/../work":/home/docker/data/work minpy:v1 