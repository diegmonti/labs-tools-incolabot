#!/bin/bash

rm /data/project/incolabot/log/*.txt 

cd /data/project/incolabot/pywikipedia && git pull > /data/project/incolabot/log/upbot.txt 2>&1
