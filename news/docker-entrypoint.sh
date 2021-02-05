#!/bin/sh
# script executed after spark-master serivce created by docker-compose (service's entrypoint)
cd /home/jovyan/work/
# install dependencies (required for cron job + notebook)

pip3 install -r requirements.txt

# enable cron daemon
/usr/sbin/crond

echo "cron daemon launched"

# launch cron job
./cron_job.py

cp /spark/conf/spark-defaults.conf.template /spark/conf/spark-defaults.conf

# Add spark mongo connector for pspark

echo "spark.jars.packages   org.mongodb.spark:mongo-spark-connector_2.12:3.0.1" >> /spark/conf/spark-defaults.conf

#execute spark-master's original entrypoint

chmod +x /master.sh && /master.sh
