#! /bin/bash

g++ -Ofast -Wall -fPIC -c my.cpp
g++ -shared -o libmycpp.so my.o
