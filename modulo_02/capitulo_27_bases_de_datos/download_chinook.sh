#!/bin/bash

sudo apt update
sudo apt install --yes unzip 
sudo apt install --yes sqlite3

wget https://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip
unzip chinook.zip
rm chinook.zip
