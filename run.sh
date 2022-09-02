#!/bin/bash

if ! command -v python3 &> /dev/null
then
    echo "python3 could not be found"
    exit
fi

python3 server.py &
sleep 1
./build/network-example