#!/bin/sh
# script executed after spark-master serivce created by docker-compose (service's entrypoint)
cd /home/jovyan/work
# The streamlit dependency WON'T be installed by docker
# If you try to install it, it will fails and show the following message :
# RuntimeError: Broken toolchain: cannot link a simple C program
# It is due to the numpy library that is not likely compatible with this Linux distribution
sed "s/streamlit//g" requirements.txt > requirements_docker.txt
# install dependencies (required for cron job + notebook)
echo "dependency installation from requirements_docker.txt"
pip3 install -r requirements_docker.txt
# This temporary file is no longer needed after the pip installation
rm requirements_docker.txt

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
