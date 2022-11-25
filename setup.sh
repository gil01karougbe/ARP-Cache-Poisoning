#!/bin/bash

#1- Python3 Check
unamestr=$(uname)
if ! [ -x "$(command -v python3)" ]; then
    echo '[ERROR] python3 is not installed.' >&2
    exit 1
fi

# Python3 Version Check
python_version="$(python3 --version 2>&1 | awk '{print $2}')"
py_major=$(echo "$python_version" | cut -d'.' -f1)
py_minor=$(echo "$python_version" | cut -d'.' -f2)
if [ "$py_major" -eq "3" ] && [ "$py_minor" -gt "7" ]; then
    echo "[INSTALL] Found Python ${python_version}"
else
    echo "[ERROR] MobSF dependencies require Python 3.8/3.9. You have Python version ${python_version} or python3 points to Python ${python_version}."
    exit 1
fi


#2- Pip check
python3 -m pip -V
if [ $? -eq 0 ]; then
    echo '[INSTALL] Found pip'
    if [[ $unamestr == 'Darwin' ]]; then
        python3 -m pip install --no-cache-dir --upgrade pip
    else
        python3 -m pip install --no-cache-dir --upgrade pip --user
    fi
else
    echo '[ERROR] python3-pip not installed'
    exit 1
fi

python3 -m pip install scapy sys os

chmod +x arp_poison.py



