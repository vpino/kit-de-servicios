#!/usr/bin/env bash

apt-get autoremove
apt-get autoclean
apt-get clean

find / -name "*.pyc" -print0 | xargs -0r rm -rf
find /var/cache/apt -type f -print0 | xargs -0r rm -rf
find /var/lib/apt/lists -type f -print0 | xargs -0r rm -rf
find /usr/share/man -type f -print0 | xargs -0r rm -rf
find /usr/share/doc -type f -print0 | xargs -0r rm -rf
find /usr/share/locale -type f -print0 | xargs -0r rm -rf
find /var/log -type f -print0 | xargs -0r rm -rf
find /var/tmp -type f -print0 | xargs -0r rm -rf
find /tmp -type f -print0 | xargs -0r rm -rf

exit 0
