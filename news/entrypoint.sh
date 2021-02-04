#!/bin/sh
# script executed after spark-master serivce created by docker-compose (service's entrypoint)
cd /home/jovyan/work/
# install dependencies (required for cron job + notebook)

pip3 install -r requirements.txt

# launch cron job
./cron_job.py

# enable cron daemon in foreground (in order to keep the service / container active)
/usr/sbin/crond -f